<template>
  <!-- The footer section of the webpage -->
  <footer
    class="flex flex-col gap-10 bg-hive-dark-purple px-5 py-7 md:flex-row md:justify-between lg:px-10 lg:py-14 xl:px-14 2xl:px-20 2xl:py-20"
  >
    <ul class="space-y-2 text-white xl:text-lg 2xl:text-xl">
      <li>
        Email:
        <strong>info@the-hive.space</strong>
      </li>
      <li>
        Phone number:
        <strong>+1 254 154 1221</strong>
      </li>
      <li>
        Address:
        <strong>Piazza Leonardo da Vinci, 32, 20133 Milano MI</strong>
      </li>
      <li>
        <p class="pt-16 text-sm text-white">
          All suggested names and pictures are either fictional or taken from
          <a href="https://www.pexels.com">https://www.pexels.com</a>
          .
        </p>
        <p class="text-sm text-white">
          This website is a project created for educational purposes.
        </p>
      </li>
    </ul>
    <iframe
      title="Center Location"
      loading="lazy"
      allowfullscreen
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d23086.889612024712!2d9.203250590024869!3d45.485194131014424!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4786c6f67dd11753%3A0x8e30fae1774a3377!2sPolitecnico%20di%20Milano!5e0!3m2!1sen!2sit!4v1720388326166!5m2!1sen!2sit"
      class="h-[320px] w-full max-w-xl border-0 md:w-7/12"
    ></iframe>
  </footer>
</template>
<script>
export default {
  name: 'AppFooter',
};
</script>
