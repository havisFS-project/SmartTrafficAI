<script setup>
import {
  VideoCameraIcon,
  SignalIcon,
} from "@heroicons/vue/24/outline"

defineProps({
  title: {
    type: String,
    required: true,
  },

  location: {
    type: String,
    required: true,
  },

  status: {
    type: String,
    default: "Live",
  },

  fps: {
    type: Number,
    default: 0,
  },
})

const statusMap = {
  Live: {
    text: "text-green-400",
    background: "bg-green-500/10",
    dot: "bg-green-500",
  },

  Offline: {
    text: "text-red-400",
    background: "bg-red-500/10",
    dot: "bg-red-500",
  },

  Maintenance: {
    text: "text-yellow-400",
    background: "bg-yellow-500/10",
    dot: "bg-yellow-500",
  },
}
</script>

<template>
  <div
    class="app-surface app-border group rounded-2xl border p-5 shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-[#008170]/40 hover:shadow-[0_10px_30px_rgba(0,168,132,.12)]"
  >
    <!-- Header -->
    <div class="flex items-start justify-between">
      <div>
        <h3 class="app-text text-lg font-semibold">
          {{ title }}
        </h3>

        <p class="app-text-muted text-sm">
          {{ location }}
        </p>
      </div>

      <div class="rounded-xl bg-[#005B41]/10 p-3">
        <VideoCameraIcon class="h-6 w-6 text-[#00A884]" />
      </div>
    </div>

    <!-- Preview -->
    <div
      class="app-surface-soft app-border mt-5 flex h-52 items-center justify-center rounded-xl border border-dashed"
    >
      <div class="text-center">
        <VideoCameraIcon
          class="mx-auto mb-4 h-14 w-14 text-gray-500"
        />

        <p class="app-text-muted">
          Waiting for stream...
        </p>
      </div>
    </div>

    <!-- Footer -->
    <div class="mt-5 flex items-center justify-between">
      <!-- Status -->
      <div
        class="flex items-center gap-2 rounded-full px-3 py-1"
        :class="
          statusMap[status]?.background ?? 'bg-gray-500/10'
        "
      >
        <span
          class="h-2.5 w-2.5 rounded-full"
          :class="[
            statusMap[status]?.dot ?? 'bg-gray-500',
            status === 'Live' ? 'animate-pulse' : '',
          ]"
        />

        <span
          class="text-sm font-medium"
          :class="
            statusMap[status]?.text ?? 'text-gray-400'
          "
        >
          {{ status }}
        </span>
      </div>

      <!-- FPS -->
      <div class="flex items-center gap-2">
        <SignalIcon class="app-text-muted h-5 w-5" />

        <span class="app-text-muted text-sm">
          {{ fps }} FPS
        </span>
      </div>
    </div>
  </div>
</template>