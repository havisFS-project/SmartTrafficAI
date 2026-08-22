<script setup>
import {
  ArrowPathIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border px-5 py-4"
  >
    <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
      <div class="flex flex-wrap gap-3">
        <select
          class="app-surface-soft app-text app-border rounded-xl border px-4 py-2.5 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/20"
        >
          <option>Last 24 Hours</option>
          <option>Last 7 Days</option>
          <option>Last 30 Days</option>
        </select>

        <select
          class="app-surface-soft app-text app-border rounded-xl border px-4 py-2.5 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/20"
        >
          <option>All Cameras</option>
          <option>Camera 01</option>
          <option>Camera 02</option>
          <option>Camera 03</option>
        </select>
      </div>

      <button
        class="flex items-center justify-center gap-2 rounded-xl bg-[#008170] px-4 py-2.5 font-medium text-white transition hover:bg-[#00A884]"
      >
        <ArrowPathIcon class="h-5 w-5" />

        Refresh
      </button>
    </div>
  </section>
</template>