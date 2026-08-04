<script setup>
import {
  ArrowDownTrayIcon,
  CalendarDaysIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>

<div class="mb-6 rounded-2xl border border-white/5 bg-[#232D3F] p-6 shadow-lg">

  <div class="flex flex-wrap items-center justify-between gap-4">

    <div>

      <h1 class="text-4xl font-bold text-white">
        Analytics Dashboard
      </h1>

      <p class="mt-2 text-gray-400">
        AI Traffic Insights & Historical Analysis
      </p>

    </div>

    <div class="flex items-center gap-3">

      <button
        class="flex items-center gap-2 rounded-xl bg-[#1B2435] px-4 py-3 text-white transition hover:bg-[#273449]">

        <CalendarDaysIcon class="h-5 w-5"/>

        Last 24 Hours

      </button>

      <button
        class="flex items-center gap-2 rounded-xl bg-[#008170] px-4 py-3 text-white transition hover:bg-[#00A884]">

        <ArrowDownTrayIcon class="h-5 w-5"/>

        Export

      </button>

    </div>

  </div>

</div>

</template>