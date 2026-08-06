<script setup>
import {
  MapIcon,
  MapPinIcon,
} from "@heroicons/vue/24/outline"

const hotspots = [
  {
    location: "Highway KM 12",
    status: "Heavy",
    color: "bg-red-500",
  },
  {
    location: "City Center",
    status: "Medium",
    color: "bg-yellow-500",
  },
  {
    location: "Airport Road",
    status: "Normal",
    color: "bg-green-500",
  },
]
</script>

<template>
  <div class="rounded-2xl border border-white/5 bg-[#232D3F] p-6">

    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="text-xl font-semibold text-white">
          Traffic Heatmap
        </h2>

        <p class="text-sm text-gray-400">
          Congestion hotspot overview
        </p>
      </div>

      <MapIcon class="h-7 w-7 text-[#00A884]" />
    </div>

    <!-- Map Preview -->

    <div
      class="flex h-56 items-center justify-center rounded-xl border border-dashed border-white/10 bg-[#1B2435]"
    >
      <div class="text-center">

        <MapPinIcon class="mx-auto mb-3 h-10 w-10 text-[#00A884]" />

        <p class="font-medium text-white">
          Interactive Map
        </p>

        <p class="text-sm text-gray-400">
          Google Maps / Leaflet Coming Soon
        </p>

      </div>
    </div>

    <!-- Hotspot -->

    <div class="mt-6 space-y-3">

      <div
        v-for="spot in hotspots"
        :key="spot.location"
        class="flex items-center justify-between rounded-lg bg-[#1B2435] px-4 py-3"
      >
        <div>
          <p class="font-medium text-white">
            {{ spot.location }}
          </p>

          <p class="text-sm text-gray-400">
            Traffic Hotspot
          </p>
        </div>

        <span
          :class="spot.color"
          class="rounded-full px-3 py-1 text-xs font-semibold text-white"
        >
          {{ spot.status }}
        </span>

      </div>

    </div>

  </div>
</template>