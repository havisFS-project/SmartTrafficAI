<script setup>
import {
  MagnifyingGlassIcon,
  FunnelIcon,
  ArrowPathIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border p-5"
  >
    <div
      class="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between"
    >
      <div class="relative w-full lg:max-w-md">
        <MagnifyingGlassIcon
          class="app-text-muted absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2"
        />

        <input
          type="text"
          placeholder="Search reports..."
          class="app-surface-soft app-text app-border w-full rounded-xl border py-3 pl-12 pr-4 outline-none transition-all duration-300 placeholder:text-gray-500 focus:border-[#00A884] focus:ring-4 focus:ring-[#008170]/20 focus:shadow-[0_0_16px_rgba(0,168,132,0.2)]"
        />
      </div>

      <div class="flex flex-wrap gap-3">
        <select
          class="app-surface-soft app-text app-border rounded-xl border px-4 py-3 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/20"
        >
          <option>All Cameras</option>
          <option>Camera 01</option>
          <option>Camera 02</option>
          <option>Camera 03</option>
        </select>

        <select
          class="app-surface-soft app-text app-border rounded-xl border px-4 py-3 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/20"
        >
          <option>Today</option>
          <option>Last 7 Days</option>
          <option>Last Month</option>
        </select>

        <button
          class="app-surface-soft app-text flex items-center gap-2 rounded-xl px-4 py-3 transition hover:opacity-80"
        >
          <FunnelIcon class="h-5 w-5" />
          Filter
        </button>

        <button
          class="flex items-center gap-2 rounded-xl bg-[#008170] px-4 py-3 text-white transition hover:bg-[#00A884]"
        >
          <ArrowPathIcon class="h-5 w-5" />
          Refresh
        </button>
      </div>
    </div>
  </section>
</template>