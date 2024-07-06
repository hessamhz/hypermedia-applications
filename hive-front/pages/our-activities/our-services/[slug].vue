<script setup>
const route = useRoute();

const { data } = await useApi(`services/${route.params.slug}`);

const comments = [
  {
    id: '567d3fbd-e07c-4266-9e00-915be04b8f0d',
    picture: null,
    name: 'Filippo',
    description:
      ' 1 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 11 1 1 1 1 1 1',
    created_at: '2024-06-28T23:39:16.453806Z',
    updated_at: '2024-06-28T23:39:16.453823Z',
  },
  {
    id: '567d3fbd-e07c-4266-9e00-915be04b8f0e',
    picture: null,
    name: 'Filippo 2',
    description: '2 2 2 2 2 22 2 2 2 2 22 2 2 2 2 22 2 2 2 2 22 2 2 2 2 2',
    created_at: '2024-06-28T23:39:16.453806Z',
    updated_at: '2024-06-28T23:39:16.453823Z',
  },
  {
    id: '567d3fbd-e07c-4266-9e00-915be04b8f0f',
    picture: null,
    name: 'Filippo 3',
    description:
      '3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 33 3 3 3 3 3 3 3 33 3 3 3 3 3 3 33 3 3 3 3 3 3 3 3 3 3 3 3 3 ',
    created_at: '2024-06-28T23:39:16.453806Z',
    updated_at: '2024-06-28T23:39:16.453823Z',
  },
  {
    id: '567d3fbd-e07c-4266-9e00-915be04b8f0g',
    picture: null,
    name: 'Filippo 4',
    description:
      '4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 ',
    created_at: '2024-06-28T23:39:16.453806Z',
    updated_at: '2024-06-28T23:39:16.453823Z',
  },
];
</script>

<template>
  <div>
    <header
      class="bg-purple-700 px-5 py-4 font-bold text-white md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <NuxtLink
        to="/our-activities/our-services"
        class="mb-2 flex items-end gap-2 text-lg md:text-xl lg:text-2xl xl:text-3xl"
      >
        <span class="border-b">Our Services</span>
        <IconChevron />
      </NuxtLink>
      <h1 class="text-2xl md:text-3xl lg:text-5xl xl:text-6xl 2xl:text-7xl">
        {{ data?.title }}
      </h1>
    </header>
    <div
      class="mx-auto max-w-[1240px] space-y-3 px-5 py-10 md:px-10 md:py-16 lg:space-y-4 xl:px-24 xl:py-28 2xl:space-y-5"
    >
      <div class="flex md:gap-3 lg:gap-4 2xl:gap-5">
        <div
          class="hidden aspect-square h-44 shrink-0 rounded-xl bg-orange-100 md:block lg:h-52 lg:rounded-[20px] xl:h-56"
        ></div>
        <div
          class="grow rounded-xl bg-purple-100 p-5 md:h-44 md:p-6 lg:h-52 lg:rounded-[20px] lg:p-7 xl:h-56 xl:p-8 2xl:p-9"
        >
          <h2 class="pb-3 text-xl font-semibold lg:text-2xl xl:text-3xl">
            {{ data.title }}
          </h2>
          <h4 class="pb-2 italic text-purple-700 lg:text-lg xl:text-xl">
            {{ data.manager.name }}
          </h4>
          <span class="italic lg:text-lg xl:text-xl">
            {{ data.working_time }}
          </span>
        </div>
      </div>
      <div
        class="rounded-xl bg-orange-100 p-5 md:p-6 lg:rounded-[20px] lg:p-7 xl:p-8 2xl:p-9"
      >
        {{ data.description }}
      </div>
    </div>
    <div class="px-5">
      <h2
        class="mt-10 text-center text-3xl font-bold text-purple-700 md:text-4xl xl:text-5xl 2xl:text-6xl"
      >
        Your Opinion Matters
      </h2>
      <Swiper
        :slides-per-view="1"
        :grab-cursor="true"
        :centered-slides="true"
        :breakpoints="{
          768: {
            slidesPerView: 3,
          },
        }"
        class="mb-20 mt-12 h-full w-full lg:mb-40 lg:mt-16 xl:mt-20 2xl:mt-24"
      >
        <SwiperSlide
          v-for="comment in comments"
          :key="comment.id"
          class="min-h-52 rounded-xl bg-gray-100 p-4 shadow-sm lg:rounded-[20px]"
        >
          <p>{{ comment.description }}</p>
        </SwiperSlide>
      </Swiper>
    </div>
  </div>
</template>

<style scoped>
.swiper-slide-prev,
.swiper-slide-next {
  scale: 0.7;
  opacity: 0.5;
  transition: all 0.3s;
}

.swiper-slide-active {
  scale: 1;
  opacity: 1;
  transition: all 0.3s;
}
</style>
