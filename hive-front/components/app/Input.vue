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
  type: {
    type: String,
    default: 'text',
  },
  inputClass: {
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
      :class="`mb-1 pl-1 text-sm font-medium text-purple-700 md:text-base ${labelClass}`"
      :for="name"
    >
      {{ label }}
    </label>
    <input
      v-model="model"
      :type="type"
      :name="name"
      :class="`h-10 rounded-lg border bg-white px-4 md:rounded-xl ${inputClass}`"
    />
  </div>
</template>
