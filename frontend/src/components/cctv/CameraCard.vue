<script setup>
import {
  VideoCameraIcon,
  SignalIcon,
} from "@heroicons/vue/24/outline"

defineProps({

  title: String,

  location: String,

  status: String,

  fps: Number,

})

</script>

<template>

<div
class="rounded-2xl
border border-white/5
bg-[#232D3F]
p-5
shadow-lg
transition-all
duration-300
hover:border-[#008170]
hover:-translate-y-1">

<!-- Header -->

<div class="flex items-start justify-between">

<div>

<h3 class="text-lg font-semibold text-white">

{{ title }}

</h3>

<p class="text-sm text-gray-400">

{{ location }}

</p>

</div>

<div
class="rounded-xl
bg-[#1B2A41]
p-3">

<VideoCameraIcon
class="h-6 w-6 text-[#00A884]"/>

</div>

</div>

<!-- Preview -->

<div
class="mt-5
flex
h-52
items-center
justify-center
rounded-xl
border
border-dashed
border-white/10
bg-[#1B2435]">

<div class="text-center">

<VideoCameraIcon
class="mx-auto
mb-4
h-14
w-14
text-gray-500"/>

<p class="text-gray-400">

Waiting for stream...

</p>

</div>

</div>

<!-- Footer -->

<div
class="mt-5
flex
items-center
justify-between">

<div
class="flex
items-center
gap-2">

<div
class="h-2.5
w-2.5
rounded-full
bg-green-500
animate-pulse">

</div>

<span class="text-green-400">

{{ status }}

</span>

</div>

<div
class="flex
items-center
gap-2
text-gray-400">

<SignalIcon class="h-5 w-5"/>

{{ fps }} FPS

</div>

</div>

</div>

</template>