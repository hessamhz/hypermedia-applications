<script setup>
const { data } = await useApi('members/');
</script>

<template>
  <div>
    <header
      class="bg-gradient-to-r from-purple-700 to-orange-300 px-5 py-8 md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <h1
        class="text-3xl font-bold text-white md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl"
      >
        Our Team
      </h1>
    </header>
    <div class="px-5 py-10 md:px-10 md:py-16 xl:px-24 xl:py-28">
      <ul
        class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-10 md:gap-x-16 md:gap-y-12 lg:gap-x-20 xl:gap-x-24"
      >
        <li
          v-for="person in data"
          :key="person.slug"
          class="mx-auto md:mx-0"
        >
          <NuxtLink
              :to="{ name: 'who-we-are-our-team-slug', params: { slug: person.slug } }"
              class="flex flex-col items-center"
          >
            <div
              class="hexagon mb-4 flex w-[144px] items-center justify-center bg-orange-300 sm:w-[180px] xl:w-[200px]"
            >
              <img
                :src="person?.avatar.file"
                :alt="person?.name"
                class="hexagon w-[138px] object-cover sm:w-[172px] xl:w-[192px]"
              />
            </div>
            <h2 class="mb-px text-center max-w-[18ch] font-bold xl:text-lg">{{ person.name }}</h2>
            <h3 class="font-medium text-purple-700 text-center max-w-[24ch] xl:text-lg">
              {{ person.role }}
            </h3>
          </NuxtLink>
        </li>
      </ul>
      <p class="text-center text-sm text-gray-600 pt-16">
        All suggested names and pictures are either fictional or taken from <a href="https://www.pexels.com">https://www.pexels.com</a>.
      </p>
      <p class="text-center text-sm text-gray-600">
        This website is a project created for educational purposes.
      </p>
    </div>
  </div>
</template>
