<script setup>
const predictions = [
  {
    time: "09:45",
    location: "Highway KM 12",
    status: "Heavy Traffic",
    confidence: "98%",
    statusClass: "bg-red-500/10 text-red-400",
  },
  {
    time: "09:30",
    location: "City Center",
    status: "Normal",
    confidence: "96%",
    statusClass: "bg-green-500/10 text-green-400",
  },
  {
    time: "09:10",
    location: "Airport Road",
    status: "Low Traffic",
    confidence: "95%",
    statusClass: "bg-blue-500/10 text-blue-400",
  },
]
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
        v-for="prediction in predictions"
        :key="prediction.time"
        class="app-surface-soft rounded-xl p-4 transition hover:opacity-90"
      >
        <div class="flex items-center justify-between gap-4">
          <div>
            <p class="app-text font-medium">
              {{ prediction.location }}
            </p>

            <p class="app-text-muted text-sm">
              {{ prediction.time }}
            </p>
          </div>

          <span
            class="rounded-full px-3 py-1 text-xs font-semibold"
            :class="prediction.statusClass"
          >
            {{ prediction.status }}
          </span>
        </div>

        <div class="mt-3">
          <span class="app-text-muted text-sm">
            Confidence
          </span>

          <span class="ml-2 text-sm font-semibold text-[#00A884]">
            {{ prediction.confidence }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>