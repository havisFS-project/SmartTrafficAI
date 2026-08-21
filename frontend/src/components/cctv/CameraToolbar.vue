<script setup>
import {
  MagnifyingGlassIcon,
  ArrowPathIcon,
  PlusIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border p-5"
  >
    <!-- Header -->
    <div class="mb-5 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h1 class="app-text text-2xl font-bold">
          CCTV Monitoring
        </h1>

        <p class="app-text-muted mt-1">
          Monitor all connected cameras in realtime
        </p>
      </div>

      <button
        class="flex items-center justify-center gap-2 rounded-xl bg-[#008170] px-4 py-3 font-medium text-white transition hover:bg-[#00A884]"
      >
        <PlusIcon class="h-5 w-5" />

        Add Camera
      </button>
    </div>

    <!-- Toolbar -->
    <div class="flex flex-col gap-3 lg:flex-row">
      <!-- Search -->
      <div class="relative flex-1">
        <MagnifyingGlassIcon
          class="app-text-muted absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2"
        />

        <input
          type="text"
          placeholder="Search camera..."
          class="app-surface-soft app-text app-border w-full rounded-xl border py-3 pl-12 pr-4 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/30 placeholder:text-gray-500"
        />
      </div>

      <!-- Status -->
      <select
        class="app-surface-soft app-text app-border rounded-xl border px-4 py-3 outline-none transition focus:border-[#00A884]"
      >
        <option>All Status</option>
        <option>Live</option>
        <option>Offline</option>
        <option>Maintenance</option>
      </select>

      <!-- Refresh -->
      <button
        class="app-surface-soft app-text flex items-center justify-center gap-2 rounded-xl px-4 py-3 transition hover:opacity-80"
      >
        <ArrowPathIcon class="h-5 w-5" />

        Refresh
      </button>
    </div>
  </section>
</template>