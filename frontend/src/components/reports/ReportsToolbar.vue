<script setup>
import {
  MagnifyingGlassIcon,
  FunnelIcon,
  ArrowPathIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="flex flex-col gap-4 rounded-2xl border border-white/5 bg-[#232D3F] p-5 lg:flex-row lg:items-center lg:justify-between"
  >
    <!-- Search -->

    <div class="relative w-full lg:max-w-md">

      <MagnifyingGlassIcon
        class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-gray-400"
      />

      <input
        type="text"
        placeholder="Search reports..."
        class="w-full rounded-xl border border-white/10 bg-[#1B2435] py-3 pl-12 pr-4 text-white placeholder:text-gray-500 focus:border-[#00A884] focus:outline-none"
      />

    </div>

    <!-- Filter -->

    <div class="flex flex-wrap items-center gap-3">

      <select
        class="rounded-xl border border-white/10 bg-[#1B2435] px-4 py-3 text-white outline-none"
      >
        <option>All Cameras</option>
        <option>Camera 01</option>
        <option>Camera 02</option>
      </select>

      <select
        class="rounded-xl border border-white/10 bg-[#1B2435] px-4 py-3 text-white outline-none"
      >
        <option>Today</option>
        <option>Last 7 Days</option>
        <option>Last Month</option>
      </select>

      <button
        class="flex items-center gap-2 rounded-xl bg-[#1B2435] px-4 py-3 text-white transition hover:bg-[#2B3548]"
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

  </section>
</template>