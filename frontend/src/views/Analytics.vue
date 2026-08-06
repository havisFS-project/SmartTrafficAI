<script setup>
import AnalyticsHeader from "@/components/analytics/AnalyticsHeader.vue"
import AnalyticsToolbar from "@/components/analytics/AnalyticsToolbar.vue"

import AnalyticsStatCard from "@/components/analytics/AnalyticsStatCard.vue"

import TrafficTrendChart from "@/components/analytics/TrafficTrendChart.vue"
import TrafficDensityChart from "@/components/analytics/TrafficDensityChart.vue"

import VehicleDistribution from "@/components/analytics/VehicleDistribution.vue"
import PredictionHistory from "@/components/analytics/PredictionHistory.vue"

import AIInsight from "@/components/analytics/AIInsight.vue"
import HeatmapCard from "@/components/analytics/HeatmapCard.vue"

import {
  TruckIcon,
  BoltIcon,
  CpuChipIcon,
  SignalIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <div class="space-y-6">

    <!-- Header -->

    <AnalyticsHeader />

    <!-- Toolbar -->

    <AnalyticsToolbar />

    <!-- Stat Cards -->

    <section
      class="grid gap-6 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-4"
    >
      <AnalyticsStatCard
        title="Vehicles"
        value="15,284"
        subtitle="+8% Today"
        :icon="TruckIcon"
        color="bg-green-500/10 text-green-400"
      />

      <AnalyticsStatCard
        title="Average Speed"
        value="48 km/h"
        subtitle="Realtime"
        :icon="BoltIcon"
        color="bg-blue-500/10 text-blue-400"
      />

      <AnalyticsStatCard
        title="AI Accuracy"
        value="98.7%"
        subtitle="YOLO v11"
        :icon="CpuChipIcon"
        color="bg-cyan-500/10 text-cyan-400"
      />

      <AnalyticsStatCard
        title="Traffic Density"
        value="Medium"
        subtitle="Current"
        :icon="SignalIcon"
        color="bg-yellow-500/10 text-yellow-400"
      />
    </section>

    <!-- Trend -->

    <section class="grid gap-6 xl:grid-cols-3">

      <div class="xl:col-span-2">
        <TrafficTrendChart />
      </div>

      <TrafficDensityChart />

    </section>

    <!-- Distribution -->

    <section class="grid gap-6 md:grid-cols-2">

      <VehicleDistribution />

      <PredictionHistory />

    </section>

    <!-- AI -->

    <section class="grid gap-6 xl:grid-cols-2">

      <AIInsight />

      <HeatmapCard />

    </section>

  </div>
</template>