<script setup>
import SectionHeader from "~/components/app/SectionHeader.vue";

const route = useRoute();

const { data } = await useApi(`members/${route.params.slug}/`);
</script>

<template>
  <div>
    <SectionHeader :title="data?.name" background-color="bg-hive-purple" linkTo="/who-we-are/our-team"></SectionHeader>
    <div
      class="mx-auto flex max-w-[1240px] items-start gap-4 px-5 pb-10 pt-32 md:px-20 md:py-16 xl:px-24 xl:py-28"
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
          Main Role
        </h2>
        <p class="mb-8 lg:mb-12 lg:text-xl xl:mb-16 xl:text-2xl">
          {{ data?.role_description }}
        </p>
        <!-- Activities -->
        <div
            v-show="data && (data?.activities.services.length || data?.activities.projects.length)"
        >
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
                  :to="{ name: 'our-activities-our-projects-slug', params: { slug: project.slug } }"
                  class="border-b border-current text-purple-700"
              >
                {{ project.title }}
              </NuxtLink>
              <span>:</span>
              <p class="inline">&nbsp;{{ project.overview }}</p>
            </li>
          </ul>
        </div>
        <div
          class="hexagon absolute -top-28 right-1/2 mb-4 flex w-[144px] translate-x-1/2 items-center justify-center bg-hive-dark-yellow sm:-right-12 sm:-top-36 sm:w-[200px] sm:translate-x-0 md:-right-24 md:-top-28 xl:-top-52 xl:w-[280px]"
        >
          <img
            :src="data?.avatar.file"
            :alt="data?.name"
            class="hexagon w-[138px] object-cover sm:w-[192px] xl:w-[264px]"
          />
        </div>
      </div>
      <ul class="sticky top-0 hidden basis-44 pt-28 text-gray-500 sm:block">
        <li>
          <a class="hover:text-gray-700" href="#education">Education</a>
        </li>
        <li>
          <a class="hover:text-gray-700" href="#main-expertise">Main Expertise</a>
        </li>
        <li>
          <a class="hover:text-gray-700" href="#main-role">Main Role</a>
        </li>
        <li>
          <a class="hover:text-gray-700" href="#activities">Activities</a>
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
