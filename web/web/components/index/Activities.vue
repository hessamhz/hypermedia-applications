<template>
    <div class="flex flex-col items-center justify-center bg-[#F4F1EC] h-[38rem] gap-12">
        <h1 class="font-bold text-5xl text-black text-center "> Our Activities</h1>

        <div class="flex flex-row justify-center  py-4 px-12 gap-12">
            <div class="flex flex-col items-start px-12 py-10 bg-[#794094] rounded-xl h-[24rem] w-[22rem] gap-20" >
                <div class="flex flex-col gap-8">
                    <h3 class="font-bold text-2xl text-white">Projects</h3>
                    <p class="font-medium text-base text-white">Lorem ipsum dolor sit amet consectetur. Sit quam ac pellentesque aenean ante. At dolor elementum mi mollis.</p>
                </div>
                <button @click="navigateTo({ path: '/projects' })" class="bg-white text-black px-10 py-2 rounded-full font-semibold" >See More</button>
            </div>
            <div class="flex flex-col items-start px-12 py-10 bg-[#D7A549] rounded-xl h-[24rem] w-[22rem] gap-20" >
                <div class="flex flex-col gap-8">
                    <h3 class="font-bold text-2xl">Services</h3>
                    <p class="font-medium text-base">Lorem ipsum dolor sit amet consectetur. Sit quam ac pellentesque aenean ante. At dolor elementum mi mollis.</p>
                </div>
                <button @click="navigateTo({ path: '/services' })" class="bg-white text-black px-10 py-2 rounded-full font-semibold" >See More</button>
            </div>
        </div>
    </div>
</template>
