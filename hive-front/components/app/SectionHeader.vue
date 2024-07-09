<template>
  <header :class="`${backgroundColor} text-${color} px-5 py-4 font-bold md:px-14 md:py-10 xl:px-20 xl:py-14`">
    <NuxtLink
        :to=linkTo
        class="mb-2 flex items-center gap-2 text-lg md:text-xl lg:text-2xl xl:text-3xl ${textColor}"
        v-if="!isLinkEmpty"
    >
      <span :class="`border-b border-${color} text-${color}`" v-if="!isLinkEmpty">{{ formattedLinkTitle }}</span>
      <IconChevron class="w-6 md:w-7 lg:w-8 xl:w-9" />
    </NuxtLink>

    <h1 :class="`text-3xl font-bold md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl`">
      {{ title }}
    </h1>

    <slot></slot> <!-- Allows for dynamic content inside the header -->
  </header>
</template>

<script>
export default {
  name: 'SectionHeader',
  props: {
    linkTo: {
      type: String,
      required: false,
      default: ''
    },
    backgroundColor: {
      type: String,
      required: false,
      default: 'bg-gradient-to-r from-purple-700 to-yellow-400'
    },
    color: {
      type: String,
      required: false,
      default: 'white'
    },
    title: {
      type: String,
      required: true,
    }
  },
  computed: {
    // Computed property to check if linkTo is empty
    isLinkEmpty() {
      return this.linkTo.trim() === '';
    },
    formattedLinkTitle() {
      if (this.isLinkEmpty) return '';

      const lastSlashIndex = this.linkTo.lastIndexOf('/');
      const rawTitle = this.linkTo.substring(lastSlashIndex + 1);
      return rawTitle
          .split('-')
          .map(word => word.charAt(0).toUpperCase() + word.slice(1))
          .join(' ');
    },
  },
}
</script>
