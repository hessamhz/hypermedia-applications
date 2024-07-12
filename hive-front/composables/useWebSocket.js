/* eslint-disable no-console */

import { ref, onMounted, onUnmounted, watch } from "vue";

export function useWebSocket() {
  const socket = ref(null);
  const messages = ref([]);
  const error = ref(null);

  const saveMessages = () => {
    localStorage.setItem("chatHistory", JSON.stringify(messages.value));
  };

  const loadMessages = () => {
    const savedMessages = localStorage.getItem("chatHistory");
    if (savedMessages) {
      messages.value = JSON.parse(savedMessages);
    }
  };

  const maxReconnectAttempts = 5;
  let reconnectAttempts = 0;

  const connect = () => {
    let wsEndpoint = "";
    if (localStorage.getItem("thread_id")) {
      wsEndpoint = `wss://the-hive.space/ws/chat/?id=${localStorage.getItem("thread_id")}`;
    } else {
      wsEndpoint = "wss://the-hive.space/ws/chat/";
    }
    socket.value = new WebSocket(wsEndpoint);

    socket.value.onopen = (e) => {
      console.log("WebSocket connected");
      reconnectAttempts = 0;
    };

    socket.value.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.thread_id) localStorage.setItem("thread_id", data.thread_id);
        if (data.message) {
          messages.value.unshift({
            text: data.message,
            sender: "bot",
            timestamp: new Date().toISOString(),
          });
          saveMessages();
        } else if (data.error) {
          error.value = data.error;
        }
      } catch (e) {
        console.error("Error parsing message:", e);
        error.value = "Error parsing server response";
      }
    };

    socket.value.onerror = (event) => {
      console.error("WebSocket error:", event);
      error.value = `WebSocket error: ${event.type}`;
    };

    socket.value.onclose = (event) => {
      console.log("WebSocket disconnected:", event.code, event.reason);
      error.value = `WebSocket disconnected: ${event.code} ${event.reason}`;

      if (reconnectAttempts < maxReconnectAttempts) {
        reconnectAttempts++;
        console.log(
          `Attempting to reconnect (${reconnectAttempts}/${maxReconnectAttempts})...`
        );
        setTimeout(connect, 3000); // Try to reconnect after 3 seconds
      } else {
        error.value =
          "Max reconnection attempts reached. Please refresh the page.";
      }
    };
  };

  const sendMessage = (query) => {
    if (socket.value?.readyState === WebSocket.OPEN) {
      const context = localStorage.getItem("chatContext") || "";
      const message = JSON.stringify({ context, query });
      socket.value.send(message);
      localStorage.setItem("chatContext", context + "\n" + query);
      messages.value.unshift({
        text: query,
        sender: "user",
        timestamp: new Date().toISOString(),
      });
      saveMessages(); // Save messages after adding a new one
    } else {
      console.error("WebSocket is not connected");
    }
  };

  onMounted(() => {
    loadMessages();
    connect();
  });

  onUnmounted(() => {
    if (socket.value) {
      reconnectAttempts = maxReconnectAttempts; // Stop reconnecting
      socket.value.close();
    }
  });

  watch(
    messages,
    () => {
      saveMessages();
    },
    { deep: true }
  );

  const clearHistory = () => {
    messages.value = []; // Clear messages array
    localStorage.removeItem("chatHistory"); // Remove chat history from localStorage
    localStorage.removeItem("chatContext"); // Remove chat context from localStorage
  };

  return {
    messages,
    error,
    sendMessage,
    loadMessages,
    saveMessages,
    clearHistory,
  };
}
