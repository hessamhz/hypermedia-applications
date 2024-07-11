<script setup>
const isMobileMenuOpen = ref(false);
</script>

<template>
  <header
    class="app-header sticky top-0 z-[99] bg-white w-full drop-shadow-md sm:py-4! flex items-center justify-between px-5 py-5 sm:px-8 md:px-12 lg:px-20"
  >
    <nav class="flex w-full items-center justify-between">
      <NuxtLink
        to="/"
        exact
      >
        <img
          class="w-28 lg:w-32 xl:w-40"
          src="/logo.svg"
        />
      </NuxtLink>
      <ul
        class="hidden gap-2 font-semibold md:flex md:gap-7 lg:gap-10 lg:text-md xl:gap-12 xl:text-lg 2xl:gap-16 2xl:text-xl"
      >
        <li class="relative cursor-pointer [&>nav]:hover:block">
          <NuxtLink
            to="/who-we-are"
            class="pointer-events-none p-2"
          >
            Who Are We
          </NuxtLink>
          <nav class="absolute left-0 top-6 z-20 hidden pt-3 lg:top-7 lg:pt-5">
            <ul
              class="w-max space-y-1 rounded-md border bg-white px-4 py-3 text-sm shadow-sm lg:px-5 lg:py-4 lg:text-base xl:px-6 xl:py-5 xl:text-lg 2xl:text-xl"
            >
              <li>
                <NuxtLink
                  to="/who-we-are/our-team"
                  class="inline-block w-full rounded-lg px-3 py-2 hover:bg-hive-grey"
                >
                  Our Team
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/who-we-are/about"
                  class="inline-block w-full rounded-lg px-3 py-2 hover:bg-hive-grey"
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
            class="pointer-events-none p-2"
          >
            Our Activities
          </NuxtLink>
          <nav class="absolute left-0 top-6 z-20 hidden pt-3 lg:top-7 lg:pt-5">
            <ul
              class="w-max space-y-1 rounded-md border bg-white px-4 py-3 text-sm shadow-sm lg:px-5 lg:py-4 lg:text-base xl:px-6 xl:py-5 xl:text-lg 2xl:text-xl"
            >
              <li>
                <NuxtLink
                  to="/our-activities/our-services"
                  class="inline-block w-full rounded-lg px-3 py-2 hover:bg-hive-grey"
                >
                  Our Services
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/our-activities/our-projects"
                  class="inline-block w-full rounded-lg px-3 py-2 hover:bg-hive-grey"
                >
                  Our Projects
                </NuxtLink>
              </li>
            </ul>
          </nav>
        </li>
        <li>
          <NuxtLink
            to="/contacts"
            class="rounded-xl p-2 hover:bg-hive-grey"
          >
            Contacts
          </NuxtLink>
        </li>
        <li>
          <NuxtLink
            to="/chat"
            class="rounded-lg px-6 bg-hive-yellow py-2 hover:bg-hive-dark-yellow"
          >
            Chat with Bee
          </NuxtLink>
        </li>
      </ul>
    </nav>
    <button
      class="md:hidden"
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
.app-header ul .router-link-active {
  position: relative;
}
.app-header ul .router-link-active::before {
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
