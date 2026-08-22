<script setup>
import {
  SparklesIcon,
  LightBulbIcon,
  ClockIcon,
  CheckCircleIcon,
} from "@heroicons/vue/24/outline"

const recommendations = [
  "Increase green light duration",
  "Deploy traffic officers",
  "Open alternative route",
]
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6 shadow-lg"
  >
    <!-- Header -->
    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="app-text text-xl font-semibold">
          AI Insight
        </h2>

        <p class="app-text-muted text-sm">
          Realtime traffic intelligence
        </p>
      </div>

      <SparklesIcon class="h-7 w-7 text-[#00A884]" />
    </div>

    <!-- Prediction -->
    <div class="app-surface-soft rounded-xl p-5">
      <div class="flex items-start justify-between gap-4">
        <div>
          <p class="app-text text-lg font-semibold">
            Traffic is predicted to increase
          </p>

          <p class="app-text-muted mt-2">
            Expected between
            <span class="app-text font-medium">
              17:00 - 18:00
            </span>
          </p>
        </div>

        <span
          class="rounded-full bg-red-500/10 px-3 py-1 text-xs font-semibold text-red-400"
        >
          High Risk
        </span>
      </div>

      <!-- Recommendation -->
      <div class="mt-6">
        <p
          class="app-text-muted mb-3 text-xs font-semibold uppercase tracking-wider"
        >
          Recommendation
        </p>

        <div class="space-y-3">
          <div
            v-for="recommendation in recommendations"
            :key="recommendation"
            class="flex items-center gap-3"
          >
            <CheckCircleIcon class="h-5 w-5 text-[#00A884]" />

            <span class="app-text-muted">
              {{ recommendation }}
            </span>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div
        class="app-border mt-6 flex flex-col gap-3 border-t pt-4 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-2">
          <LightBulbIcon class="h-5 w-5 text-yellow-400" />

          <span class="app-text-muted text-sm">
            Confidence
          </span>

          <span class="font-semibold text-[#00A884]">
            98%
          </span>
        </div>

        <div class="flex items-center gap-2">
          <ClockIcon class="h-5 w-5 text-[#00A884]" />

          <span class="app-text-muted text-sm">
            Updated 21:40
          </span>
        </div>
      </div>
    </div>
  </div>
</template>