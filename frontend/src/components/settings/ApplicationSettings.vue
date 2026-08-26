<script setup>
import { ref } from "vue"
import {
  ArrowPathIcon,
  VideoCameraIcon,
  ClockIcon,
} from "@heroicons/vue/24/outline"

const autoRefresh = ref(true)
const realtimeMonitoring = ref(true)
const defaultCamera = ref("Camera 01")
const refreshInterval = ref("30")
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Application
      </h2>

      <p class="app-text-muted mt-1 text-sm">
        Configure SmartTrafficAI application behavior
      </p>
    </div>

    <div class="space-y-4">
      <div
        class="app-surface-soft flex items-center justify-between gap-4 rounded-xl p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <ArrowPathIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Auto Refresh
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              Automatically refresh dashboard data
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="autoRefresh"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/30"
          :class="autoRefresh ? 'bg-[#008170]' : 'app-toggle-off'"
          @click="autoRefresh = !autoRefresh"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="autoRefresh ? 'translate-x-5' : 'translate-x-0'"
          />
        </button>
      </div>

      <div
        class="app-surface-soft flex items-center justify-between gap-4 rounded-xl p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <VideoCameraIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Realtime Monitoring
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              Enable realtime traffic and CCTV updates
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="realtimeMonitoring"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/30"
          :class="
            realtimeMonitoring
              ? 'bg-[#008170]'
              : 'app-toggle-off'
          "
          @click="realtimeMonitoring = !realtimeMonitoring"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="
              realtimeMonitoring
                ? 'translate-x-5'
                : 'translate-x-0'
            "
          />
        </button>
      </div>

      <div
        class="app-surface-soft flex flex-col gap-4 rounded-xl p-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <VideoCameraIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Default Camera
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              Camera shown first on the CCTV page
            </p>
          </div>
        </div>

        <select
          v-model="defaultCamera"
          class="app-surface app-text app-border rounded-xl border px-4 py-2.5 text-sm outline-none transition focus:border-[#00A884]"
        >
          <option>Camera 01</option>
          <option>Camera 02</option>
          <option>Camera 03</option>
          <option>Camera 04</option>
        </select>
      </div>

      <div
        class="app-surface-soft flex flex-col gap-4 rounded-xl p-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <ClockIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Refresh Interval
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              How often dashboard data is refreshed
            </p>
          </div>
        </div>

        <select
          v-model="refreshInterval"
          class="app-surface app-text app-border rounded-xl border px-4 py-2.5 text-sm outline-none transition focus:border-[#00A884]"
        >
          <option value="15">15 seconds</option>
          <option value="30">30 seconds</option>
          <option value="60">1 minute</option>
          <option value="300">5 minutes</option>
        </select>
      </div>
    </div>
  </section>
</template>