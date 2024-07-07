<script setup>
import { useWebSocket } from '~/composables/useWebSocket';

const { messages, sendMessage: send } = useWebSocket();

const newMessage = ref('');

const sendMessage = () => {
  if (newMessage.value.trim() === '') return;

  send(newMessage.value);

  newMessage.value = '';
};
</script>
<template>
  <div class="">
    <!-- MESSAGES -->
    <div
      class="flex h-[80vh] flex-col-reverse space-y-5 overflow-y-auto px-5 pb-5 pt-10 lg:px-10 lg:pb-9 xl:pb-14"
    >
      <div
        v-for="(message, index) in messages"
        :key="index"
        class="flex"
        :class="{
          'justify-start': message.sender === 'bot',
          'justify-end': message.sender === 'user',
        }"
      >
        <p
          class="max-w-72 rounded-lg px-4 py-2 sm:max-w-96 md:max-w-md md:px-5 md:py-3 md:text-lg xl:px-6 xl:py-4 xl:text-xl"
          :class="{
            'bg-orange-100': message.sender === 'bot',
            'bg-purple-100': message.sender === 'user',
          }"
        >
          {{ message.text }}
        </p>
      </div>
    </div>
    <!-- INPUT -->
    <input
      v-model="newMessage"
      type="text"
      class="fixed bottom-8 left-5 lg:left-10 lg:right-14 right-5 rounded-lg bg-gray-100 px-2 py-4 md:px-3 md:py-5 md:text-lg xl:text-xl"
      placeholder="Type your message... (Press Enter to send.)"
      @keydown.enter="sendMessage"
    />
  </div>
</template>
