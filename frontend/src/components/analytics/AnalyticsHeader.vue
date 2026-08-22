<script setup>
import {
  ArrowDownTrayIcon,
  CalendarDaysIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="app-surface app-border rounded-3xl border p-7"
  >
    <div
      class="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between"
    >
      <div>
        <h1 class="app-text text-4xl font-bold">
          Analytics Dashboard
        </h1>

        <p class="app-text-muted mt-2 text-lg">
          AI Traffic Insights & Historical Analysis
        </p>
      </div>

      <div class="flex gap-3">
        <button
          class="app-surface-soft app-text flex items-center gap-2 rounded-xl px-5 py-3 transition hover:opacity-80"
        >
          <CalendarDaysIcon class="h-5 w-5" />

          Last 24 Hours
        </button>

        <button
          class="flex items-center gap-2 rounded-xl bg-[#008170] px-5 py-3 font-medium text-white transition hover:bg-[#00A884]"
        >
          <ArrowDownTrayIcon class="h-5 w-5" />

          Export
        </button>
      </div>
    </div>
  </section>
</template>