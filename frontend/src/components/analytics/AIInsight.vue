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
  <div class="rounded-2xl border border-white/5 bg-[#232D3F] p-6">
    <!-- Header -->

    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="text-2xl font-bold text-white">
          AI Insight
        </h2>

        <p class="text-sm text-gray-400">
          Realtime traffic intelligence
        </p>
      </div>

      <SparklesIcon class="h-7 w-7 text-[#00A884]" />
    </div>

    <!-- Main Prediction -->

    <div class="rounded-xl bg-[#1B2435] p-5">
      <h3 class="text-lg font-semibold text-white">
        Traffic is predicted to increase
      </h3>

      <p class="mt-2 text-gray-400">
        Expected between
        <span class="font-medium text-white">
          17:00 - 18:00
        </span>
      </p>

      <!-- Recommendation -->

      <div class="mt-6">
        <p class="mb-3 text-sm font-semibold uppercase tracking-wider text-gray-400">
          Recommendation
        </p>

        <div class="space-y-3">
          <div
            v-for="item in recommendations"
            :key="item"
            class="flex items-center gap-3"
          >
            <CheckCircleIcon class="h-5 w-5 text-[#00A884]" />

            <span class="text-gray-300">
              {{ item }}
            </span>
          </div>
        </div>
      </div>

      <!-- Footer -->

      <div class="mt-8 flex items-center justify-between border-t border-white/10 pt-4">

        <div class="flex items-center gap-2">
          <LightBulbIcon class="h-5 w-5 text-yellow-400" />

          <span class="text-sm text-gray-300">
            Confidence
          </span>

          <span class="font-bold text-[#00A884]">
            98%
          </span>
        </div>

        <div class="flex items-center gap-2">
          <ClockIcon class="h-5 w-5 text-[#00A884]" />

          <span class="text-sm text-gray-400">
            Updated 21:40
          </span>
        </div>

      </div>
    </div>
  </div>
</template>