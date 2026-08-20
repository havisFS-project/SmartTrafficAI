<script setup>
import {
  VideoCameraIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6 shadow-lg"
  >
    <div class="mb-5 flex items-center justify-between">
      <div>
        <h2 class="app-text text-xl font-semibold">
          Live CCTV
        </h2>

        <p class="app-text-muted text-sm">
          Realtime Camera Preview
        </p>
      </div>

      <div class="rounded-xl bg-[#005B41]/20 p-3">
        <VideoCameraIcon class="h-6 w-6 text-[#00A884]" />
      </div>
    </div>

    <div
      class="app-surface-soft app-border flex h-64 items-center justify-center rounded-xl border border-dashed"
    >
      <div class="text-center">
        <VideoCameraIcon
          class="mx-auto h-16 w-16 text-gray-500"
        />

        <p class="app-text-muted mt-4">
          Camera Preview
        </p>

        <p class="app-text-muted text-sm">
          Waiting for stream...
        </p>
      </div>
    </div>

    <div class="mt-5 flex items-center justify-between">
      <div>
        <p class="app-text">
          Camera 01
        </p>

        <p class="app-text-muted text-sm">
          Main Intersection
        </p>
      </div>

      <div
        class="flex items-center gap-2 rounded-full bg-green-500/10 px-3 py-1"
      >
        <div class="h-2 w-2 animate-pulse rounded-full bg-green-400" />

        <span class="text-sm text-green-400">
          Live
        </span>
      </div>
    </div>
  </div>
</template>