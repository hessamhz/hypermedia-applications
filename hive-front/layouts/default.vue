<template>
  <div>
    <AppHeader />
    <main>
      <slot />
    </main>
    <AppFooter/>
  </div>
</template>
<script setup lang="ts">
import AppFooter from "~/components/app/AppFooter.vue";
</script>
