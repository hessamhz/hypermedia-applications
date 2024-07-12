<script setup>
import SectionHeader from "~/components/app/SectionHeader.vue";

const route = useRoute();

const { data } = await useApi(`projects/${route.params.slug}/`);

useSeoMeta({
  title: `${data.value.title} | Projects | The Hive`,
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
    <SectionHeader :title="data?.title" backgroundColor="bg-hive-yellow" color="black" linkTo="/our-activities/our-projects"></SectionHeader>
    <div
      class="mx-auto px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28"
    >
      <div class="text-sm italic md:text-base">
        <span class="text-gray-700">Responsible:</span>
        <NuxtLink :to="{ name: 'who-we-are-our-team-slug', params: { slug: data.manager.slug } }">
          <span class="font-semibold underline">{{ data.responsible }}</span>
        </NuxtLink>
      </div>
      <div class="text-sm italic md:text-base">
        <span class="text-gray-700">Started:</span>
        <span class="font-semibold">{{ data.start_date }}</span>
      </div>
      <img
        :src="data.picture.file"
        alt=""
        class="mb-10 mt-7 max-w-full m-auto object-contain rounded-xl shadow-lg xl:rounded-2xl"
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
