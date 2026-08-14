<script setup>
import { ref } from "vue"
import {
  BellAlertIcon,
  ExclamationTriangleIcon,
  SparklesIcon,
  ServerIcon,
  EnvelopeIcon,
} from "@heroicons/vue/24/outline"

const notifications = ref([
  {
    id: "traffic-alerts",
    title: "Traffic Alerts",
    description: "Receive notifications about traffic congestion.",
    enabled: true,
    icon: BellAlertIcon,
  },
  {
    id: "accident-detection",
    title: "Accident Detection",
    description: "Get alerts when AI detects a possible accident.",
    enabled: true,
    icon: ExclamationTriangleIcon,
  },
  {
    id: "ai-predictions",
    title: "AI Predictions",
    description: "Receive updates about traffic predictions.",
    enabled: true,
    icon: SparklesIcon,
  },
  {
    id: "system-status",
    title: "System Status",
    description: "Receive alerts when a service changes status.",
    enabled: true,
    icon: ServerIcon,
  },
  {
    id: "email-notifications",
    title: "Email Notifications",
    description: "Receive important alerts through email.",
    enabled: false,
    icon: EnvelopeIcon,
  },
])
</script>

<template>
  <section
    class="rounded-2xl border border-white/5 bg-[#232D3F] p-6"
  >
    <div class="mb-6">
      <h2 class="text-xl font-semibold text-white">
        Notifications
      </h2>

      <p class="mt-1 text-sm text-gray-400">
        Choose which notifications you want to receive
      </p>
    </div>

    <div class="divide-y divide-white/5">
      <div
        v-for="notification in notifications"
        :key="notification.id"
        class="flex items-center justify-between gap-4 py-5 first:pt-0 last:pb-0"
      >
        <div class="flex items-center gap-4">
          <div
            class="rounded-xl bg-[#005B41]/20 p-3"
          >
            <component
              :is="notification.icon"
              class="h-6 w-6 text-[#00A884]"
            />
          </div>

          <div>
            <h3 class="font-medium text-white">
              {{ notification.title }}
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              {{ notification.description }}
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="notification.enabled"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/40"
          :class="
            notification.enabled
              ? 'bg-[#008170]'
              : 'bg-[#475569]'
          "
          @click="notification.enabled = !notification.enabled"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="
              notification.enabled
                ? 'translate-x-5'
                : 'translate-x-0'
            "
          />
        </button>
      </div>
    </div>
  </section>
</template>