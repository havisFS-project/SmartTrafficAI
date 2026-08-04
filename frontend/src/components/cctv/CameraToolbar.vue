<script setup>
import {
  MagnifyingGlassIcon,
  ArrowPathIcon,
  PlusIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>

<div class="mb-6 rounded-2xl border border-white/5 bg-[#232D3F] p-5 shadow-lg">

  <!-- Header -->
  <div class="mb-5 flex items-center justify-between">

    <div>

      <h1 class="text-2xl font-bold text-white">
        CCTV Monitoring
      </h1>

      <p class="text-gray-400">
        Monitor all connected cameras in realtime
      </p>

    </div>

    <button
      class="flex items-center gap-2 rounded-xl bg-[#008170] px-4 py-3 text-white transition hover:bg-[#00A884]">

      <PlusIcon class="h-5 w-5"/>

      Add Camera

    </button>

  </div>

  <!-- Toolbar -->
  <div class="flex flex-wrap items-center gap-4">

    <!-- Search -->

    <div class="relative flex-1 min-w-[250px]">

      <MagnifyingGlassIcon
        class="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-gray-400"/>

      <input

        type="text"

        placeholder="Search camera..."

        class="w-full rounded-xl border border-white/10 bg-[#1B2435] py-3 pl-12 pr-4 text-white outline-none transition focus:border-[#008170]"

      />

    </div>

    <!-- Filter -->

    <select
      class="rounded-xl border border-white/10 bg-[#1B2435] px-4 py-3 text-white outline-none">

      <option>All Status</option>

      <option>Live</option>

      <option>Offline</option>

      <option>Maintenance</option>

    </select>

    <!-- Refresh -->

    <button
      class="flex items-center gap-2 rounded-xl bg-[#1B2435] px-4 py-3 text-white transition hover:bg-[#273449]">

      <ArrowPathIcon class="h-5 w-5"/>

      Refresh

    </button>

  </div>

</div>

</template>