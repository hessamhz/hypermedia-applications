<script setup>
import SectionHeader from "~/components/app/SectionHeader.vue";

const route = useRoute();

const { data } = await useApi(`services/${route.params.slug}/`);

useSeoMeta({
  title: `${data.value.title} | Services | The Hive`,
  description: `"${data.value.description}" at The Hive`,
  ogTitle: "Our Projects | The Hive",
  ogType: "website",
  ogUrl: "https://the-hive.space/",
  canonical: "https://the-hive.space/",
  ogSiteName: "The Hive"
});
</script>

<template>
  <div>
    <SectionHeader
      :title="data?.title"
      background-color="bg-hive-purple"
      color="white"
      linkTo="/our-activities/our-services"
    ></SectionHeader>
    <div
      class="mx-auto max-w-[1240px] space-y-3 px-5 py-10 md:px-10 md:py-16 lg:space-y-4 xl:px-24 xl:py-28 2xl:space-y-5"
    >
      <div class="flex md:gap-3 lg:gap-4 2xl:gap-5">
        <div
          class="hidden aspect-square h-44 shrink-0 rounded-xl bg-purple-200 md:block lg:h-52 lg:rounded-[20px] xl:h-56"
        >
          <img
            v-if="data.picture"
            :src="data.picture.file"
            :alt="data.title"
            class="h-full w-full p-16 rounded-xl object-cover lg:rounded-[20px]"
          />
        </div>
        <div
          class="grow rounded-xl bg-purple-100 p-5 md:h-44 md:p-6 lg:h-52 lg:rounded-[20px] lg:p-7 xl:h-56 xl:p-8 2xl:p-9"
        >
          <h2 class="pb-3 text-xl font-semibold lg:text-2xl xl:text-3xl">
            {{ data.title }}
          </h2>
          <h4
            v-if="data.manager"
            class="pb-2 italic text-purple-700 lg:text-lg xl:text-xl"
          >
            <!-- {{ data.manager.name }} -->
            <NuxtLink
              :to="{
                name: 'who-we-are-our-team-slug',
                params: { slug: data.manager.slug },
              }"
            >
              {{ data.manager.name }}
            </NuxtLink>
          </h4>
          <span class="italic lg:text-lg xl:text-xl">
            {{ data.working_time }}
          </span>
        </div>
      </div>
      <div
        class="rounded-xl bg-purple-200 p-5 md:p-6 lg:rounded-[20px] lg:p-7 xl:p-8 2xl:p-9"
      >
        {{ data.description }}
      </div>
    </div>
    <div v-if="data.comments.length > 0" class="px-5">
      <h2
        class="mt-10 text-center text-3xl font-bold text-hive-purple md:text-4xl xl:text-5xl 2xl:text-6xl"
      >
        Your Opinion Matters
      </h2>
      <Swiper
        :modules="[SwiperAutoplay]"
        :autoplay="{
          delay: 2000,
          disableOnInteraction: false,
        }"
        :speed="2000"
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
          v-for="comment in data.comments"
          :key="comment.id"
          class="!flex min-h-52 items-center justify-center rounded-xl bg-gray-100 p-4 shadow-sm lg:rounded-[20px] xl:text-lg 2xl:text-xl"
        >

          <div
            class="flex-col items-start flex gap-2 text-sm px-3 text-gray-500"
          >
            <div class="flex flox-row items-center mb-2">
              <img
                v-if="comment.picture"
                :src="comment.picture.file"
                class="aspect-square w-10 rounded-full mr-4"
              />
              <span>{{ comment.name }}</span>
            </div>
            <p class="text-black">{{ comment.description }}</p>
          </div>
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
