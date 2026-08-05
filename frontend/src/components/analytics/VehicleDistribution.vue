<script setup>
import VueApexCharts from "vue3-apexcharts"

const series = [42, 36, 12, 7, 3]

const chartOptions = {
  chart: {
    type: "donut",
    background: "transparent",

    animations: {
      enabled: false,
    },
  },

  theme: {
    mode: "dark",
  },

  labels: [
    "Car",
    "Motorcycle",
    "Truck",
    "Bus",
    "Others",
  ],

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
      colors: "#CBD5E1",
    },
  },

  dataLabels: {
    enabled: false,
  },

  stroke: {
    show: false,
  },
}
</script>

<template>

<div class="rounded-2xl border border-white/5 bg-[#232D3F] p-6">

    <div class="mb-6">

        <h2 class="text-xl font-semibold text-white">
            Vehicle Distribution
        </h2>

        <p class="text-sm text-gray-400">
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