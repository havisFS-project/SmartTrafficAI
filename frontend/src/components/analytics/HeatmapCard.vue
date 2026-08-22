<script setup>
import {
  MapIcon,
  MapPinIcon,
} from "@heroicons/vue/24/outline"

const hotspots = [
  {
    location: "Highway KM 12",
    status: "Heavy",
    color: "bg-red-500/10 text-red-400",
  },
  {
    location: "City Center",
    status: "Medium",
    color: "bg-yellow-500/10 text-yellow-400",
  },
  {
    location: "Airport Road",
    status: "Normal",
    color: "bg-green-500/10 text-green-400",
  },
]
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6 shadow-lg"
  >
    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="app-text text-xl font-semibold">
          Traffic Heatmap
        </h2>

        <p class="app-text-muted text-sm">
          Congestion hotspot overview
        </p>
      </div>

      <MapIcon class="h-7 w-7 text-[#00A884]" />
    </div>

    <!-- Map Preview -->
    <div
      class="app-surface-soft app-border flex h-56 items-center justify-center rounded-xl border border-dashed"
    >
      <div class="text-center">
        <MapPinIcon
          class="mx-auto mb-3 h-10 w-10 text-[#00A884]"
        />

        <p class="app-text font-medium">
          Interactive Map
        </p>

        <p class="app-text-muted text-sm">
          Leaflet Map Coming Soon
        </p>
      </div>
    </div>

    <!-- Hotspots -->
    <div class="mt-6 space-y-3">
      <div
        v-for="spot in hotspots"
        :key="spot.location"
        class="app-surface-soft flex items-center justify-between rounded-xl px-4 py-3"
      >
        <div>
          <p class="app-text font-medium">
            {{ spot.location }}
          </p>

          <p class="app-text-muted text-sm">
            Traffic Hotspot
          </p>
        </div>

        <span
          class="rounded-full px-3 py-1 text-xs font-semibold"
          :class="spot.color"
        >
          {{ spot.status }}
        </span>
      </div>
    </div>
  </div>
</template>