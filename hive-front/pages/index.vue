<script setup></script>

<template>
  <div>
    <!-- HERO -->
    <div
      class="relative flex flex-col gap-12 px-5 py-10 md:py-16 xl:flex-row xl:justify-end xl:px-0"
    >
      <div
        class="z-0 text-center xl:absolute xl:left-20 xl:top-1/3 xl:text-left"
      >
        <h1 class="mb-4 text-5xl font-bold md:text-7xl">Title title title</h1>
        <h3 class="mb-10 text-3xl font-semibold md:mb-14 md:text-4xl xl:mb-16">
          Subtitle subtitle subtitle
        </h3>
        <NuxtLink
          class="rounded-lg bg-purple-700 px-7 py-3 text-white md:text-xl xl:rounded-2xl xl:px-10 xl:py-4"
          to="/contacts"
        >
          Contact us
        </NuxtLink>
      </div>
      <img
        src="~/assets/images/landing-hero-img.png"
        alt="Hero Image"
        class="z-0 mx-auto w-full max-w-3xl xl:mx-0 xl:w-2/3 xl:max-w-none 2xl:w-9/12 2xl:max-w-6xl"
      />
    </div>
    <!-- OUR CENTER -->
    <div
      class="flex flex-col items-center bg-red-200 bg-opacity-20 bg-[linear-gradient(to_right,rgba(126,34,206,0.7),rgba(253,186,116,0.7)),url('https://fastly.picsum.photos/id/107/1200/800.jpg?hmac=dKPtzgSuX7AN26ivr2Crjeix70xYFn8k38d17j0mcp8')] bg-cover bg-center bg-no-repeat px-5 py-10 text-center text-white md:px-10 md:py-16 xl:px-20 xl:py-20"
    >
      <h2 class="mb-6 text-4xl font-bold md:mb-11 md:text-5xl">Our Center</h2>
      <p class="mb-8 max-w-3xl xl:mb-12 xl:text-lg">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eveniet quam
        exercitationem enim nihil sed itaque sunt porro iste totam veritatis
        deserunt tempora necessitatibus eum, ab possimus placeat ullam similique
        modi quisquam, consequatur omnis dolore dignissimos. Error dolor
        provident tempora repellendus.
      </p>
      <NuxtLink
        to="/who-we-are/about"
        class="max-w-64 rounded-full bg-white px-8 py-3 text-black md:text-lg lg:text-xl xl:max-w-80"
      >
        Discover The Hive
      </NuxtLink>
    </div>
    <!-- COUNTERS -->
    <div class="bg-gray-100 px-5 py-16">
      <ul
        class="mx-auto flex max-w-4xl flex-col items-center gap-7 sm:flex-row sm:justify-center sm:gap-0 xl:max-w-5xl"
      >
        <li
          class="py-4 text-center sm:border-r sm:border-gray-300 sm:pr-6 md:pr-11 lg:pr-14"
        >
          <div
            class="mb-2 text-5xl font-bold text-purple-700 lg:mb-5 lg:text-6xl xl:mb-6 xl:text-7xl"
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
            class="mb-2 text-5xl font-bold text-purple-700 lg:mb-5 lg:text-6xl xl:mb-6 xl:text-7xl"
          >
            20300+
          </div>
          <div class="text-lg font-semibold lg:text-xl xl:text-2xl">
            Women assisted
          </div>
        </li>
        <li class="py-4 text-center sm:pl-6 md:pl-11 lg:pl-14">
          <div
            class="mb-2 text-5xl font-bold text-purple-700 lg:mb-5 lg:text-6xl xl:mb-6 xl:text-7xl"
          >
            20K
          </div>
          <div class="text-lg font-semibold lg:text-xl xl:text-2xl">
            Donations
          </div>
        </li>
      </ul>
    </div>
    <!-- WHO WE ARE -->
    <div class="px-5 py-10 text-center md:px-10 md:py-16 xl:px-20 xl:py-20">
      <h2 class="mb-6 text-4xl font-bold text-purple-700 md:mb-11 md:text-5xl">
        Who we are
      </h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae quae
        voluptates consequatur libero fugit animi at. Quae ipsa aspernatur
        molestias natus distinctio quia illo soluta reiciendis adipisci iste,
        debitis doloribus voluptatibus nisi nulla officia quas iure? Quas
        praesentium quasi error repudiandae, similique laboriosam expedita
        voluptate velit, itaque repellat dolorum eius.
      </p>
    </div>
    <!-- OUR ACTIVITIES -->
    <div class="bg-gray-100 px-5 py-10 md:px-10 md:py-16 xl:px-20 xl:py-20">
      <h2 class="mb-9 text-center text-4xl font-bold md:mb-11 md:text-5xl">
        Our Activities
      </h2>
      <div class="mx-auto flex max-w-3xl flex-col gap-10 sm:flex-row sm:gap-5">
        <div
          class="flex flex-col items-start rounded-lg bg-purple-300 p-5 sm:basis-full md:p-7"
        >
          <h3 class="mb-4 text-2xl font-bold md:mb-6 md:text-3xl">Projects</h3>
          <p class="mb-10">
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor,
            veritatis molestiae! Est, eligendi eaque? Consectetur molestias quod
            similique doloribus iusto?
          </p>
          <NuxtLink
            to="/our-activities/our-projects"
            class="mt-auto rounded-full bg-white px-5 py-2"
          >
            Read More
          </NuxtLink>
        </div>
        <div
          class="flex flex-col items-start rounded-lg bg-orange-300 p-5 sm:basis-full md:p-7"
        >
          <h3 class="mb-4 text-2xl font-bold md:mb-6 md:text-3xl">Services</h3>
          <p class="mb-10">
            Lorem ipsum, dolor sit amet orem ipsum, dolor sit amet orem ipsum,
            dolor sit amet orem ipsum, dolor sit amet consectetur adipisicing
            elit. Dolor, veritatis molestiae! Est, eligendi eaque? Consectetur
            molestias quod similique doloribus iusto?
          </p>
          <NuxtLink
            to="/our-activities/our-services"
            class="mt-auto rounded-full bg-white px-5 py-2"
          >
            Read More
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>
