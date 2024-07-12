<script setup>
import { useWebSocket } from '~/composables/useWebSocket';

definePageMeta({
  layout: "chat-layout",
});

const { messages, sendMessage: send, clearHistory } = useWebSocket();

const newMessage = ref('');

const sendMessage = () => {
  if (newMessage.value.trim() === '') return;

  send(newMessage.value);

  newMessage.value = '';
};

function formatTimestamp(timestamp) {
  const date = new Date(timestamp);
  const year = date.getFullYear().toString().slice(-2); // Get last 2 digits of year
  const month = ('0' + (date.getMonth() + 1)).slice(-2); // Month is 0-indexed, add leading zero
  const day = ('0' + date.getDate()).slice(-2); // Add leading zero
  const hours = ('0' + date.getHours()).slice(-2); // Add leading zero
  const minutes = ('0' + date.getMinutes()).slice(-2); // Add leading zero
  return `${year}/${month}/${day} ${hours}:${minutes}`;
}

const isDialogOpen = ref(false);

function openDialog() {
  isDialogOpen.value = true;
}

function closeDialog() {
  isDialogOpen.value = false;
}

function deleteMessages() {
  clearHistory();
  closeDialog();
}

useSeoMeta({
  title: "Chat With Bee | The hive",
  description: "Chat with Bee about The Hive, Anti-Violence Center for Women.",
  ogTitle: "Chat With Bee | The hive",
  ogType: "website",
  ogUrl: "https://the-hive.space/",
  canonical: "https://the-hive.space/",
  ogSiteName: "The Hive"
});
</script>
<template>
  <div
    class="absolute bottom-0 left-0 right-0 top-[89px] flex flex-col overflow-y-hidden"
  >
    <!-- MESSAGES -->
    <div
      class="flex h-full flex-grow flex-col-reverse gap-5 overflow-y-auto px-5 pb-5 pt-10 lg:px-10 xl:pb-8"
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
        <div class="flex flex-col gap-0.5">
          <p
            class="max-w-72 rounded-lg px-4 py-2 sm:max-w-96 md:max-w-md md:px-5 md:py-3 md:text-lg xl:px-6 xl:py-4 xl:text-xl"
            :class="{
              'bg-orange-100': message.sender === 'bot',
              'bg-purple-100': message.sender === 'user',
            }"
          >
            {{ message.text }}
          </p>
          <sub
            class="px-1 text-xs italic text-gray-400 xl:text-sm"
            :class="message.sender === 'user' && 'text-end'"
          >
            {{ formatTimestamp(message.timestamp) }}
          </sub>
        </div>
      </div>
    </div>
    <!-- INPUT -->
    <div class="flex items-center gap-2 bg-white px-5 py-4 md:py-5">
      <button
        class="flex aspect-square w-14 items-center justify-center rounded-full bg-gray-100 md:w-[68px]"
        @click="openDialog"
      >
        <IconTrash class="w-6" />
      </button>
      <input
        v-model="newMessage"
        type="text"
        class="grow rounded-lg bg-gray-100 px-2 py-4 placeholder:text-xs placeholder:sm:text-sm md:px-3 md:py-5 md:text-lg xl:text-xl"
        placeholder="Type your message... (Press Enter to send.)"
        @keydown.enter="sendMessage"
      />
      <button
        class="flex aspect-square w-14 items-center justify-center rounded-full bg-gray-100 md:w-[68px]"
        @click="sendMessage"
      >
        <IconSend class="w-6" />
      </button>
    </div>
    <!-- POPUP -->
    <dialog
      v-if="isDialogOpen"
      class="fixed inset-0 flex items-center justify-center"
    >
      <div class="rounded-lg bg-gray-200 p-5">
        <p class="text-lg">Are you sure you want to delete all messages?</p>
        <div class="mt-5 flex justify-end gap-2">
          <button
            class="rounded-full bg-red-500 px-5 py-2 text-white"
            @click="deleteMessages"
          >
            Yes
          </button>
          <button
            class="rounded-full bg-white px-5 py-2"
            @click="closeDialog"
          >
            No
          </button>
        </div>
      </div>
    </dialog>
  </div>
</template>
