<script setup>
import {
  VideoCameraIcon,
  SignalIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>

<div
class="rounded-2xl border border-white/5 bg-[#232D3F] p-6 shadow-lg">

<div class="mb-5 flex items-center justify-between">

<div>

<h2 class="text-xl font-semibold text-white">
Live CCTV
</h2>

<p class="text-sm text-gray-400">
Realtime Camera Preview
</p>

</div>

<div
class="rounded-xl bg-[#005B41]/30 p-3">

<VideoCameraIcon
class="h-6 w-6 text-[#00A884]" />

</div>

</div>

<div
class="flex h-64 items-center justify-center rounded-xl border border-dashed border-gray-700 bg-[#1A2332]">

<div class="text-center">

<VideoCameraIcon
class="mx-auto h-16 w-16 text-gray-600" />

<p class="mt-4 text-gray-400">
Camera Preview
</p>

<p class="text-sm text-gray-500">
Waiting for stream...
</p>

</div>

</div>

<div
class="mt-5 flex items-center justify-between">

<div>

<p class="text-white">
Camera 01
</p>

<p class="text-sm text-gray-500">
Main Intersection
</p>

</div>

<div
class="flex items-center gap-2 rounded-full bg-green-500/10 px-3 py-1">

<div
class="h-2 w-2 animate-pulse rounded-full bg-green-400">
</div>

<span class="text-sm text-green-400">
Live
</span>

</div>

</div>

</div>

</template>