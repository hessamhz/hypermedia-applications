<script setup>
const form = ref({
  name: '',
  email: '',
  message: '',
});

const config = useRuntimeConfig();

async function submit() {
  const response = await $fetch(`${config.public.baseURL}/contact-us/`, {
    method: 'POST',
    body: form.value,
  });
  // if successful, empty the form fields
  if (response.id) {
    form.value = {
      name: '',
      email: '',
      message: '',
    };
  }
}
</script>

<template>
  <div>
    <header
      class="bg-gradient-to-r from-purple-700 to-orange-300 px-5 py-8 md:px-14 md:py-10 xl:px-20 xl:py-14"
    >
      <h1
        class="text-3xl font-bold text-white md:text-4xl lg:text-5xl xl:text-6xl 2xl:text-7xl"
      >
        Contact
      </h1>
    </header>
    <div
      class="mx-auto max-w-[1240px] items-start gap-10 px-5 py-10 md:px-10 md:py-16 lg:flex xl:gap-11 xl:px-24 xl:py-28 2xl:gap-12"
    >
      <p class="mb-10 lg:basis-5/12 xl:text-lg 2xl:text-xl">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus,
        architecto perspiciatis. Hic doloremque a sequi odit possimus dolorum
        repudiandae ratione, dolores ipsum molestiae, culpa consequatur
        cupiditate molestias accusantium vel quae!
      </p>
      <form
        class="space-y-5 rounded-xl bg-purple-100 p-4 sm:p-5 md:p-7 lg:basis-7/12"
        @submit.prevent="submit"
      >
        <AppInput
          v-model="form.name"
          label="Name"
          name="name"
          class="max-w-80"
        />
        <AppInput
          v-model="form.email"
          type="email"
          label="Email"
          name="email"
          class="max-w-80"
        />
        <AppTextarea
          v-model="form.message"
          label="What do you want to tell us?"
          name="message"
        />
        <button
          type="submit"
          class="rounded-full bg-purple-700 px-10 py-2 text-sm text-white md:!mt-12 md:px-12 md:py-3 md:text-base"
        >
          Submit
        </button>
      </form>
    </div>
    <div
      class="mt-14 bg-orange-50 px-5 py-10 md:px-10 md:py-14 xl:px-24 xl:py-28"
    >
      <h2
        class="mb-7 text-center text-3xl font-bold text-purple-700 md:text-4xl lg:mb-10 xl:mb-14 xl:text-5xl 2xl:mb-16 2xl:text-6xl"
      >
        Useful Contacts
      </h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium
        exercitationem, facilis possimus illo totam, laboriosam, esse alias a
        iure assumenda architecto vitae ab corrupti eos dicta doloremque illum
        voluptatibus nihil dolores. Recusandae hic minus tempora, nulla ipsum at
        natus suscipit praesentium architecto expedita, nam nobis id, quo autem
        corrupti culpa.
      </p>
    </div>
  </div>
</template>
