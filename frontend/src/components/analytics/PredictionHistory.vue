<script setup>
defineProps({
  predictions: {
    type: Array,
    default: () => [],
  },
})

const getDensityClass = (density) => {
  if (density === "High") {
    return "bg-red-500/10 text-red-400"
  }

  if (density === "Medium") {
    return "bg-yellow-500/10 text-yellow-400"
  }

  if (density === "Low") {
    return "bg-green-500/10 text-green-400"
  }

  return "bg-gray-500/10 text-gray-400"
}

const formatTime = (timestamp) => {
  return new Date(timestamp).toLocaleString([], {
    hour: "2-digit",
    minute: "2-digit",
  })
}
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6 shadow-lg"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        AI Prediction History
      </h2>

      <p class="app-text-muted text-sm">
        Latest AI traffic predictions
      </p>
    </div>

    <div class="space-y-4">
      <div
        v-for="prediction in predictions.slice(0, 5)"
        :key="`${prediction.camera_id}-${prediction.timestamp}`"
        class="app-surface-soft app-border rounded-xl border p-4"
      >
        <div class="flex items-center justify-between gap-4">
          <div>
            <p class="app-text font-medium">
              {{ prediction.camera_id }}
            </p>

            <p class="app-text-muted text-sm">
              {{ formatTime(prediction.timestamp) }}
            </p>
          </div>

          <span
            class="rounded-full px-3 py-1 text-xs font-semibold"
            :class="getDensityClass(prediction.predicted_density)"
          >
            {{ prediction.predicted_density }}
          </span>
        </div>

        <div class="mt-3 flex items-center gap-4">
          <div>
            <span class="app-text-muted text-sm">
              Vehicles
            </span>

            <span class="ml-2 app-text text-sm font-semibold">
              {{ prediction.predicted_vehicle_count }}
            </span>
          </div>

          <div>
            <span class="app-text-muted text-sm">
              Speed
            </span>

            <span class="ml-2 text-sm font-semibold text-[#00A884]">
              {{ prediction.predicted_speed }} km/h
            </span>
          </div>

          <div>
            <span class="app-text-muted text-sm">
              Forecast
            </span>

            <span class="ml-2 app-text text-sm font-semibold">
              +{{ prediction.forecast_horizon_minutes }} min
            </span>
          </div>
        </div>
      </div>

      <div
        v-if="predictions.length === 0"
        class="app-surface-soft rounded-xl px-4 py-8 text-center"
      >
        <p class="app-text-muted text-sm">
          No prediction data available.
        </p>
      </div>
    </div>
  </div>
</template>