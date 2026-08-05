<script setup>
import VueApexCharts from "vue3-apexcharts"

const series = [72]

const chartOptions = {

  chart: {
    type: "radialBar",
    background: "transparent",

     animations: {
        enabled: false,
        speed: 500,
        animateGradually: {
            enabled: false,
        },
        
        dynamicAnimation: {
            enabled: true,
            speed: 300,
        },
     }
    },

  theme: {
    mode: "dark",
  },

  colors: ["#00A884"],

  plotOptions: {
    radialBar: {

      hollow: {
        size: "70%",
      },

      dataLabels: {

        name: {
          color: "#94A3B8",
        },

        value: {
          color: "#ffffff",
          fontSize: "32px",
          fontWeight: 700,
        },

      },

    },

  },

  labels: ["Density"],

}
</script>

<template>

<div class="rounded-2xl border border-white/5 bg-[#232D3F] p-6">

    <div class="mb-6">

        <h2 class="text-xl font-semibold text-white">

            Traffic Density

        </h2>

        <p class="text-sm text-gray-400">

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