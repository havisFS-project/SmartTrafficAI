<script setup>
import {
  ExclamationTriangleIcon,
  TruckIcon,
  CheckCircleIcon,
  ClockIcon,
} from "@heroicons/vue/24/outline"

const events = [
  {
    title: "Accident Detected",
    location: "Highway KM 12",
    time: "2 min ago",
    color: "text-red-400",
    icon: ExclamationTriangleIcon,
  },
  {
    title: "Heavy Traffic",
    location: "City Center",
    time: "5 min ago",
    color: "text-yellow-400",
    icon: TruckIcon,
  },
  {
    title: "Road Cleared",
    location: "South Ring Road",
    time: "12 min ago",
    color: "text-green-400",
    icon: CheckCircleIcon,
  },
]
</script>

<template>

<div
  class="app-surface app-border rounded-2xl border p-6 shadow-lg"
>
  <div class="mb-6 flex items-center justify-between">
    <h2 class="app-text text-xl font-semibold">
      Recent Events
    </h2>

    <ClockIcon class="app-text-muted h-6 w-6" />
  </div>

  <div class="space-y-4">
    <div
      v-for="event in events"
      :key="event.title"
      class="app-surface-soft flex gap-4 rounded-xl p-4 transition hover:opacity-90"
    >
      <component
        :is="event.icon"
        :class="['h-6 w-6', event.color]"
      />

      <div>
        <p class="app-text font-medium">
          {{ event.title }}
        </p>

        <p class="app-text-muted text-sm">
          {{ event.location }}
        </p>

        <p class="app-text-muted mt-1 text-xs">
          {{ event.time }}
        </p>
      </div>
    </div>
  </div>
</div>

</template>