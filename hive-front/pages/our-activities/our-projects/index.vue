<script setup>
import SectionHeader from '~/components/app/SectionHeader.vue';

const { data } = await useApi('projects/');

// Define SEO metadata for the page
useSeoMeta({
  title: 'Our Projects | The Hive',
  description:
    'Learn more about the projects we are working on at The Hive, Anti-Violence Center for Women.',
  ogTitle: 'Our Projects | The Hive',
  ogType: 'website',
  ogUrl: 'https://the-hive.space/',
  canonical: 'https://the-hive.space/',
  ogSiteName: 'The Hive',
});
</script>

<template>
  <div>
    <SectionHeader
      title="Our Projects"
      backgroundColor="bg-gradient-to-r from-hive-yellow to-hive-purple"
      color="black"
    ></SectionHeader>
    <div
      class="mx-auto max-w-[1240px] px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <!-- Projects list -->
      <ul class="grid gap-3 sm:grid-cols-2 lg:gap-4 2xl:gap-5">
        <!-- Iterate over each project and create a list item -->
        <!-- Basically the view here is based on a periodic reccurence of items in the list that we -->
        <!-- have based on 7 item periodicity (if you look at the ui you will understand it better) -->
        <li
          v-for="project in data"
          :key="project.slug"
          class="sm:[&:nth-child(7n+1)>a>div]:w-1/2 sm:[&:nth-child(7n+1)>a>div]:items-start sm:[&:nth-child(7n+1)]:col-span-2 sm:[&:nth-child(7n+2)>a>div]:mx-auto sm:[&:nth-child(7n+2)>a>div]:w-4/5 sm:[&:nth-child(7n+2)>a>div]:items-center sm:[&:nth-child(7n+3)>a>div]:mx-auto sm:[&:nth-child(7n+3)>a>div]:w-4/5 sm:[&:nth-child(7n+3)>a>div]:items-center sm:[&:nth-child(7n+3)>a>div]:text-center sm:[&:nth-child(7n+4)>a>div]:w-1/2 sm:[&:nth-child(7n+4)>a>div]:items-start sm:[&:nth-child(7n+4)]:col-span-2 sm:[&:nth-child(7n+5)>a>div]:mx-auto sm:[&:nth-child(7n+5)>a>div]:w-4/5 sm:[&:nth-child(7n+5)>a>div]:items-center sm:[&:nth-child(7n+6)>a>div]:mx-auto sm:[&:nth-child(7n+6)>a>div]:w-4/5 sm:[&:nth-child(7n+6)>a>div]:items-center sm:[&:nth-child(7n+7)>a>div]:mx-auto sm:[&:nth-child(7n+7)>a>div]:w-4/5 sm:[&:nth-child(7n+7)>a>div]:items-center"
        >
          <NuxtLink
            :to="{
              name: 'our-activities-our-projects-slug',
              params: { slug: project.slug },
            }"
            :style="{ backgroundImage: `url(${project.picture.file})` }"
            class="block h-full w-full rounded-xl bg-cover bg-center bg-no-repeat px-5 py-8 text-white shadow-[inset_0_0_0_2000px_rgba(1,1,1,0.5)] sm:px-6 sm:py-10 md:px-9 md:py-14 lg:rounded-[20px] lg:px-10 lg:py-16 xl:px-11 2xl:px-12 2xl:py-20"
          >
            <div
              class="flex flex-col items-start rounded-lg bg-white bg-opacity-10 p-4 backdrop-blur-lg"
            >
              <h2
                class="pb-4 text-xl font-bold md:pb-6 md:text-2xl lg:pb-8 lg:text-3xl"
              >
                {{ project.title }}
              </h2>
              <p class="line-clamp-4 md:text-lg lg:text-xl">
                {{ project.overview }}
              </p>
              <NuxtLink
                :to="{
                  name: 'our-activities-our-projects-slug',
                  params: { slug: project.slug },
                }"
                class="mt-4 rounded-lg bg-white px-3 py-2 text-black hover:bg-gray-200 hover:duration-150 hover:ease-in sm:px-4 sm:py-3"
              >
                Read more
              </NuxtLink>
            </div>
          </NuxtLink>
        </li>
      </ul>
    </div>
  </div>
</template>
