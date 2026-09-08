<script setup>
import { computed, ref, onMounted, onUnmounted } from "vue"
import VueApexCharts from "vue3-apexcharts"

import { isDarkTheme } from "@/utils/theme"

const props = defineProps({
  trafficData: {
    type: Array,
    default: () => [],
  },
})

const themeVersion = ref(0)


const series = computed(() => {
  return [
    {
      name: "Vehicles",
      data: props.trafficData.map(
        (item) => item.vehicle_count,
      ),
    },
  ]
})


const categories = computed(() => {
  return props.trafficData.map((item) => {
    return new Date(item.timestamp).toLocaleTimeString(
      [],
      {
        hour: "2-digit",
        minute: "2-digit",
      },
    )
  })
})


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
        enabled: false,
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
      categories: categories.value,

      labels: {
        style: {
          colors: dark ? "#94A3B8" : "#64748B",
        },
      },
    },

    yaxis: {
      title: {
        text: "Vehicles",
        style: {
          color: dark ? "#94A3B8" : "#64748B",
        },
      },

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


const handleThemeChange = () => {
  themeVersion.value++
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
        Traffic Trend
      </h2>

      <p class="app-text-muted text-sm">
        Vehicle count based on recorded traffic data
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