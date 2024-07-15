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
  rows: {
    type: Number,
    default: 5,
  },
  teaxtareaClass: {
    type: String,
    default: '',
  },
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
