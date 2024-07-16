<script setup>
// Define a prop for size
const props = defineProps({
  size: {
    type: Number,
    default: 200, // Default size if not provided
  },
  src: {
    type: String,
    required: true,
  },
  alt: {
    type: String,
    default: '',
  },
});

// Use computed property to construct the style object
const wrapperStyle = computed(() => ({
  '--size': `${props.size}px`,
}));
const imageStyle = computed(() => ({
  '--size': `${props.size - 8}px`,
}));
</script>

<template>
  <div
    class="hexagon overflow-hidden"
    :style="wrapperStyle"
  >
    <img
      class="hexagon"
      :style="imageStyle"
      :src="src"
      :alt="alt"
    />
  </div>
</template>

<style scoped>
/* The 'hexagon' class applies the following styles */
.hexagon {
  /* CSS variable for size */
  --f: 15;
  --radius: calc(var(--size) / var(--f));

  /* Width and height settings */
  width: var(--size);
  height: auto;
  aspect-ratio: 1.155;
  object-fit: cover;

  /* CSS variables for gradient and mask settings */
  --cg: #0000, #000 1deg 119deg, #0000 120deg;
  --rad: radial-gradient(farthest-side, #000 99%, #0000 101%);
  --s: calc(2 * var(--radius)) calc(2 * var(--radius));

  /* -webkit-mask settings for creating hexagon shapes */
  -webkit-mask:
    var(--rad) left calc(0.25 * var(--size) - 0.4 * var(--radius)) top 0 /
      var(--s),
    var(--rad) right calc(0.25 * var(--size) - 0.4 * var(--radius)) top 0 /
      var(--s),
    var(--rad) left calc(0.25 * var(--size) - 0.4 * var(--radius)) bottom 0 /
      var(--s),
    var(--rad) right calc(0.25 * var(--size) - 0.4 * var(--radius)) bottom 0 /
      var(--s),
    var(--rad) left calc(0.15 * var(--radius)) top 50% / var(--s),
    var(--rad) right calc(0.15 * var(--radius)) top 50% / var(--s),
    conic-gradient(
        from 30deg at left calc(-0.3 * var(--radius)) top 50%,
        var(--cg)
      )
      left calc(0.3 * var(--radius)) top 50% /50% calc(100% - 0.8 *
          var(--radius)),
    conic-gradient(
        from -150deg at right calc(-0.3 * var(--radius)) top 50%,
        var(--cg)
      )
      right calc(0.3 * var(--radius)) top 50% /50% calc(100% - 0.8 *
          var(--radius)),
    linear-gradient(#000 0 0) center/calc(45% - 1.1 * var(--radius));

    /* Ensure the mask does not repeat */
  -webkit-mask-repeat: no-repeat;
}
</style>
