<script setup>
const route = useRoute();

const { data } = await useApi(`projects/${route.params.slug}`);
</script>

<template>
  <div>
    <header
      class="bg-purple-700 px-5 py-4 font-bold text-white md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <NuxtLink
        to="/our-activities/our-projects"
        class="mb-2 flex items-end gap-2 text-lg md:text-xl lg:text-2xl xl:text-3xl"
      >
        <span class="border-b">Our Projects</span>
        <IconChevron />
      </NuxtLink>
      <h1 class="text-2xl md:text-3xl lg:text-5xl xl:text-6xl 2xl:text-7xl">
        {{ data?.title }}
      </h1>
    </header>
    <div
      class="mx-auto max-w-[1240px] px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <div class="text-sm italic md:text-base">
        <span class="text-gray-700">Responsible:</span>
        <span class="font-semibold">{{ data.responsible }}</span>
      </div>
      <div class="text-sm italic md:text-base">
        <span class="text-gray-700">Started:</span>
        <span class="font-semibold">{{ data.start_date }}</span>
      </div>
      <img
        :src="data.picture.file"
        alt=""
        class="mb-10 mt-7 aspect-[16/9] w-full rounded-xl object-cover shadow-lg xl:rounded-2xl"
      />
      <div
        class="project-detail-content"
        v-html="data.description"
      ></div>
      <div
        class="project-detail-content"
        v-html="data.content"
      ></div>
    </div>
  </div>
</template>

<style>
.project-detail-content h1 {
  font-weight: 700;
  font-size: clamp(24px, 4vw, 36px);
  margin-block: 0.7em;
}
.project-detail-content h2 {
  font-weight: 700;
  font-size: clamp(20px, 4vw, 30px);
  margin-block: 0.7em;
}
.project-detail-content h3 {
  font-weight: 600;
  font-size: clamp(18px, 4vw, 28px);
  margin-block: 0.7em;
}
.project-detail-content h4,
.project-detail-content h5,
.project-detail-content h6 {
  font-weight: 600;
  font-size: clamp(16px, 4vw, 24px);
  margin-block: 0.7em;
}
.project-detail-content p {
  font-size: clamp(14px, 2vw, 20px);
  margin-block: 0.7em;
}
.project-detail-content ul {
  list-style-type: circle;
  list-style-position: inside;
  font-size: clamp(14px, 2vw, 20px);
  margin-block: 0.7em;
}
.project-detail-content img {
  margin-inline: auto;
  margin-block: 14px;
  border-radius: 10px;
  box-shadow:
    0 4px 6px -1px rgb(0 0 0 / 0.1),
    0 2px 4px -2px rgb(0 0 0 / 0.1);
}

@media (width > 1024px) {
  .project-detail-content img {
    border-radius: 12px;
  }
}
</style>
