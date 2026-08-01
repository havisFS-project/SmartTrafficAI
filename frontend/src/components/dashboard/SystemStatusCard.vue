<script setup>

const systems = [
  {
    name:"Backend",
    status:"Online",
    color:"bg-green-500"
  },
  {
    name:"AI Engine",
    status:"Running",
    color:"bg-green-500"
  },
  {
    name:"MongoDB",
    status:"Connected",
    color:"bg-green-500"
  },
  {
    name:"YOLO Model",
    status:"Loaded",
    color:"bg-green-500"
  },
]

</script>

<template>

<div class="rounded-2xl border border-white/5 bg-[#232D3F] p-6 shadow-lg h-full">

<h2 class="text-lg font-semibold text-white">
System Status
</h2>

<p class="mb-6 text-sm text-gray-400">
Realtime Services
</p>

<div class="space-y-5">

<div
v-for="item in systems"
:key="item.name"
class="flex items-center justify-between">

<span class="text-gray-300">

{{ item.name }}

</span>

<div class="flex items-center gap-2">

<div
:class="[item.color,'h-2 w-2 rounded-full animate-pulse']">
</div>

<span class="text-green-400 text-sm">

{{ item.status }}

</span>

</div>

</div>

</div>

</div>

</template>