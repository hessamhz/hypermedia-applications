<script setup>
import SectionHeader from '~/components/app/SectionHeader.vue';

const { data } = await useApi('services/');

// Define SEO metadata for the page
useSeoMeta({
  title: 'Our Services | The Hive',
  description:
    'Learn more about the services offered at The Hive, Anti-Violence Center for Women.',
  ogTitle: 'Our Services | The Hive',
  ogType: 'website',
  ogUrl: 'https://the-hive.space/',
  canonical: 'https://the-hive.space/',
  ogSiteName: 'The Hive',
});
</script>

<template>
  <div>
    <SectionHeader title="Our Services"></SectionHeader>
    <div
      class="mx-auto max-w-[1240px] px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <!-- Services list -->
      <ul class="space-y-3 lg:space-y-4 2xl:space-y-5">
        <li
          v-for="service in data"
          :key="service.slug"
          class="flex flex-col gap-1 sm:flex-row sm:even:flex-row-reverse md:gap-3 lg:gap-4 2xl:gap-5 [&>*]:odd:bg-purple-300 [&>*]:even:bg-purple-200"
        >
          <!-- Had to create to distinct NuxtLinks because flex wouldn't operate correctly otherwise, and we really need the image to be selectable -->
          <NuxtLink
            :to="{
              name: 'our-activities-our-services-slug',
              params: { slug: service.slug },
            }"
            class="flex h-44 shrink-0 items-center justify-center rounded-xl sm:aspect-square sm:h-44 md:block lg:h-52 lg:rounded-[20px] xl:h-56"
            :class="!service.picture && 'hidden sm:block'"
          >
            <img
              v-if="service.picture"
              :src="service.picture.file"
              :alt="service.title"
              class="max-w-28 rounded-xl object-cover sm:h-full sm:w-full sm:max-w-max sm:p-12 lg:rounded-[20px]"
            />
          </NuxtLink>
          <div
            class="flex grow flex-col items-center justify-between gap-2 rounded-xl p-5 text-center sm:items-start sm:text-start md:h-44 md:p-6 lg:h-52 lg:rounded-[20px] lg:p-7 xl:h-56 xl:p-8 2xl:p-9"
          >
            <div class="flex flex-col gap-1">
              <h2 class="text-xl font-semibold lg:text-2xl xl:text-3xl">
                {{ service.title }}
              </h2>
              <p class="lg:text-lg xl:text-xl">
                {{ service.overview }}
              </p>
            </div>
            <NuxtLink
              :to="{
                name: 'our-activities-our-services-slug',
                params: { slug: service.slug },
              }"
              class="rounded-lg bg-white px-3 py-2 hover:bg-gray-200 hover:duration-150 hover:ease-in sm:px-4 sm:py-3"
              :class="!service.picture && 'hidden sm:block'"
            >
              Read More
            </NuxtLink>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
