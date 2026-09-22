<script setup>
import { computed } from "vue"

import {
  SparklesIcon,
  LightBulbIcon,
  ClockIcon,
  CheckCircleIcon,
} from "@heroicons/vue/24/outline"

const props = defineProps({
  trafficData: {
    type: Object,
    default: null,
  },

  prediction: {
    type: Object,
    default: null,
  },
})


const formatTime = (timestamp) => {
  if (!timestamp) {
    return "-"
  }

  return new Date(timestamp).toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  })
}


const riskLevel = computed(() => {
  if (!props.prediction) {
    return "Unknown"
  }

  if (props.prediction.predicted_density === "High") {
    return "High Risk"
  }

  if (props.prediction.predicted_density === "Medium") {
    return "Medium Risk"
  }

  return "Low Risk"
})


const riskClass = computed(() => {
  if (riskLevel.value === "High Risk") {
    return "bg-red-500/10 text-red-400"
  }

  if (riskLevel.value === "Medium Risk") {
    return "bg-yellow-500/10 text-yellow-400"
  }

  if (riskLevel.value === "Low Risk") {
    return "bg-green-500/10 text-green-400"
  }

  return "bg-gray-500/10 text-gray-400"
})


const speedChange = computed(() => {
  if (
    !props.trafficData ||
    !props.prediction
  ) {
    return null
  }

  return (
    props.prediction.predicted_speed
    - props.trafficData.average_speed
  )
})


const insightTitle = computed(() => {
  if (!props.prediction) {
    return "Prediction data is unavailable"
  }

  if (
    props.prediction.predicted_density === "High"
    && speedChange.value < 0
  ) {
    return "Traffic is predicted to become more congested"
  }

  if (
    props.prediction.predicted_vehicle_count
    > props.trafficData.vehicle_count
  ) {
    return "Vehicle volume is expected to increase"
  }

  return "Traffic conditions are expected to remain relatively stable"
})


const recommendations = computed(() => {
  if (!props.prediction || !props.trafficData) {
    return []
  }

  const result = []

  if (props.prediction.predicted_density === "High") {
    result.push("Monitor the affected traffic corridor")
  }

  if (speedChange.value < 0) {
    result.push("Prepare traffic management response")
  }

  if (
    props.prediction.predicted_vehicle_count
    > props.trafficData.vehicle_count
  ) {
    result.push("Review alternative route capacity")
  }

  if (result.length === 0) {
    result.push("Continue normal traffic monitoring")
  }

  return result.slice(0, 3)
})


const forecastTime = computed(() => {
  return formatTime(props.prediction?.timestamp)
})


const forecastHorizon = computed(() => {
  if (!props.prediction) {
    return "-"
  }

  return `+${props.prediction.forecast_horizon_minutes} min`
})
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
            {{ insightTitle }}
          </p>

          <p
            v-if="prediction"
            class="app-text-muted mt-2"
          >
            Forecast for

            <span class="app-text font-medium">
              {{ forecastTime }}
            </span>
          </p>

          <p
            v-if="prediction && trafficData"
            class="app-text-muted mt-1 text-sm"
          >
            Speed:
            {{ trafficData.average_speed }}
            km/h
            →

            <span class="app-text font-medium">
              {{ prediction.predicted_speed }}
              km/h
            </span>
          </p>
        </div>

        <span
          class="shrink-0 rounded-full px-3 py-1 text-xs font-semibold"
          :class="riskClass"
        >
          {{ riskLevel }}
        </span>
      </div>


      <!-- Recommendation -->
      <div
        v-if="recommendations.length"
        class="mt-6"
      >
        <p
          class="app-text-muted mb-3 text-xs font-semibold uppercase tracking-wider"
        >
          Suggested Actions
        </p>

        <div class="space-y-3">
          <div
            v-for="recommendation in recommendations"
            :key="recommendation"
            class="flex items-center gap-3"
          >
            <CheckCircleIcon
              class="h-5 w-5 text-[#00A884]"
            />

            <span class="app-text-muted">
              {{ recommendation }}
            </span>
          </div>
        </div>
      </div>


      <!-- Empty State -->
      <div
        v-else
        class="mt-6 rounded-xl bg-black/5 px-4 py-5 text-center dark:bg-white/5"
      >
        <p class="app-text-muted text-sm">
          No prediction data available.
        </p>
      </div>


      <!-- Footer -->
      <div
        class="app-border mt-6 flex flex-col gap-3 border-t pt-4 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-2">
          <LightBulbIcon
            class="h-5 w-5 text-yellow-400"
          />

          <span class="app-text-muted text-sm">
            Forecast Horizon
          </span>

          <span class="font-semibold text-[#00A884]">
            {{ forecastHorizon }}
          </span>
        </div>

        <div
          v-if="prediction"
          class="flex items-center gap-2"
        >
          <ClockIcon
            class="h-5 w-5 text-[#00A884]"
          />

          <span class="app-text-muted text-sm">
            {{ prediction.camera_id }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>