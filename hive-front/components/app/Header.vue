<script setup>
const isMobileMenuOpen = ref(false);
</script>

<template>
  <header
    class="app-header flex items-center justify-between px-5 py-6 sm:px-8 sm:py-5 md:px-12 lg:px-20"
  >
    <div class="flex">
      <img
        class="w-28 lg:w-32 xl:w-44"
        src="/logo.svg"
      />
    </div>
    <nav class="hidden sm:flex">
      <ul
        class="flex gap-7 font-semibold md:gap-14 lg:gap-24 lg:text-lg xl:text-xl 2xl:text-2xl"
      >
        <li>
          <NuxtLink
            to="/"
            exact
          >
            Home
          </NuxtLink>
        </li>
        <li class="relative cursor-pointer [&>nav]:hover:block">
          <NuxtLink
            to="/who-we-are"
            class="pointer-events-none"
          >
            Who We Are
          </NuxtLink>
          <nav class="absolute left-0 top-6 z-10 hidden pt-3 lg:top-7 lg:pt-5">
            <ul
              class="w-max space-y-3 rounded-md border bg-white px-6 py-3 text-sm shadow-sm lg:px-7 lg:py-4 lg:text-base xl:px-8 xl:py-5 xl:text-lg 2xl:text-xl"
            >
              <li>
                <NuxtLink
                  to="/who-we-are/our-team"
                  class="inline-block w-full"
                >
                  Our Team
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/who-we-are/about"
                  class="inline-block w-full"
                >
                  About
                </NuxtLink>
              </li>
            </ul>
          </nav>
        </li>
        <li class="relative cursor-pointer [&>nav]:hover:block">
          <NuxtLink
            to="/our-activities"
            class="pointer-events-none"
          >
            Our Activities
          </NuxtLink>
          <nav class="absolute left-0 top-6 z-10 hidden pt-3 lg:top-7 lg:pt-5">
            <ul
              class="w-max space-y-3 rounded-md border bg-white px-6 py-3 text-sm shadow-sm lg:px-7 lg:py-4 lg:text-base xl:px-8 xl:py-5 xl:text-lg 2xl:text-xl"
            >
              <li>
                <NuxtLink
                  to="/our-activities/our-services"
                  class="inline-block w-full"
                >
                  Our Services
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/our-activities/our-projects"
                  class="inline-block w-full"
                >
                  Our Projects
                </NuxtLink>
              </li>
            </ul>
          </nav>
        </li>

        <li>
          <NuxtLink to="/contacts">Contacts</NuxtLink>
        </li>
      </ul>
    </nav>
    <button
      class="sm:hidden"
      @click="isMobileMenuOpen = true"
    >
      <IconMenu />
    </button>
  </header>
  <AppMobileMenu
    :is-open="isMobileMenuOpen"
    @close="isMobileMenuOpen = false"
  />
</template>

<style scoped>
.app-header .router-link-active {
  position: relative;
}
.app-header .router-link-active::before {
  position: absolute;
  content: '';
  background-color: theme('colors.purple.600');
  bottom: -12px;
  left: 0;
  right: 0;
  width: 100%;
  height: 4px;
}

.app-header nav nav .router-link-active::before {
  bottom: -2px;
  height: 2px;
}
</style>
