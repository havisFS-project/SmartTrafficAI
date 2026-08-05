<script setup>
import VueApexCharts from "vue3-apexcharts"

const series = [
  {
    name: "Vehicles",
    data: [120, 180, 240, 300, 260, 420, 510],
  },
]

const chartOptions = {

  chart: {
    toolbar: {
      show: false,
    },
    zoom: {
      enabled: false,
    },
    background: "transparent",
  },

  theme: {
    mode: "dark",
  },

  stroke: {
    curve: "smooth",
    width: 4,
  },

  colors: ["#00A884"],

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
        colors: "#94A3B8",
      },
    },

  },

  yaxis: {

    labels: {

      style: {
        colors: "#94A3B8",
      },

    },

  },

  grid: {

    borderColor: "#334155",

  },

}
</script>

<template>

<div
class="rounded-2xl border border-white/5 bg-[#232D3F] p-6">

<div class="mb-6">

<h2 class="text-xl font-semibold text-white">

Traffic Trend

</h2>

<p class="text-sm text-gray-400">

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