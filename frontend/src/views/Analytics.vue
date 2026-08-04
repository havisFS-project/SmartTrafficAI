<script setup>

import AnalyticsHeader from "@/components/analytics/AnalyticsHeader.vue"

import AnalyticsStatCard from "@/components/analytics/AnalyticsStatCard.vue"

import {

TruckIcon,

BoltIcon,

CpuChipIcon,

SignalIcon,

} from "@heroicons/vue/24/outline"

</script>

<template>

<div class="space-y-6">

<AnalyticsHeader/>

<div
class="grid
gap-6
sm:grid-cols-1
md:grid-cols-2
xl:grid-cols-4">

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

</div>

</div>

</template>