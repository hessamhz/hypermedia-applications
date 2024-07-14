<script setup>
import SectionHeader from "~/components/app/SectionHeader.vue";

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

  const submitButton = document.getElementById('submit-button')
  submitButton.textContent = 'Submitted!'

  setTimeout(function() {submitButton.textContent = 'Submit'}, 3000)
}

useSeoMeta({
  title: "Contact Us | The Hive",
  description: "Get in touch with The Hive, Anti-Violence Center for Women.",
  ogTitle: "Contact Us | The Hive",
  ogType: "website",
  ogUrl: "https://the-hive.space/",
  canonical: "https://the-hive.space/",
  ogSiteName: "The Hive"
});
</script>

<template>
  <div>
    <SectionHeader title="Contact Us"></SectionHeader>
    <div
      class="mx-auto max-w-[1240px] items-start gap-10 px-5 py-10 md:px-10 md:py-16 lg:flex xl:gap-11 xl:px-24 xl:py-28 2xl:gap-12"
    >
      <p class="mb-10 lg:basis-5/12 xl:text-lg 2xl:text-xl">
        The Hive is here to support and assist you.
        If you need help, have questions, or want to learn more about our services,
        please reach out to us with an email by filling this form
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
          id="submit-button"
          type="submit"
          class="rounded-full bg-hive-purple px-10 py-2 text-sm text-white md:!mt-12 md:px-12 md:py-3 md:text-base hover:bg-hive-dark-purple"
        >
          Submit
        </button>
      </form>
    </div>
    <div
      class="mt-14 bg-hive-beige px-5 py-10 md:px-10 md:py-14 xl:px-24 xl:py-28"
    >
      <h2
        class="mb-7 text-center text-3xl font-bold text-hive-purple md:text-4xl lg:mb-10 xl:mb-14 xl:text-5xl 2xl:mb-16 2xl:text-6xl"
      >
        More Useful Contacts
      </h2>
      <div class="flex flex-col gap-1 items-center md:grid md:grid-cols-2 md:justify-items-end md:gap-x-12 md:gap-y-4 xl:px-48 text-2xl">
        <p class="font-semibold  text-hive-purple">+1522</p>
        <p class="justify-self-start mb-3 md:mb-0">Telefono Rosa</p>
        <p class="font-semibold text-2xl text-hive-purple">+1 254 154 1221</p>
        <p class="justify-self-start">The Hive</p>
      </div>
    </div>
  </div>
</template>
