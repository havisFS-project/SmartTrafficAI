<script setup>
import {
  CloudIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>

<div class="rounded-2xl border border-white/5 bg-[#232D3F] p-6 shadow-lg h-full">

<div class="flex items-center justify-between">

<div>

<h2 class="text-lg font-semibold text-white">
Weather
</h2>

<p class="text-sm text-gray-400">
Current Condition
</p>

</div>

<CloudIcon class="h-7 w-7 text-sky-400"/>

</div>

<div class="mt-8 text-center">

<p class="text-5xl font-bold text-white">
28°
</p>

<p class="mt-2 text-gray-400">
Sunny
</p>

</div>

<div class="mt-8 space-y-3 text-sm">

<div class="flex justify-between">

<span class="text-gray-400">
Humidity
</span>

<span class="text-white">
71%
</span>

</div>

<div class="flex justify-between">

<span class="text-gray-400">
Wind
</span>

<span class="text-white">
12 km/h
</span>

</div>

<div class="flex justify-between">

<span class="text-gray-400">
Visibility
</span>

<span class="text-white">
5 km
</span>

</div>

</div>

</div>

</template>