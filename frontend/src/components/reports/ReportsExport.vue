<script setup>
import {
  DocumentArrowDownIcon,
  TableCellsIcon,
} from "@heroicons/vue/24/outline"

const exportPdf = () => {
  console.log("Export PDF")
}

const exportExcel = () => {
  console.log("Export Excel")
}
</script>

<template>
  <div class="flex items-center gap-3">
    <button
      type="button"
      class="app-surface-soft app-text flex items-center gap-2 rounded-xl px-4 py-3 font-medium transition hover:opacity-80"
      @click="exportPdf"
    >
      <DocumentArrowDownIcon class="h-5 w-5" />

      Export PDF
    </button>

    <button
      type="button"
      class="flex items-center gap-2 rounded-xl bg-[#008170] px-4 py-3 font-medium text-white transition hover:bg-[#00A884]"
      @click="exportExcel"
    >
      <TableCellsIcon class="h-5 w-5" />

      Export Excel
    </button>
  </div>
</template>