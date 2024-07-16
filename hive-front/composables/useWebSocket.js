/* eslint-disable no-console */

import { ref, onMounted, onUnmounted, watch } from 'vue';

export function useWebSocket() {
  const socket = ref(null);
  const messages = ref([]);
  const error = ref(null);

  // Save messages to localStorage so we persist the messages on client side
  // Altough we are also keeping them on open AI as well (theads)
  const saveMessages = () => {
    localStorage.setItem('chatHistory', JSON.stringify(messages.value));
  };

  // Load messages from localStorage
  const loadMessages = () => {
    const savedMessages = localStorage.getItem('chatHistory');
    if (savedMessages) {
      messages.value = JSON.parse(savedMessages);
    }
  };

  const maxReconnectAttempts = 5; // Maximum number of reconnection attempts
  let reconnectAttempts = 0; // Current number of reconnection attempts

  const isBotTyping = ref(false); // Track bot typing status for showing is typing indicator

  // Function to establish WebSocket connection
  const connect = () => {
    let wsEndpoint = '';
    // thread_id is a unique identifier for the backend for each thread (conversation)
    if (localStorage.getItem('thread_id')) {
      // recalling the last conversation (since we have the backend uses this id
      // to recall the last conversation from open AI
      wsEndpoint = `wss://the-hive.space/ws/chat/?id=${localStorage.getItem('thread_id')}`;
    } else {
      // if there is no thread_id, we start a new conversation to fetch a thread id from the backend
      // basically the first message sent to the backend will return a thread_id and you cannot
      // continue a conversation without a thread_id
      wsEndpoint = 'wss://the-hive.space/ws/chat/';
    }
    socket.value = new WebSocket(wsEndpoint);

    socket.value.onopen = () => {
      console.log('WebSocket connected');
      reconnectAttempts = 0; // reset reconnection attempts
    };

    socket.value.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.thread_id) localStorage.setItem('thread_id', data.thread_id); // Save thread_id to localStorage
        if (data.message) {
          messages.value.unshift({
            text: data.message,
            sender: 'bot',
            timestamp: new Date().toISOString(), // keep the timestamp for each message
          });
          saveMessages();
        } else if (data.error) {
          error.value = data.error;
        }
      } catch (e) {
        console.error('Error parsing message:', e);
        error.value = 'Error parsing server response';
      }

      isBotTyping.value = false;
    };

    socket.value.onerror = (event) => {
      console.error('WebSocket error:', event);
      error.value = `WebSocket error: ${event.type}`;
    };

    socket.value.onclose = (event) => {
      console.log('WebSocket disconnected:', event.code, event.reason);
      error.value = `WebSocket disconnected: ${event.code} ${event.reason}`;

      if (reconnectAttempts < maxReconnectAttempts) {
        reconnectAttempts++;
        console.log(
          `Attempting to reconnect (${reconnectAttempts}/${maxReconnectAttempts})...`
        );
        setTimeout(connect, 3000); // Try to reconnect after 3 seconds
      } else {
        error.value =
          'Max reconnection attempts reached. Please refresh the page.';
      }
    };
  };

  // Function to send a message through the WebSocket
  const sendMessage = (query) => {
    if (socket.value?.readyState === WebSocket.OPEN) {
      // Saving the whole conversation as a context in case backend wants to process it
      const context = localStorage.getItem('chatContext') || '';
      const message = JSON.stringify({ context, query });
      socket.value.send(message);
      localStorage.setItem('chatContext', context + '\n' + query);
      messages.value.unshift({
        text: query,
        sender: 'user',
        timestamp: new Date().toISOString(),
      });
      saveMessages(); // Save messages after adding a new one
    } else {
      console.error('WebSocket is not connected');
    }
  };

  // Lifecycle hook to handle WebSocket connection on component mount
  onMounted(() => {
    loadMessages();
    connect();
    if (socket.value) {
      setTimeout(() => {
        reconnectAttempts = maxReconnectAttempts; // Stop reconnecting
        socket.value.close();
      }, 1000);
    }
    setTimeout(() => connect(), 1100);
  });

  onUnmounted(() => {
    if (socket.value) {
      reconnectAttempts = maxReconnectAttempts; // Stop reconnecting
      socket.value.close();
    }
  });

  // Watcher to save messages whenever the messages array changes
  watch(
    messages,
    () => {
      saveMessages();
    },
    { deep: true }
  );

  // Function to clear message history and local storage
  const clearHistory = () => {
    messages.value = []; // Clear messages array
    localStorage.removeItem('chatHistory'); // Remove chat history from localStorage
    localStorage.removeItem('chatContext'); // Remove chat context from localStorage
    localStorage.removeItem('thread_id'); // Remove thread_id from localStorage

    connect();
    setTimeout(() => {
      reconnect();
    }, 1000);
  };

  // Function to handle WebSocket reconnection
  const reconnect = () => {
    reconnectAttempts = maxReconnectAttempts; // Stop reconnecting
    socket.value.close();

    socket.value = null; // Reset socket
    setTimeout(() => {
      reconnectAttempts = 0;
      connect();
    }, 1000);
  };

  // "is typing" indicator for the bot to show that it is "typing...
  const simulateBotTyping = () => {
    isBotTyping.value = true;
  };

  // Return references and functions for use in the component
  return {
    messages,
    error,
    sendMessage,
    loadMessages,
    saveMessages,
    clearHistory,
    isBotTyping,
    simulateBotTyping,
  };
}
