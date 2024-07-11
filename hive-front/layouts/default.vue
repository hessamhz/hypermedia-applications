<template>
  <div>
    <header>
      <AppHeader />
    </header>
    <main class=" mt-24 ">
      <slot />
    </main>
    <AppFooter/>
  </div>
</template>
<script setup lang="ts">
import AppFooter from "~/components/app/AppFooter.vue";
</script>
