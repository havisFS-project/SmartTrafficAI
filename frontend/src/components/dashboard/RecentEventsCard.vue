<script setup>
import {
  ExclamationTriangleIcon,
  TruckIcon,
  CheckCircleIcon,
  ClockIcon,
} from "@heroicons/vue/24/outline"

const events = [
  {
    title: "Accident Detected",
    location: "Highway KM 12",
    time: "2 min ago",
    color: "text-red-400",
    icon: ExclamationTriangleIcon,
  },
  {
    title: "Heavy Traffic",
    location: "City Center",
    time: "5 min ago",
    color: "text-yellow-400",
    icon: TruckIcon,
  },
  {
    title: "Road Cleared",
    location: "South Ring Road",
    time: "12 min ago",
    color: "text-green-400",
    icon: CheckCircleIcon,
  },
]
</script>

<template>

<div
class="rounded-2xl border border-white/5 bg-[#232D3F] p-6 shadow-lg">

<div class="mb-6 flex items-center justify-between">

<h2
class="text-xl font-semibold text-white">

Recent Events

</h2>

<ClockIcon
class="h-6 w-6 text-gray-400"/>

</div>

<div class="space-y-5">

<div
v-for="event in events"
:key="event.title"
class="flex gap-4 rounded-xl bg-[#1A2332] p-4 transition hover:bg-[#202C3D]">

<component
:is="event.icon"
:class="['h-6 w-6',event.color]" />

<div>

<p
class="font-medium text-white">

{{ event.title }}

</p>

<p
class="text-sm text-gray-400">

{{ event.location }}

</p>

<p
class="mt-1 text-xs text-gray-500">

{{ event.time }}

</p>

</div>

</div>

</div>

</div>

</template>