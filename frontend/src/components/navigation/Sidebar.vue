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
    badge: null,
  },
  {
    name: "CCTV",
    icon: VideoCameraIcon,
    path: "/cctv",
    badge: 3,
  },
  {
    name: "Analytics",
    icon: ChartBarIcon,
    path: "/analytics",
    badge: null,
  },
  {
    name: "Reports",
    icon: DocumentChartBarIcon,
    path: "/reports",
    badge: null,
  },
  {
    name: "AI Assistant",
    icon: SparklesIcon,
    path: "/chatbot",
    badge: "AI",
  },
]

const systems = [
  {
    name: "Backend",
    status: "Online",
  },
  {
    name: "AI Engine",
    status: "Ready",
  },
  {
    name: "MongoDB",
    status: "Connected",
  },
]
</script>

<template>
  <aside class="app-surface flex h-screen w-72 flex-col">

    <!-- Logo -->
    <div class="border-b border-white/5 px-7 py-8">

      <h1 class="text-2xl font-bold tracking-wide text-[#00A884]">
        SmartTrafficAI
      </h1>

      <p class="mt-2 text-sm text-gray-400">
        AI Powered Traffic Monitoring
      </p>

    </div>

    <!-- Navigation -->
    <nav class="flex-1 overflow-y-auto py-6 scrollbar-thin scrollbar-thumb-[#005B41]">

      <!-- OVERVIEW -->
      <div>

        <p
          class="px-7 pb-3 text-xs font-semibold uppercase tracking-[0.25em] text-gray-500"
        >
          Overview
        </p>

        <RouterLink
           v-for="menu in menus"
           :key="menu.name"
           :to="menu.path"
           class="group relative mx-3 mb-2 flex items-center gap-4 rounded-xl px-5 py-3 text-gray-300 transition-all duration-300 hover:bg-[#005B41]/20 hover:text-white hover:shadow-md"
           active-class="bg-[#005B41] text-white shadow-lg"
        >
          <div class="absolute left-0 h-8 w-1 rounded-r-full bg-[#00A884]"></div>
          <component
            :is="menu.icon"
            class="h-6 w-6 transition-all duration-300 group-hover:scale-110"
          />

          <span class="font-medium transition-all duration-300 group-hover:translate-x-1">
            {{ menu.name }}
          </span>

          <span
            v-if="menu.badge"
            class="ml-auto rounded-full bg-[#008170] px-2 py-1 text-xs font-semibold text-white"
          >
            {{ menu.badge }}
          </span>
        </RouterLink>

      </div>

      <!-- SYSTEM -->
      <div class="mt-10">

        <p
          class="px-7 pb-4 text-xs font-semibold uppercase tracking-[0.25em] text-gray-500"
        >
          System
        </p>

        <div class="space-y-4 px-7">

          <div 
            v-for="system in systems"
            :key="system.name"
            class="flex items-center gap-3 rounded-lg px-3 py-2 hover:bg-white/5"
          >
          
          <div class="h-2 w-2 rounded-full bg-[#00A884]"></div>
          
          <div>
            
            <p class="text-sm font-medium">
              {{ system.name }}
            </p>
            
            <p class="text-xs text-[#00D68F]">
              {{ system.status }}
            </p>
          
          </div>
          </div>

        </div>

      </div>

      <!-- Divider -->
      <div class="mx-6 my-8 border-t border-white/10"></div>

      <!-- Preferences -->
      <div>

        <p
          class="px-7 pb-4 text-xs font-semibold uppercase tracking-[0.25em] text-gray-500"
        >
          Preferences
        </p>

        <div class="space-y-2 px-3">

          <RouterLink
            to="/settings"
            class="flex w-full items-center gap-4 rounded-xl px-4 py-3 text-gray-300 transition-all duration-300 hover:bg-white/5 hover:text-white"
            active-class="bg-[#005B41] text-white"
          >
            <Cog6ToothIcon class="h-6 w-6" />

            <span class="font-medium">
              Settings
            </span>
          </RouterLink>

          <button
            class="flex w-full items-center gap-4 rounded-xl px-4 py-3 text-gray-300 transition hover:bg-[#005B41]/30 hover:text-white"
          >
            <MoonIcon class="h-6 w-6" />

            Dark Mode
          </button>

        </div>

      </div>

    </nav>

    <!-- Footer -->
    <div class="border-t border-white/10 p-5">

      <div class="flex items-center gap-4">

        <div
          class="flex h-12 w-12 items-center justify-center rounded-full bg-gradient-to-r from-[#005B41] to-[#008170] font-bold shadow-lg"
        >
          HF
        </div>

        <div>

          <p class="font-semibold">
            Havis
          </p>

          <p class="text-sm text-gray-400">
            Administrator
          </p>

          <p class="mt-1 text-xs text-gray-500">
            Version 0.1.0
          </p>

        </div>

      </div>

    </div>

  </aside>
</template>