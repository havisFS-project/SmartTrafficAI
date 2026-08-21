<script setup>
import { computed, onMounted, onUnmounted, ref } from "vue"
import VueApexCharts from "vue3-apexcharts"

import { isDarkTheme } from "@/utils/theme"

const theme = ref(isDarkTheme() ? "dark" : "light")

const series = [72]

const chartOptions = computed(() => {
  const dark = theme.value === "dark"

  return {
    chart: {
      type: "radialBar",
      background: "transparent",

      animations: {
        enabled: false,
      },
    },

    theme: {
      mode: dark ? "dark" : "light",
    },

    colors: ["#00A884"],

    plotOptions: {
      radialBar: {
        hollow: {
          size: "70%",
        },

        track: {
          background: dark
            ? "#1A2332"
            : "#E2E8F0",
        },

        dataLabels: {
          name: {
            color: dark
              ? "#94A3B8"
              : "#64748B",
          },

          value: {
            color: dark
              ? "#F8FAFC"
              : "#0F172A",

            fontSize: "32px",
            fontWeight: 700,
          },
        },
      },
    },

    labels: ["Density"],
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
        Traffic Density
      </h2>

      <p class="app-text-muted text-sm">
        Current congestion level
      </p>
    </div>

    <VueApexCharts
      type="radialBar"
      height="320"
      :options="chartOptions"
      :series="series"
    />
  </div>
</template>