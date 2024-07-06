<script setup>
const route = useRoute();

const { data } = await useApi(`members/${route.params.slug}`);
</script>

<template>
  <div>
    <header
      class="bg-purple-700 px-5 py-4 font-bold text-white md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <NuxtLink
        to="/who-we-are/our-team"
        class="mb-2 flex items-end gap-2 text-lg md:text-xl lg:text-2xl xl:text-3xl"
      >
        <span class="border-b">Our People</span>
        <IconChevron />
      </NuxtLink>
      <h1 class="text-2xl md:text-3xl lg:text-5xl xl:text-6xl 2xl:text-7xl">
        {{ data?.name }}
      </h1>
    </header>
    <div
      class="mx-auto flex max-w-[1240px] gap-4 px-5 pb-10 pt-32 md:px-20 md:py-16 xl:px-24 xl:py-28"
    >
      <div
        class="relative basis-full rounded-lg bg-purple-100 px-5 pb-8 pt-20 sm:py-8 md:p-10 xl:p-14 2xl:p-20"
      >
        <h2
          id="education"
          class="mb-3 text-2xl font-semibold lg:mb-5 lg:text-3xl xl:text-4xl"
        >
          Education
        </h2>
        <p class="mb-8 w-9/12 lg:mb-12 lg:text-xl xl:mb-16 xl:text-2xl">
          {{ data?.education }}
        </p>
        <h2
          id="main-expertise"
          class="mb-3 text-2xl font-semibold lg:mb-5 lg:text-3xl xl:text-4xl"
        >
          Main Expertise
        </h2>
        <p class="mb-8 lg:mb-12 lg:text-xl xl:mb-16 xl:text-2xl">
          {{ data?.expertise }}
        </p>
        <h2
          id="main-role"
          class="mb-3 text-2xl font-semibold lg:mb-5 lg:text-3xl xl:text-4xl"
        >
          {{ data?.role }}
        </h2>
        <p class="mb-8 lg:mb-12 lg:text-xl xl:mb-16 xl:text-2xl">
          {{ data?.role_description }}
        </p>
        <h2
          id="activities"
          class="mb-3 text-2xl font-semibold lg:mb-5 lg:text-3xl xl:text-4xl"
        >
          Activities
        </h2>
        <ul class="space-y-2 lg:text-xl xl:text-2xl">
          <li
            v-for="service in data?.activities.services"
            :key="service.slug"
          >
            <NuxtLink
              :to="`/our-activities/our-services/${service.slug}`"
              class="border-b border-current text-purple-700"
            >
              {{ service.title }}
            </NuxtLink>
            <span>:</span>
            <p class="inline">&nbsp;{{ service.overview }}</p>
          </li>
          <li
            v-for="project in data?.activities.projects"
            :key="project.slug"
          >
            <NuxtLink
              :to="`/our-activities/our-projects/${project.slug}`"
              class="border-b border-current text-purple-700"
            >
              {{ project.title }}
            </NuxtLink>
            <span>:</span>
            <p class="inline">&nbsp;{{ project.overview }}</p>
          </li>
        </ul>
        <AppHexagonalImage
          :src="data?.avatar.file"
          :alt="data?.name"
          :size="200"
          class="absolute -top-28 right-1/2 flex translate-x-1/2 items-center justify-center bg-orange-300 sm:-right-12 sm:-top-24 sm:translate-x-0"
        />
      </div>
      <ul class="hidden basis-44 pt-28 text-gray-500 sm:block">
        <li>
          <a href="#education">Education</a>
        </li>
        <li>
          <a href="#main-expertise">Main Expertise</a>
        </li>
        <li>
          <a href="#main-role">{{ data?.role }}</a>
        </li>
        <li>
          <a href="#activities">Activities</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.hexagon {
  --size: 200px;
}
.hexagon.wrapper {
  --size: 205px;
}
</style>