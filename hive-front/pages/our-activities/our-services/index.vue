<script setup>
import SectionHeader from "~/components/app/SectionHeader.vue";

const { data } = await useApi('services/');
</script>

<template>
  <div>
    <SectionHeader title="Our Services"></SectionHeader>
    <div
      class="mx-auto max-w-[1240px] px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <ul class="space-y-3 lg:space-y-4 2xl:space-y-5">
        <li
          v-for="service in data"
          :key="service.slug"
          class="flex flex-col gap-1 sm:flex-row sm:even:flex-row-reverse md:gap-3 lg:gap-4 2xl:gap-5 [&>*]:odd:bg-purple-300 [&>*]:even:bg-purple-200"
        >
          <div
            class="service-image-container h-64 shrink-0 rounded-xl sm:aspect-square sm:h-44 md:block lg:h-52 lg:rounded-[20px] xl:h-56"
            :class="!service.picture && 'hidden sm:block'"
          >
            <img
              v-if="service.picture"
              :src="service.picture.file"
              :alt="service.title"
              class=" service-image sm:h-full sm:w-full sm:p-12 rounded-xl object-cover lg:rounded-[20px]"
            />
          </div>
          <NuxtLink
              :to="{ name: 'our-activities-our-services-slug', params: { slug: service.slug } }"
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

<style scoped>
@media (max-width: 639px) {
  .service-image-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 175px;
  }

  .service-image {
    max-width: 50%; /* Adjusts the maximum width to be 80% of its container */
    max-height: 50%; /* Adjusts the maximum height to be 80% of its container */
    object-fit: contain; /* Ensures the image fits within the given dimensions without being cropped */
    margin: auto; /* Centers the image horizontally */
  }
}
</style>
