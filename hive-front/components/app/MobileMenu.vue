<script setup>
defineProps({
  isOpen: Boolean,
});

defineEmits(['close']);
</script>

<template>
  <div
    class="app-mobile-menu fixed bottom-0 right-0 top-0 z-10 flex h-full w-48 flex-col border-l border-gray-400 bg-white px-5 py-8 transition-transform"
    :class="isOpen ? 'translate-x-0' : 'translate-x-full'"
  >
    <button
      class="mb-10 self-end"
      @click="$emit('close')"
    >
      <IconX />
    </button>
    <nav class="self-center">
      <ul class="space-y-6">
        <li>
          <NuxtLink
            to="/"
            exact
          >
            Home
          </NuxtLink>
        </li>
        <li>
          <NuxtLink to="/who-we-are/our-team">Who We Are</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/our-activities">Our Activities</NuxtLink>
        </li>
        <li>
          <NuxtLink to="/contacts">Contacts</NuxtLink>
        </li>
      </ul>
    </nav>
  </div>
</template>
