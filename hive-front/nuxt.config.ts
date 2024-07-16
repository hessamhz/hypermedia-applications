// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: true,
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@nuxt/eslint', 'nuxt-swiper'],
  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      link: [
        {
          rel: 'apple-touch-icon',
          sizes: '180x180',
          href: '/apple-touch-icon.png',
        },
        {
          rel: 'icon',
          type: 'image/png',
          sizes: '32x32',
          href: '/favicon-32x32.png',
        },
        {
          rel: 'icon',
          type: 'image/png',
          sizes: '16x16',
          href: '/favicon-16x16.png',
        },
        { rel: 'manifest', href: '/site.webmanifest' },
      ],
    },
  },
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
