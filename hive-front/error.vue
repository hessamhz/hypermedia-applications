<script setup>
useSeoMeta({
  title: "Error | The Hive",
  ogTitle: "Error | The Hive",
  robots: "noindex",
  ogType: "website",
  ogUrl: "https://the-hive.space/",
  canonical: "https://the-hive.space/",
  ogSiteName: "The Hive",
});
</script>

<template>
  <NuxtLayout>
    <div class="error-page">
      <h1 class="text-4xl font-bold text-hive-purple md:text-5xl">{{ error.statusCode }}</h1>
      <h1 class="p-5 mb-11">{{ error.statusCode === 404 || error.statusCode === 500 ? 'Page not found' : 'Oh no! Something went wrong!' }}</h1>
      <NuxtLink
          to="/"
          class=" rounded-lg bg-hive-purple px-8 py-3 text-white md:text-lg lg:text-xl xl:max-w-80 hover:bg-hive-dark-purple hover:ease-in hover:duration-150"
      >
        Go to Home Page
      </NuxtLink>

    </div>
  </NuxtLayout>
</template>

<script>
export default {
  layout: "no-footer",
  props: {
    error: Object
  }
}
</script>

<style scoped>
.error-page {
  text-align: center;
  margin: 50px auto;
  padding: 40px;
}
</style>
