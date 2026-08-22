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
    class="app-border flex flex-col gap-4 border-t px-6 py-4 sm:flex-row sm:items-center sm:justify-between"
  >
    <p class="app-text-muted text-sm">
      Showing
      <span class="app-text font-medium">1</span>
      to
      <span class="app-text font-medium">10</span>
      of
      <span class="app-text font-medium">248</span>
      reports
    </p>

    <div class="flex items-center gap-2">
      <button
        type="button"
        class="app-surface-soft app-text-muted rounded-lg p-2 transition hover:opacity-80 disabled:cursor-not-allowed disabled:opacity-40"
        :disabled="currentPage === 1"
        @click="goToPage(currentPage - 1)"
      >
        <ChevronLeftIcon class="h-5 w-5" />
      </button>

      <button
        v-for="page in totalPages"
        :key="page"
        type="button"
        class="h-9 min-w-9 rounded-lg px-3 text-sm font-medium transition"
        :class="
          page === currentPage
            ? 'bg-[#008170] text-white'
            : 'app-surface-soft app-text-muted hover:opacity-80'
        "
        @click="goToPage(page)"
      >
        {{ page }}
      </button>

      <button
        type="button"
        class="app-surface-soft app-text-muted rounded-lg p-2 transition hover:opacity-80 disabled:cursor-not-allowed disabled:opacity-40"
        :disabled="currentPage === totalPages"
        @click="goToPage(currentPage + 1)"
      >
        <ChevronRightIcon class="h-5 w-5" />
      </button>
    </div>
  </div>
</template>