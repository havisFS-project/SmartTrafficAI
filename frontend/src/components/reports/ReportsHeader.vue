<script setup>
import {
  ArrowDownTrayIcon,
  DocumentTextIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="flex flex-col gap-6 rounded-3xl border border-white/5 bg-[#232D3F] p-7 lg:flex-row lg:items-center lg:justify-between"
  >
    <div>
      <h1 class="text-4xl font-bold text-white">
        Reports
      </h1>

      <p class="mt-2 text-lg text-gray-400">
        AI Traffic Reports & Historical Records
      </p>
    </div>

    <div class="flex gap-4">
      <button
        class="flex items-center gap-3 rounded-2xl bg-[#1B2435] px-6 py-3 text-white transition hover:bg-[#2B3548]"
      >
        <DocumentTextIcon class="h-5 w-5" />

        Generate Report
      </button>

      <button
        class="flex items-center gap-3 rounded-2xl bg-[#008170] px-6 py-3 text-white transition hover:bg-[#00A884]"
      >
        <ArrowDownTrayIcon class="h-5 w-5" />

        Export
      </button>
    </div>
  </section>
</template>