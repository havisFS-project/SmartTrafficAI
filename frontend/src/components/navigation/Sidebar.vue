<script setup>
import {
  HomeIcon,
  VideoCameraIcon,
  ChartBarIcon,
  DocumentChartBarIcon,
  Cog6ToothIcon,
  SparklesIcon,
  MoonIcon,
} from "@heroicons/vue/24/outline"

const menus = [
  {
    name: "Dashboard",
    icon: HomeIcon,
    path: "/",
  },
  {
    name: "CCTV",
    icon: VideoCameraIcon,
    path: "/cctv",
  },
  {
    name: "Analytics",
    icon: ChartBarIcon,
    path: "/analytics",
  },
  {
    name: "Reports",
    icon: DocumentChartBarIcon,
    path: "/reports",
  },
  {
    name: "AI Assistant",
    icon: SparklesIcon,
    path: "/chatbot",
  },
]
</script>

<template>

<aside
class="w-72 bg-[#232D3F] text-white h-screen flex flex-col justify-between">

<div>

<div class="p-6">

<h1 class="text-3xl font-bold text-[#008170]">

SmartTrafficAI

</h1>

<p class="text-sm text-gray-400">

AI Traffic Monitoring

</p>

</div>

<nav class="mt-8">

<RouterLink
  v-for="menu in menus"
  :key="menu.name"
  :to="menu.path"
  class="group flex items-center gap-3 mx-3 my-1 rounded-xl px-4 py-3 transition-all duration-300"
  active-class="bg-[#005B41] text-white shadow-lg"
>
  <component
    :is="menu.icon"
    class="w-6 h-6 transition-all duration-300"
  />

  <span class="font-medium">
    {{ menu.name }}
  </span>
</RouterLink>

</nav>

</div>

<div class="border-t border-gray-700 p-6">

<p class="text-sm text-gray-300">

👤 Havis

</p>

</div>

</aside>

</template>