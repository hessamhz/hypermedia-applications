<script setup>
import SectionHeader from "~/components/app/SectionHeader.vue";

// Define SEO metadata for the page
useSeoMeta({
  title: "The Center | The Hive",
  description: "Learn more about the history of The Hive, Anti-Violence Center for Women.",
  ogTitle: "The Center | The Hive",
  ogType: "website",
  ogUrl: "https://the-hive.space/",
  canonical: "https://the-hive.space/",
  ogSiteName: "The Hive"
});
</script>

<template>
  <div>
    <SectionHeader title="The Center"></SectionHeader>
    <div
      class="mx-auto flex max-w-[1240px] flex-col items-start gap-10 gap-y-10 px-5 py-10 md:flex-row md:items-center md:px-10 md:py-16 xl:gap-11 xl:px-24 xl:py-28 2xl:gap-16"
    >
      <div>
        <h2
          class="mb-4 text-2xl font-bold text-hive-purple lg:mb-7 lg:text-3xl xl:text-4xl"
        >
          Our Story
        </h2>
        <p class="xl:text-lg">
          The Hive was founded by four dedicated individuals who shared a common vision of creating a safe haven
          for women affected by violence. Combining their diverse backgrounds in social work, psychology, and legal advocacy,
          they established the center to offer comprehensive support and resources.
          Their collective passion and commitment have transformed The Hive into a beacon of hope, empowering countless women to
          reclaim their lives and find healing and strength within a supportive community.
        </p>
      </div>
      <img
        src="https://images.pexels.com/photos/3811108/pexels-photo-3811108.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        alt=""
        class="sm:mx-auto sm:max-w-96 rounded-xl drop-shadow-md lg:max-w-md xl:max-w-lg xl:rounded-2xl 2xl:max-w-xl"
      />
    </div>
    <div class="flex flex-col text-center py-12 bg-hive-beige">
      <h2 class="pb-6 text-2xl font-bold text-hive-purple lg:mb-10 lg:text-3xl xl:text-4xl">What we value</h2>
      <div class="px-6 gap-10 md:grid md:grid-cols-3 md:gap-x-32 md:px-32">
        <div class="flex flex-col items-center gap-2 mb-6">
          <svg class="w-20 mb-4 fill-gray-900" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>account-tie-woman</title><path d="M11.94 3C9.75 3.03 8 4.81 8 7C7.94 8.64 7.81 10.47 7.03 11.59C9.71 13.22 12 13 12 13C12 13 14.29 13.22 16.97 11.59C16.12 10.22 15.94 8.54 16 7C16 4.79 14.21 3 12 3H11.94M8.86 13.32C6 13.93 4 15.35 4 17V21H12L9 17H6.5M12 21L13.78 13.81C13.78 13.81 13 14 12 14C11 14 10.22 13.81 10.22 13.81M12 21H20V17C20 15.35 18 13.93 15.14 13.32L17.5 17H15Z" /></svg>
          <h6 class="font-semibold text-xl">Empowerment</h6>
          <p class="text-gray-700"> We believe in equipping women with the knowledge, resources, and confidence
            they need to take control of their lives and futures.</p>
        </div>
        <div class="flex flex-col items-center gap-2">
          <svg class="w-20 mb-4 fill-gray-900" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>mother-heart</title><path d="M12 2C13.66 2 15 3.34 15 5S13.66 8 12 8 9 6.66 9 5 10.34 2 12 2M20 18L18 12.56C17.65 11.57 17.34 10.71 16 10C14.63 9.3 13.63 9 12 9C10.39 9 9.39 9.3 8 10C6.68 10.71 6.37 11.57 6 12.56L4 18C3.77 19.13 6.38 20.44 8.13 21.19C9.34 21.72 10.64 22 12 22C13.38 22 14.67 21.72 15.89 21.19C17.64 20.44 20.25 19.13 20 18M15.42 17.5L12 21L8.58 17.5C8.22 17.12 8 16.61 8 16.05C8 14.92 8.9 14 10 14C10.55 14 11.06 14.23 11.42 14.61L12 15.2L12.58 14.6C12.94 14.23 13.45 14 14 14C15.11 14 16 14.92 16 16.05C16 16.61 15.78 17.13 15.42 17.5Z" /></svg>
          <h6 class="font-semibold text-xl">Compassion</h6>
          <p class="text-gray-700"> Our approach is rooted in empathy and understanding, ensuring that every
            woman feels heard, respected, and supported.</p>
        </div>
        <div class="flex flex-col items-center gap-2">
          <svg class="w-20 mb-4 fill-gray-900" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>crowd</title><path d="M3.69 9.12C3.5 8.93 3.29 8.84 3.04 8.84C2.63 8.84 2.32 9.03 2.12 9.42S1.97 10.18 2.29 10.53C3.47 11.59 4.22 12.34 4.54 12.78C4.95 13.34 5.15 14.16 5.15 15.22C5.15 16.53 5.65 17.5 6.65 18.17C7.21 18.61 7.82 18.94 8.5 19.16L8.5 15.27C8.5 14.33 8.17 13.55 7.54 12.92M16.46 12.97C15.84 13.59 15.5 14.36 15.5 15.27L15.5 19.2C16.46 18.86 17.26 18.33 17.92 17.63C18.57 16.93 18.9 16.16 18.9 15.22C18.9 14.09 19.09 13.28 19.47 12.78C19.56 12.62 19.73 12.42 20 12.17C20.23 11.92 20.47 11.68 20.71 11.46C20.94 11.25 21.17 11.03 21.39 10.81L21.72 10.53C21.91 10.34 22 10.12 22 9.87C22 9.59 21.91 9.34 21.72 9.14C21.53 8.94 21.3 8.84 21 8.84S20.5 8.93 20.31 9.12M12 20C12.69 20 13.36 19.91 14 19.72L14 16.15C14 15.56 13.82 15.1 13.41 14.66C13 14.22 12.53 14 12 14C11.47 14 11 14.2 10.62 14.61C10.22 15 10 15.46 10 16.06L10 19.72C10.64 19.91 11.31 20 12 20M9 8.5C9 9.33 8.33 10 7.5 10S6 9.33 6 8.5 6.67 7 7.5 7 9 7.67 9 8.5M18 8.5C18 9.33 17.33 10 16.5 10C15.67 10 15 9.33 15 8.5S15.67 7 16.5 7C17.33 7 18 7.67 18 8.5M13.5 5.5C13.5 6.33 12.83 7 12 7S10.5 6.33 10.5 5.5 11.17 4 12 4 13.5 4.67 13.5 5.5M13.5 11C13.5 11.83 12.83 12.5 12 12.5S10.5 11.83 10.5 11 11.17 9.5 12 9.5 13.5 10.17 13.5 11Z" /></svg>
          <h6 class="font-semibold text-xl">Community</h6>
          <p class="text-gray-700"> We foster a sense of belonging and solidarity, creating a network of support where
            women can connect, share experiences, and find strength in unity</p>
        </div>
      </div>
    </div>
    <div>
      <div
        class="mx-auto flex max-w-[1240px] flex-col-reverse items-start gap-10 gap-y-10 px-5 py-10 md:flex-row md:items-center md:px-10 md:py-16 xl:gap-11 xl:px-24 xl:py-28 2xl:gap-16"
      >
        <img
          src="https://images.pexels.com/photos/3811082/pexels-photo-3811082.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
          alt=""
          class="sm:mx-auto sm:max-w-96 rounded-xl drop-shadow-md lg:max-w-md xl:max-w-lg xl:rounded-2xl 2xl:max-w-xl"
        />
        <div class="">
          <h2 class="mb-4 text-2xl font-bold text-hive-purple lg:mb-7 lg:text-3xl xl:text-4xl">
            Our Mission
          </h2>
          <p class="xl:text-lg">
            The Hive strives to provide a safe, supportive, and empowering environment for women
            who have experienced mistreatment and violence. We are dedicated to offering comprehensive resources,
            including emotional support, legal assistance, and educational programs, to help women rebuild their lives.
            Our goal is to foster a community where every woman can find strength, healing, and the tools necessary to thrive.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
