<script setup>
import { computed, ref } from "vue"
import VueApexCharts from "vue3-apexcharts"

import { isDarkTheme } from "@/utils/theme"

const themeVersion = ref(0)

const series = [
  {
    name: "Vehicles",
    data: [120, 180, 240, 300, 260, 420, 510],
  },
]

const chartOptions = computed(() => {
  themeVersion.value

  const dark = isDarkTheme()

  return {
    chart: {
      type: "line",
      toolbar: {
        show: false,
      },
      zoom: {
        enabled: false,
      },
      background: "transparent",
      animations: {
        enabled: true,
        speed: 500,
      },
    },

    theme: {
      mode: dark ? "dark" : "light",
    },

    colors: ["#00A884"],

    stroke: {
      curve: "smooth",
      width: 4,
    },

    xaxis: {
      categories: [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun",
      ],

      labels: {
        style: {
          colors: dark ? "#94A3B8" : "#64748B",
        },
      },
    },

    yaxis: {
      labels: {
        style: {
          colors: dark ? "#94A3B8" : "#64748B",
        },
      },
    },

    grid: {
      borderColor: dark ? "#334155" : "#E2E8F0",
    },

    tooltip: {
      theme: dark ? "dark" : "light",
    },
  }
})
</script>

<template>
  <div
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Traffic Trend
      </h2>

      <p class="app-text-muted text-sm">
        Vehicle count in the last 7 days
      </p>
    </div>

    <VueApexCharts
      type="line"
      height="330"
      :options="chartOptions"
      :series="series"
    />
  </div>
</template>