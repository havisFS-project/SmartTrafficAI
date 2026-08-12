<script setup>
import {
  ChevronLeftIcon,
  ChevronRightIcon,
} from "@heroicons/vue/24/outline"

defineProps({
  currentPage: {
    type: Number,
    default: 1,
  },
  totalPages: {
    type: Number,
    default: 5,
  },
})

const emit = defineEmits(["change"])

const goToPage = (page) => {
  emit("change", page)
}
</script>

<template>
  <div
    class="flex flex-col gap-4 border-t border-white/5 px-6 py-4 sm:flex-row sm:items-center sm:justify-between"
  >
    <p class="text-sm text-gray-400">
      Showing
      <span class="font-medium text-white">1</span>
      to
      <span class="font-medium text-white">10</span>
      of
      <span class="font-medium text-white">248</span>
      reports
    </p>

    <div class="flex items-center gap-2">
      <button
        class="rounded-lg border border-white/10 bg-[#1B2435] p-2 text-gray-400 transition hover:bg-[#2B3548] hover:text-white disabled:cursor-not-allowed disabled:opacity-40"
        :disabled="currentPage === 1"
        @click="goToPage(currentPage - 1)"
      >
        <ChevronLeftIcon class="h-5 w-5" />
      </button>

      <button
        v-for="page in totalPages"
        :key="page"
        class="h-9 min-w-9 rounded-lg px-3 text-sm font-medium transition"
        :class="
          page === currentPage
            ? 'bg-[#008170] text-white'
            : 'bg-[#1B2435] text-gray-400 hover:bg-[#2B3548] hover:text-white'
        "
        @click="goToPage(page)"
      >
        {{ page }}
      </button>

      <button
        class="rounded-lg border border-white/10 bg-[#1B2435] p-2 text-gray-400 transition hover:bg-[#2B3548] hover:text-white disabled:cursor-not-allowed disabled:opacity-40"
        :disabled="currentPage === totalPages"
        @click="goToPage(currentPage + 1)"
      >
        <ChevronRightIcon class="h-5 w-5" />
      </button>
    </div>
  </div>
</template>