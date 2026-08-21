<script setup>
import { computed, onMounted, onUnmounted, ref } from "vue"
import VueApexCharts from "vue3-apexcharts"

import { isDarkTheme } from "@/utils/theme"

const theme = ref(isDarkTheme() ? "dark" : "light")

const series = [42, 36, 12, 7, 3]

const labels = [
  "Car",
  "Motorcycle",
  "Truck",
  "Bus",
  "Others",
]

const chartOptions = computed(() => {
  const dark = theme.value === "dark"

  return {
    chart: {
      type: "donut",
      background: "transparent",

      animations: {
        enabled: false,
      },
    },

    theme: {
      mode: dark ? "dark" : "light",
    },

    labels,

    colors: [
      "#00A884",
      "#3B82F6",
      "#F59E0B",
      "#EF4444",
      "#8B5CF6",
    ],

    legend: {
      position: "bottom",

      labels: {
        colors: dark
          ? "#CBD5E1"
          : "#475569",
      },
    },

    dataLabels: {
      enabled: false,
    },

    stroke: {
      show: false,
    },

    tooltip: {
      theme: dark
        ? "dark"
        : "light",
    },
  }
})

const handleThemeChange = (event) => {
  theme.value = event.detail
}

onMounted(() => {
  window.addEventListener(
    "theme-changed",
    handleThemeChange,
  )
})

onUnmounted(() => {
  window.removeEventListener(
    "theme-changed",
    handleThemeChange,
  )
})
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Vehicle Distribution
      </h2>

      <p class="app-text-muted text-sm">
        Vehicle composition today
      </p>
    </div>

    <VueApexCharts
      type="donut"
      height="330"
      :options="chartOptions"
      :series="series"
    />
  </div>
</template>