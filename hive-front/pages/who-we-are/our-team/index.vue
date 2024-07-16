<script setup>
import SectionHeader from '~/components/app/SectionHeader.vue';

const { data } = await useApi('members/');

// Define SEO metadata for the page
useSeoMeta({
  title: `The Team | The Hive`,
  description: 'Meet the team of The Hive, Anti-Violence Center for Women.',
  ogTitle: 'The Team | The Hive',
  ogType: 'profile',
  ogUrl: 'https://the-hive.space/',
  canonical: 'https://the-hive.space/',
  ogSiteName: 'The Hive',
});
</script>

<template>
  <div>
    <SectionHeader title="Our Team"></SectionHeader>
    <div class="px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28">
      <ul
        class="grid gap-10 md:grid-cols-2 md:gap-x-16 md:gap-y-12 lg:grid-cols-3 lg:gap-x-20 xl:grid-cols-4 xl:gap-x-24"
      >
        <li
          v-for="person in data"
          :key="person.slug"
          class="mx-auto md:mx-0"
        >
          <NuxtLink
            :to="{
              name: 'who-we-are-our-team-slug',
              params: { slug: person.slug },
            }"
            class="flex flex-col items-center hover:opacity-50 hover:duration-150 hover:ease-in-out"
          >
            <div
              class="hexagon mb-4 flex w-[144px] items-center justify-center bg-orange-300 sm:w-[180px] xl:w-[200px]"
            >
              <img
                :src="person?.avatar.file"
                :alt="person?.name"
                class="hexagon w-[138px] object-cover sm:w-[172px] xl:w-[192px]"
              />
            </div>
            <h2 class="mb-px max-w-[18ch] text-center font-bold xl:text-lg">
              {{ person.name }}
            </h2>
            <h3
              class="max-w-[24ch] text-center font-medium text-purple-700 xl:text-lg"
            >
              {{ person.role }}
            </h3>
          </NuxtLink>
        </li>
      </ul>
      <p class="pt-16 text-center text-sm text-gray-600">
        All suggested names and pictures are either fictional or taken from
        <a href="https://www.pexels.com">https://www.pexels.com</a>
        .
      </p>
      <p class="text-center text-sm text-gray-600">
        This website is a project created for educational purposes.
      </p>
    </div>
  </div>
</template>
