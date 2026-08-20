<script setup>
import {
  CpuChipIcon,
  ArrowTrendingUpIcon,
} from "@heroicons/vue/24/outline"

</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6 shadow-lg"
  >
    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="app-text text-xl font-semibold">
          AI Prediction
        </h2>

        <p class="app-text-muted text-sm">
          LSTM Traffic Forecast
        </p>
      </div>

      <div class="rounded-xl bg-[#005B41]/20 p-3">
        <CpuChipIcon class="h-6 w-6 text-[#00A884]" />
      </div>
    </div>

    <div class="space-y-5">
      <div>
        <p class="app-text-muted text-sm">
          Traffic Condition
        </p>

        <h1 class="mt-2 text-3xl font-bold text-yellow-400">
          Medium
        </h1>
      </div>

      <div>
        <div class="mb-2 flex justify-between">
          <span class="app-text-muted">
            Confidence
          </span>

          <span class="app-text font-medium">
            98.7%
          </span>
        </div>

        <div class="h-3 overflow-hidden rounded-full bg-gray-200 dark:bg-[#1A2332]">
          <div
            class="h-full w-[98%] rounded-full bg-[#008170]"
          />
        </div>
      </div>

      <div
        class="app-surface-soft rounded-xl p-4"
      >
        <div class="flex items-center gap-3">
          <ArrowTrendingUpIcon class="h-6 w-6 text-green-400" />

          <div>
            <p class="app-text font-medium">
              Prediction
            </p>

            <p class="app-text-muted text-sm">
              Traffic expected to increase in
              15 minutes.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>