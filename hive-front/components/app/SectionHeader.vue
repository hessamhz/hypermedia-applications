<template>
  <!-- SectionHeader displays the title of the current page and optional breadcrumbs if within a 'slug' page -->
  <header
    :class="`${backgroundColor} text-${color} px-5 py-4 font-bold md:px-14 md:py-10 xl:px-20 xl:py-14`"
  >
    <!-- Conditional NuxtLink for navigation if 'linkTo' is provided -->
    <NuxtLink
      :to="linkTo"
      class="mb-2 flex items-center gap-2 text-lg md:text-xl lg:text-2xl xl:text-3xl"
      v-if="!isLinkEmpty"
    >
      <span
        class="hover:opacity-40 hover:duration-150 hover:ease-in-out"
        :class="`border-b border-${color} `"
        v-if="!isLinkEmpty"
      >
        {{ formattedLinkTitle }}
      </span>
      <IconChevron class="w-6 md:w-7 lg:w-8 xl:w-9" />
    </NuxtLink>

    <h1
      :class="`text-3xl font-bold md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl`"
    >
      {{ title }}
    </h1>

    <slot></slot>
    <!-- Allows for dynamic content inside the header -->
  </header>
</template>

<script>
export default {
  name: 'SectionHeader',
  props: {
    // 'linkTo' specifies the navigation target URL. If provided, a clickable link is rendered.
    linkTo: {
      type: String,
      required: false,
      default: '',
    },
    // 'backgroundColor' specifies Tailwind CSS properties for the appearance of the header.
    backgroundColor: {
      type: String,
      required: false,
      default: 'bg-gradient-to-r from-hive-purple to-hive-yellow',
    },
    // 'color' specifies the color text and other elements of the header.
    // It should just contain the name of the color, which is going to be attached to the Tailwind CSS text- and border- prefixes.
    color: {
      type: String,
      required: false,
      default: 'white',
    },
    // 'title' specifies the title of the header.
    title: {
      type: String,
      required: true,
    },
  },
  computed: {
    // Computed property to check if linkTo is empty
    isLinkEmpty() {
      return this.linkTo.trim() === '';
    },
    // Computed property to extract the title of the previous page from the linkTo property
    formattedLinkTitle() {
      if (this.isLinkEmpty) return '';

      const lastSlashIndex = this.linkTo.lastIndexOf('/');
      const rawTitle = this.linkTo.substring(lastSlashIndex + 1); // Extract the title from the linkTo property starting from the position next to the last slash
      return rawTitle
        .split('-') // Links contain the '-' character, which we need to remove
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1)) // Capitalize the first letter of each word
        .join(' '); // Join the words back together
    },
  },
};
</script>
