<script setup>
import {
  ArrowPathIcon,
  ArrowDownTrayIcon,
  FunnelIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <div
    class="mb-6 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-white/5 bg-[#232D3F] p-4"
  >
    <!-- Left -->

    <div class="flex flex-wrap gap-3">
      <select
        class="rounded-xl border border-white/10 bg-[#1B2435] px-4 py-2 text-sm text-gray-300 outline-none"
      >
        <option>Last 24 Hours</option>
        <option>Last 7 Days</option>
        <option>Last 30 Days</option>
      </select>

      <select
        class="rounded-xl border border-white/10 bg-[#1B2435] px-4 py-2 text-sm text-gray-300 outline-none"
      >
        <option>All Cameras</option>
        <option>Camera 01</option>
        <option>Camera 02</option>
        <option>Camera 03</option>
      </select>
    </div>

    <!-- Right -->

    <div class="flex gap-3">
      <button
        class="flex items-center gap-2 rounded-xl bg-[#008170] px-4 py-2 text-white transition hover:bg-[#00A884]"
      >
        <ArrowPathIcon class="h-5 w-5" />
        Refresh
      </button>
    </div>
  </div>
</template>