<script setup>
import {
  ExclamationTriangleIcon,
  TruckIcon,
  CheckCircleIcon,
  ClockIcon,
} from "@heroicons/vue/24/outline"

defineProps({
  alerts: {
    type: Array,
    default: () => [],
  },
})

const getAlertIcon = (alertType) => {
  if (alertType === "Accident") {
    return ExclamationTriangleIcon
  }

  if (alertType === "Traffic Violation") {
    return TruckIcon
  }

  if (alertType === "Road Cleared") {
    return CheckCircleIcon
  }

  return ClockIcon
}

const getAlertColor = (severity) => {
  if (severity === "High") {
    return "text-red-400"
  }

  if (severity === "Medium") {
    return "text-yellow-400"
  }

  return "text-green-400"
}
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6 shadow-lg"
  >
    <div class="mb-6 flex items-center justify-between">
      <div>
        <h2 class="app-text text-xl font-semibold">
          Recent Events
        </h2>

        <p class="app-text-muted mt-1 text-sm">
          Latest traffic events
        </p>
      </div>

      <ClockIcon class="app-text-muted h-6 w-6" />
    </div>

    <div class="space-y-4">
      <div
        v-for="alert in alerts.slice(0, 5)"
        :key="`${alert.camera_id}-${alert.timestamp}`"
        class="app-surface-soft app-border flex items-start gap-4 rounded-xl border p-4 transition-all duration-300 hover:scale-[1.01]"
      >
        <!-- Icon -->
        <div
          class="app-surface flex h-10 w-10 shrink-0 items-center justify-center rounded-xl"
        >
          <component
            :is="getAlertIcon(alert.alert_type)"
            :class="[
              'h-5 w-5',
              getAlertColor(alert.severity),
            ]"
          />
        </div>

        <!-- Event Info -->
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-3">
            <div>
              <p class="app-text font-medium">
                {{ alert.alert_type }}
              </p>

              <p class="app-text-muted mt-1 text-sm">
                {{ alert.message }}
              </p>
            </div>

            <span
              :class="[
                'shrink-0 rounded-lg px-2.5 py-1 text-xs font-medium',
                alert.severity === 'High'
                  ? 'bg-red-500/10 text-red-400'
                  : alert.severity === 'Medium'
                    ? 'bg-yellow-500/10 text-yellow-400'
                    : 'bg-green-500/10 text-green-400',
              ]"
            >
              {{ alert.severity }}
            </span>
          </div>

          <div class="app-text-muted mt-3 flex items-center gap-3 text-xs">
            <span>{{ alert.camera_id }}</span>
            <span>•</span>
            <span>
              {{ new Date(alert.timestamp).toLocaleString() }}
            </span>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div
        v-if="alerts.length === 0"
        class="app-surface-soft rounded-xl px-4 py-8 text-center"
      >
        <p class="app-text-muted text-sm">
          No recent events.
        </p>
      </div>
    </div>
  </div>
</template>