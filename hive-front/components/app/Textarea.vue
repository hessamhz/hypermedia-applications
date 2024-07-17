<script setup>
defineProps({
  label: {
    type: String,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  // Define a prop for the number of rows (or height) in the textarea
  rows: {
    type: Number,
    default: 5,
  },
  // Define a prop for the textarea class,
  // it allows for the passing of custom CSS class names to the textarea element, enabling styling customization.
  teaxtareaClass: {
    type: String,
    default: '',
  },
  // Define a prop for the label class
  // It allows for the passing of custom CSS class names to the label element, enabling styling customization.
  labelClass: {
    type: String,
    default: '',
  },
});

const model = defineModel();
</script>
<template>
  <div class="flex flex-col">
    <label
      :class="`mb-1 pl-1 text-sm font-medium text-hive-purple md:text-base ${labelClass}`"
      :for="name"
    >
      {{ label }}
    </label>
    <textarea
      v-model="model"
      :aria-label="name"
      :name="name"
      :rows="rows"
      :class="`rounded-lg border bg-white p-4 md:rounded-xl ${teaxtareaClass}`"
    ></textarea>
  </div>
</template>
