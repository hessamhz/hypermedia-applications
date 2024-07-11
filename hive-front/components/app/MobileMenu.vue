<script setup>
defineProps({
  isOpen: Boolean,
});

defineEmits(['close']);
</script>

<template>
  <div
    class="app-mobile-menu fixed bottom-0 right-0 top-0 z-[999] flex h-full w-48 flex-col border-l border-gray-400 bg-white px-5 py-8 transition-transform"
    :class="isOpen ? 'translate-x-0' : 'translate-x-full'"
  >
    <button
      class="mb-10 self-end"
      @click="$emit('close')"
    >
      <IconX />
    </button>
    <nav class="self-start">
      <NuxtLink
        to="/"
        exact
        class="block"
        @click="$emit('close')"
      >
        Home
      </NuxtLink>

      <div class="mb-2 mt-8 text-xs text-gray-400">Who Are We</div>
      <NuxtLink
        to="/who-we-are/our-team"
        class="mb-2 ml-2 block"
        @click="$emit('close')"
      >
        Our Team
      </NuxtLink>
      <NuxtLink
        to="/who-we-are/about"
        class="ml-2 block"
        @click="$emit('close')"
      >
        About
      </NuxtLink>
      <div class="mb-1 mt-8 text-xs text-gray-400">Our Activities</div>
      <NuxtLink
        to="/our-activities/our-projects"
        class="mb-2 ml-2 block"
        @click="$emit('close')"
      >
        Our Projects
      </NuxtLink>
      <NuxtLink
        to="/our-activities/our-services"
        class="ml-2 block"
        @click="$emit('close')"
      >
        Our Services
      </NuxtLink>
      <NuxtLink
        to="/chat"
        class="mt-8 block"
        @click="$emit('close')"
      >
        Chat with us
      </NuxtLink>
    </nav>
  </div>
</template>

<style scoped>
.app-mobile-menu .router-link-active {
  text-decoration: underline 2px theme('colors.purple.600');
  text-underline-offset: 6px;
}
</style>
