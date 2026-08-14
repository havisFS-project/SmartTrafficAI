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
    class="rounded-2xl border border-white/5 bg-[#232D3F] p-6"
  >
    <div class="mb-6">
      <h2 class="text-xl font-semibold text-white">
        Application
      </h2>

      <p class="mt-1 text-sm text-gray-400">
        Configure SmartTrafficAI application behavior
      </p>
    </div>

    <div class="space-y-4">
      <!-- Auto Refresh -->
      <div
        class="flex items-center justify-between gap-4 rounded-xl bg-[#1B2435] p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <ArrowPathIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Auto Refresh
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              Automatically refresh dashboard data
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="autoRefresh"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/40"
          :class="
            autoRefresh
              ? 'bg-[#008170]'
              : 'bg-[#475569]'
          "
          @click="autoRefresh = !autoRefresh"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="
              autoRefresh
                ? 'translate-x-5'
                : 'translate-x-0'
            "
          />
        </button>
      </div>

      <!-- Realtime Monitoring -->
      <div
        class="flex items-center justify-between gap-4 rounded-xl bg-[#1B2435] p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <VideoCameraIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Realtime Monitoring
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              Enable realtime traffic and CCTV updates
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="realtimeMonitoring"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/40"
          :class="
            realtimeMonitoring
              ? 'bg-[#008170]'
              : 'bg-[#475569]'
          "
          @click="
            realtimeMonitoring = !realtimeMonitoring
          "
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

      <!-- Default Camera -->
      <div
        class="flex flex-col gap-4 rounded-xl bg-[#1B2435] p-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <VideoCameraIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Default Camera
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              Camera shown first on the CCTV page
            </p>
          </div>
        </div>

        <select
          v-model="defaultCamera"
          class="rounded-xl border border-white/10 bg-[#232D3F] px-4 py-2.5 text-sm text-white outline-none transition focus:border-[#00A884]"
        >
          <option>Camera 01</option>
          <option>Camera 02</option>
          <option>Camera 03</option>
          <option>Camera 04</option>
        </select>
      </div>

      <!-- Refresh Interval -->
      <div
        class="flex flex-col gap-4 rounded-xl bg-[#1B2435] p-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <ClockIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Refresh Interval
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              How often dashboard data is refreshed
            </p>
          </div>
        </div>

        <select
          v-model="refreshInterval"
          class="rounded-xl border border-white/10 bg-[#232D3F] px-4 py-2.5 text-sm text-white outline-none transition focus:border-[#00A884]"
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