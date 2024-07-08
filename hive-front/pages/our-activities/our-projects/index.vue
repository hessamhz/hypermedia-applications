<script setup>
const { data } = await useApi('projects/');
</script>

<template>
  <div>
    <header
      class="bg-gradient-to-r from-purple-700 to-orange-300 px-5 py-8 md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <h1
        class="text-3xl font-bold text-white md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl"
      >
        Our Projects
      </h1>
    </header>
    <div
      class="mx-auto max-w-[1240px] px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <ul class="grid gap-3 sm:grid-cols-2 lg:gap-4 2xl:gap-5">
        <li
          v-for="project in data"
          :key="project.slug"
          class="sm:[&:nth-child(7n+1)>a>div]:ml-auto sm:[&:nth-child(7n+1)>a>div]:w-1/2 sm:[&:nth-child(7n+1)>a>div]:text-right sm:[&:nth-child(7n+1)]:col-span-2 sm:[&:nth-child(7n+2)>a>div]:mx-auto sm:[&:nth-child(7n+2)>a>div]:w-4/5 sm:[&:nth-child(7n+2)>a>div]:text-center sm:[&:nth-child(7n+3)>a>div]:mx-auto sm:[&:nth-child(7n+3)>a>div]:w-4/5 sm:[&:nth-child(7n+3)>a>div]:text-center sm:[&:nth-child(7n+4)>a>div]:w-1/2 sm:[&:nth-child(7n+4)]:col-span-2 sm:[&:nth-child(7n+5)>a>div]:w-1/2 sm:[&:nth-child(7n+5)]:col-span-2 sm:[&:nth-child(7n+6)>a>div]:mx-auto sm:[&:nth-child(7n+6)>a>div]:w-4/5 sm:[&:nth-child(7n+6)>a>div]:text-center sm:[&:nth-child(7n+7)>a>div]:mx-auto sm:[&:nth-child(7n+7)>a>div]:w-4/5 sm:[&:nth-child(7n+7)>a>div]:text-center"
        >
          <NuxtLink
              :to="{ name: 'our-activities-our-projects-slug', params: { slug: project.slug } }"
              class="block h-full w-full rounded-xl bg-cover bg-center bg-no-repeat px-5 py-8 text-white shadow-[inset_0_0_0_2000px_rgba(1,1,1,0.5)] sm:px-6 sm:py-10 md:px-9 md:py-14 lg:rounded-[20px] lg:px-10 lg:py-16 xl:px-11 2xl:px-12 2xl:py-20"
              :style="{ backgroundImage: `url(${project.picture.file})` }"
          >
            <div class="">
              <h2
                class="pb-4 text-xl font-bold md:pb-6 md:text-2xl lg:pb-8 lg:text-3xl"
              >
                {{ project.title }}
              </h2>
              <p class="line-clamp-4 md:text-lg lg:text-xl">
                {{ project.overview }}
              </p>
            </div>
          </NuxtLink>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
/* li:nth-child(7n+1),
li:nth-child(7n+4),
li:nth-child(7n+5) {
  grid-column: span 2;
}

li:nth-child(7n+1),
li:nth-child(7n+4),
li:nth-child(7n+5) {
  grid-column: span 2;
} */
</style>
