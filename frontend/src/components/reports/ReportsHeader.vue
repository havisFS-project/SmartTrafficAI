<script setup>
import { DocumentTextIcon } from "@heroicons/vue/24/outline"
import ReportsExport from "./ReportsExport.vue"
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
          Reports
        </h1>

        <p class="app-text-muted mt-2 text-lg">
          AI Traffic Reports & Historical Records
        </p>
      </div>

      <div class="flex flex-wrap gap-3">
        <button
          class="app-surface-soft app-text flex items-center gap-3 rounded-xl px-5 py-3 transition hover:opacity-80"
        >
          <DocumentTextIcon class="h-5 w-5" />
          Generate Report
        </button>

        <ReportsExport />
      </div>
    </div>
  </section>
</template>