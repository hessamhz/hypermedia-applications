<script setup lang="js">
import { shuffleArray } from '~/utils/shuffleArray.js';

const data = await useApi('/members/avatars').data.value;

let hexagon = [];

if (Array.isArray(data)) {
  const avatars = data.map((item) => item.avatar.file);
  shuffleArray(avatars);

  const MAX_HEXAGONS_PER_ROW = 7;
  hexagon = [];
  let currentRow = [];

  avatars.forEach((avatar) => {
    if (currentRow.length < MAX_HEXAGONS_PER_ROW) {
      currentRow.push(avatar);
    } else {
      hexagon.push(currentRow);
      currentRow = [avatar];
    }
  });

  //if there are any remaining hexagons
  if (currentRow.length > 0) {
    // Fill the rest of the row with previous images if needed
    while (currentRow.length < MAX_HEXAGONS_PER_ROW) {
      const randomIndex = Math.floor(Math.random() * avatars.length);
      currentRow.push(avatars[randomIndex]);
    }
    hexagon.push(currentRow);
  }
}

function hexagonColumnClass(i) {
  let classes = '';
  if (i > 0) classes += ' -mt-[20px] md:-mt-[30px] xl:-mt-[40px] ';
  if (i % 2 === 0) classes += ' pl-[45px] md:pl-[67px] xl:pl-[87px] ';
  return classes;
}

// Define SEO metadata for the page
useSeoMeta({
  title: 'Main Page | The Hive',
  description: 'The home page of The Hive Anti-Violence Center for Women.',
  ogTitle: 'Main Page | The Hive',
  ogType: 'website',
  ogUrl: 'https://the-hive.space/',
  canonical: 'https://the-hive.space/',
  ogSiteName: 'The Hive',
});
</script>

<template>
  <div>
    <!-- HERO -->
    <div
      class="flex flex-col items-center justify-center gap-12 xl:flex-col xl:items-start xl:justify-center"
    >
      <div class="absolute z-10 text-center xl:pb-5 xl:pl-20 xl:text-left">
        <h1 class="mb-4 text-5xl font-bold text-white md:text-7xl">
          Violence can be
          <span
            class="blur-sm duration-300 ease-in hover:blur-0 hover:duration-500 hover:ease-in-out"
          >
            invisible
          </span>
        </h1>
        <h1 class="mb-10 text-5xl font-bold text-white md:text-7xl">
          You are not
        </h1>
        <NuxtLink
          class="rounded-lg border-white bg-white px-7 py-3 font-medium hover:bg-hive-grey hover:duration-150 hover:ease-in md:text-xl xl:rounded-2xl xl:px-10 xl:py-4"
          to="/contacts"
        >
          Talk to us
        </NuxtLink>
      </div>
      <div>
        <img
          src="~/assets/images/heronew.png"
          alt="Hero Image"
          class="h-[36rem] object-cover object-[left_calc(30%)_top_calc(0%)] sm:object-left md:h-[48rem] md:w-[120rem] xl:w-[200rem] 2xl:w-[250rem]"
        />
      </div>
    </div>

    <!-- OUR CENTER -->
    <div class="flex flex-col items-center justify-center py-20 text-center">
      <h2 class="mb-6 text-4xl font-bold text-hive-purple md:mb-11 md:text-5xl">
        Our Center
      </h2>
      <p class="mb-8 max-w-3xl xl:mb-12 xl:text-lg">
        The Hive was founded by four dedicated individuals who shared a common
        vision of creating a safe haven for women affected by violence, abuse or
        discrimination. We strive to provide a safe, supportive, and empowering
        environment for them to share their experience.
      </p>
      <NuxtLink
        to="/who-we-are/about"
        class="max-w-64 rounded-lg bg-hive-purple px-8 py-3 text-white hover:bg-hive-dark-purple hover:duration-150 hover:ease-in md:text-lg lg:text-xl xl:max-w-80"
      >
        Discover The Hive
      </NuxtLink>
    </div>
    <!-- COUNTERS -->
    <div class="bg-hive-beige px-5 py-16">
      <ul
        class="mx-auto flex max-w-4xl flex-col items-center gap-7 sm:flex-row sm:justify-center sm:gap-0 xl:max-w-5xl"
      >
        <li
          class="py-4 text-center sm:border-r sm:border-gray-300 sm:pr-6 md:pr-11 lg:pr-14"
        >
          <div
            class="mb-2 text-5xl font-bold text-hive-purple lg:mb-5 lg:text-6xl xl:mb-6 xl:text-7xl"
          >
            20
          </div>
          <div class="text-lg font-semibold lg:text-xl xl:text-2xl">
            Active Volunteers
          </div>
        </li>
        <li
          class="py-4 text-center sm:border-r sm:border-gray-300 sm:px-6 md:px-11 lg:px-14"
        >
          <div
            class="mb-2 text-5xl font-bold text-hive-purple lg:mb-5 lg:text-6xl xl:mb-6 xl:text-7xl"
          >
            2300+
          </div>
          <div class="text-lg font-semibold lg:text-xl xl:text-2xl">
            Women assisted
          </div>
        </li>
        <li class="py-4 text-center sm:pl-6 md:pl-11 lg:pl-14">
          <div
            class="mb-2 text-5xl font-bold text-hive-purple lg:mb-5 lg:text-6xl xl:mb-6 xl:text-7xl"
          >
            20K
          </div>
          <div class="text-lg font-semibold lg:text-xl xl:text-2xl">
            Donations
          </div>
        </li>
      </ul>
    </div>
    <!-- RISK ASSESSMENT BOT -->
    <div
      class="flex flex-col items-center bg-red-200 bg-opacity-20 bg-[url('~/assets/images/ourcenter.png')] bg-cover bg-fixed bg-center bg-no-repeat px-5 py-10 text-center text-white md:px-10 md:py-16 xl:px-20 xl:py-20"
    >
      <h2 class="mb-6 text-4xl font-bold md:mb-11 md:text-5xl">
        Risk Assessment
      </h2>
      <p class="mb-8 max-w-3xl xl:mb-12 xl:text-lg">
        We have developed Bee, our virtual assistant capable of providing a live
        risk assessment of a dangerous situation you or someone you know might
        be going through. Bee will ask some questions to better understand the
        severity of the case and tailor a response with suggestions about the
        most important emergency contacts or services that can be of help.
      </p>
      <NuxtLink
        to="/chat"
        class="max-w-64 rounded-lg bg-white px-8 py-3 text-black hover:bg-gray-200 hover:duration-150 hover:ease-in md:text-lg lg:text-xl xl:max-w-80"
      >
        Chat with Bee
      </NuxtLink>
    </div>

    <!-- WHO WE ARE -->
    <div class="py-10 text-center md:py-16 xl:py-20">
      <h2 class="mb-6 text-4xl font-bold text-hive-purple md:mb-11 md:text-5xl">
        Who are we
      </h2>
      <div class="overflow-x-clip">
        <div class="m-auto flex w-fit flex-col">
          <div
            v-for="(row, rowIndex) in hexagon"
            :key="rowIndex"
            class="flex gap-[7px] md:gap-[8px] xl:gap-[7px]"
            :class="hexagonColumnClass(rowIndex)"
          >
            <template
              v-for="(hexagon, hexagonIndex) in row"
              :key="hexagonIndex + 1000"
            >
              <img
                v-if="hexagon !== 'EMPTY'"
                :src="hexagon"
                alt="Member profile picture"
                class="hexagon h-24 object-cover md:h-36 xl:h-48"
                :class="!hexagon && 'invisible'"
              />
              <div
                v-else
                class="hexagon h-24 bg-gray-100 md:h-36 xl:h-48"
              ></div>
            </template>
          </div>
        </div>
      </div>
      <div class="pt-14">
        <NuxtLink
          class="rounded-lg bg-hive-purple px-7 py-3 text-white hover:bg-hive-dark-purple md:text-xl xl:rounded-2xl xl:px-10 xl:py-4"
          to="/who-we-are/our-team"
        >
          Meet the Team
        </NuxtLink>
      </div>
    </div>
    <!-- OUR ACTIVITIES -->
    <div class="bg-hive-beige px-5 py-10 md:px-10 md:py-16 xl:px-20 xl:py-20">
      <h2 class="mb-9 text-center text-4xl font-bold md:mb-11 md:text-5xl">
        Our Activities
      </h2>
      <div class="mx-auto flex max-w-3xl flex-col gap-10 sm:flex-row sm:gap-5">
        <div
          class="flex flex-col items-start rounded-lg bg-hive-purple p-5 text-white sm:basis-full md:p-7"
        >
          <h3 class="mb-4 text-2xl font-bold md:mb-6 md:text-3xl">Services</h3>
          <p class="mb-10">
            Our team of highly specialized people is responsible for the
            organization of many services to help women through difficult times.
          </p>
          <NuxtLink
            to="/our-activities/our-services"
            class="mt-auto rounded-lg bg-white px-5 py-2 text-black hover:bg-gray-200 hover:duration-150 hover:ease-in"
          >
            Read More
          </NuxtLink>
        </div>
        <div
          class="flex flex-col items-start rounded-lg bg-hive-yellow p-5 font-medium text-hive-black sm:basis-full md:p-7"
        >
          <h3 class="mb-4 text-2xl font-bold md:mb-6 md:text-3xl">Projects</h3>
          <p class="mb-10">
            We collaborate with local and international institutions with the
            goal of providing education and information about issues and
            struggles that women face in their life.
          </p>
          <NuxtLink
            to="/our-activities/our-projects"
            class="mt-auto rounded-lg bg-white px-5 py-2 hover:bg-hive-grey hover:duration-150 hover:ease-in"
          >
            Read More
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>
