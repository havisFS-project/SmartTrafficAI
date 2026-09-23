<script setup>
import {
  MapIcon,
  MapPinIcon,
} from "@heroicons/vue/24/outline"

const props = defineProps({
  hotspots: {
    type: Array,
    default: () => [],
  },
})

const getStatus = (density) => {
  if (density === "High") {
    return "Heavy"
  }

  if (density === "Medium") {
    return "Medium"
  }

  if (density === "Low") {
    return "Normal"
  }

  return "Unknown"
}

const getStatusClass = (density) => {
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
        v-for="spot in props.hotspots"
        :key="spot.camera_id"
        class="app-surface-soft flex items-center justify-between rounded-xl px-4 py-3"
      >
        <div>
          <p class="app-text font-medium">
            {{ spot.location }}
          </p>

          <p class="app-text-muted text-sm">
            {{ spot.camera_id }} · Traffic Hotspot
          </p>
        </div>

        <span
          class="rounded-full px-3 py-1 text-xs font-semibold"
          :class="getStatusClass(spot.density)"
        >
          {{ getStatus(spot.density) }}
        </span>
      </div>

      <div
        v-if="props.hotspots.length === 0"
        class="app-surface-soft rounded-xl px-4 py-6 text-center"
      >
        <p class="app-text-muted text-sm">
          No traffic hotspot data available.
        </p>
      </div>
    </div>
  </div>
</template>