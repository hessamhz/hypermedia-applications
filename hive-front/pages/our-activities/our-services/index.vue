<script setup>
const { data } = await useApi('services');
</script>

<template>
  <div>
    <header
      class="bg-gradient-to-r from-purple-700 to-orange-300 px-5 py-8 md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <h1
        class="text-3xl font-bold text-white md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl"
      >
        Our Services
      </h1>
    </header>
    <div
      class="mx-auto max-w-[1240px] px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <ul class="space-y-3 lg:space-y-4 2xl:space-y-5">
        <li
          v-for="service in data"
          :key="service.slug"
          class="flex even:flex-row-reverse md:gap-3 lg:gap-4 2xl:gap-5 [&>*]:odd:bg-orange-100 [&>*]:even:bg-purple-100"
        >
          <div
            class="hidden aspect-square h-44 shrink-0 rounded-xl md:block lg:h-52 lg:rounded-[20px] xl:h-56"
          ></div>
          <NuxtLink
            :to="`/our-activities/our-services/${service.slug}`"
            class="grow rounded-xl p-5 md:h-44 md:p-6 lg:h-52 lg:rounded-[20px] lg:p-7 xl:h-56 xl:p-8 2xl:p-9"
          >
            <h2 class="pb-2 text-xl font-semibold lg:text-2xl xl:text-3xl">
              {{ service.title }}
            </h2>
            <p class="line-clamp-4 lg:text-lg xl:text-xl">
              {{ service.overview }}
            </p>
          </NuxtLink>
        </li>
      </ul>
    </div>
  </div>
</template>
