<script setup>
import { toggleTheme } from "@/utils/theme"

import {
  Bars3Icon,
  MagnifyingGlassIcon,
  BellIcon,
  MoonIcon,
} from "@heroicons/vue/24/outline"

import { BaseInput } from "@/components/ui"
</script>

<template>
  <header
    class="app-surface app-border flex h-20 items-center justify-between border-b px-8"
  >

    <!-- LEFT -->
    <div class="flex items-center gap-6">

      <!-- Sidebar Toggle -->
      <button
        class="rounded-xl p-2 transition duration-300 hover:scale-105 hover:bg-white/5"
      >
        <Bars3Icon
          class="h-6 w-6 text-gray-300"
        />
      </button>

      <!-- Search -->
      <div class="relative w-96">

        <MagnifyingGlassIcon
          class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-gray-400"
        />

        <BaseInput
          placeholder="Search cameras, roads, reports..."
          class="pl-12"
        />

      </div>

    </div>

    <!-- RIGHT -->
    <div class="flex items-center gap-3">

      <!-- Notification -->
      <div class="relative">

      <button
        class="rounded-xl p-2 transition-all duration-300 hover:scale-105 hover:bg-white/5"
      >
        <BellIcon class="h-6 w-6 text-gray-300"/>
      </button>

      <span
        class="absolute right-2 top-2 h-2.5 w-2.5 rounded-full bg-red-500"
      ></span>

      </div>

      <!-- Dark Mode -->
      <button
        type="button"
        @click="toggleTheme"
      >
        <MoonIcon class="h-6 w-6 text-gray-300" />
      </button>

      <!-- User -->
      <div
        class="ml-3 flex cursor-pointer items-center gap-3 rounded-xl px-3 py-2 transition hover:bg-white/5 hover:shadow-md"
      >

        <div
          class="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-r from-[#005B41] to-[#008170] font-semibold text-white ring-2 ring-[#008170]/20"
        >
          HF
        </div>

        <div>

          <p class="app-text font-medium">
            Havis
          </p>

          <p class="app-text-muted text-xs">
            Administrator
          </p>

        </div>

      </div>

    </div>

  </header>
</template>

<script setup>
</script>