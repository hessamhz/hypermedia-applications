// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxt/eslint', 'nuxt-swiper'],
  swiper: {
    modules: ['autoplay'],
  },
  runtimeConfig: {
    public: {
      baseURL: 'https://the-hive.space/api/v1',
    },
  },
  css: [
    '~/assets/css/custom-styles.css',
    '~/assets/css/tailwind.css',
    '~/assets/css/font-face/inter.css',
  ],
});
