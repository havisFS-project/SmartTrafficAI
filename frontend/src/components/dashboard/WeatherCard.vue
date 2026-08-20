<script setup>
import { CloudIcon } from "@heroicons/vue/24/outline"
</script>

<template>
  <div
    class="app-surface app-border h-full rounded-2xl border p-6 shadow-lg"
  >
    <div class="flex items-center justify-between">
      <div>
        <h2 class="app-text text-xl font-semibold">
          Weather
        </h2>

        <p class="app-text-muted text-sm">
          Current Condition
        </p>
      </div>

      <CloudIcon class="h-7 w-7 text-sky-400" />
    </div>

    <div class="mt-8 text-center">
      <p class="app-text text-5xl font-bold">
        28°
      </p>

      <p class="app-text-muted mt-2">
        Sunny
      </p>
    </div>

    <div class="mt-8 space-y-3 text-sm">
      <div class="flex justify-between">
        <span class="app-text-muted">
          Humidity
        </span>

        <span class="app-text">
          71%
        </span>
      </div>

      <div class="flex justify-between">
        <span class="app-text-muted">
          Wind
        </span>

        <span class="app-text">
          12 km/h
        </span>
      </div>

      <div class="flex justify-between">
        <span class="app-text-muted">
          Visibility
        </span>

        <span class="app-text">
          5 km
        </span>
      </div>
    </div>
  </div>
</template>