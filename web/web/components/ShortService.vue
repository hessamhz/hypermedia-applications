<script setup>
    defineProps(['name', 'schedule',  'description'])
</script>

<template>
    <div class="flex flex-row border-2 items-center justify-center w-full mt-8 gap-3">
        <div class="flex items-center justify-center w-[10rem] h-[10rem] bg-[#D7A549] bg-opacity-20 rounded-xl">
            <img src="#">
        </div>
        <div class="flex flex-col items-start justify-top px-10 py-6 bg-[#D7A549] bg-opacity-20 w-[40rem] h-[10rem] rounded-xl ">
            <a class="font-semibold text-xl" href="/service"> {{ name }} </a>
            <p class="font-medium text-base text-gray-700"> {{ schedule }} </p>
            <p class="font-medium text-base"> {{ description }} </p>
        </div>
    </div>
    <div class="flex flex-row border-2 items-center justify-center w-full mt-3 gap-3">
        <div class="flex flex-col items-start justify-top px-10 py-6 bg-[#7A4194] bg-opacity-20 w-[40rem] h-[10rem] rounded-xl ">
            <h3 class="font-semibold text-xl"> {{ name }} </h3>
            <p class="font-medium text-base text-gray-700"> {{ schedule }} </p>
            <p class="font-medium text-base"> {{ description }} </p>
        </div>
        <div class="flex items-center justify-center w-[10rem] h-[10rem] bg-[#7A4194] bg-opacity-20 rounded-xl">
            <img src="#">
        </div>
    </div>
    <div class="flex flex-row border-2 items-center justify-center w-full mt-3 gap-3">
        <div class="flex items-center justify-center w-[10rem] h-[10rem] bg-[#D7A549] bg-opacity-20 rounded-xl">
            <img src="#">
        </div>
        <div class="flex flex-col items-start justify-top px-10 py-6 bg-[#D7A549] bg-opacity-20 w-[40rem] h-[10rem] rounded-xl ">
            <h3 class="font-semibold text-xl"> {{ name }} </h3>
            <p class="font-medium text-base text-gray-700"> {{ schedule }} </p>
            <p class="font-medium text-base"> {{ description }} </p>
        </div>
    </div>
</template>

