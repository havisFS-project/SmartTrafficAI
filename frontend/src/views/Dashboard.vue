<script setup>
import {
  BaseStatCard,
} from "@/components/ui"

import {
  TruckIcon,
  VideoCameraIcon,
  CpuChipIcon,
  SignalIcon,
} from "@heroicons/vue/24/outline"
import LiveCameraCard from "@/components/dashboard/LiveCameraCard.vue"
import AIPredictionCard from "@/components/dashboard/AIPredictionCard.vue"
import RecentEventsCard from "@/components/dashboard/RecentEventsCard.vue"
import WeatherCard from "@/components/dashboard/WeatherCard.vue"
import SystemStatusCard from "@/components/dashboard/SystemStatusCard.vue"
</script>

<!-- Welcome -->

<template>

<div class="space-y-8">

  <section>
    
    <h1
      class="text-3xl font-bold text-white">

      Good Evening, Havis 👋

    </h1>
    
    <p
      class="mt-2 text-gray-400">

      Welcome back to SmartTrafficAI Dashboard.

      Monitor your traffic system in real time.

    </p>

  </section>

<!-- Statistics -->

<section>

<div
class="grid grid-cols-4 gap-6">

<BaseStatCard
title="Vehicle Count"
value="15,284"
subtitle="+8% Today"
:icon="TruckIcon"
/>

<BaseStatCard
title="Active CCTV"
value="48"
subtitle="Online"
:icon="VideoCameraIcon"
color="blue"
/>

<BaseStatCard
title="AI Accuracy"
value="98.7%"
subtitle="Excellent"
:icon="CpuChipIcon"
/>

<BaseStatCard
title="Traffic Density"
value="Medium"
subtitle="Realtime"
:icon="SignalIcon"
color="yellow"
/>

</div>

</section>

<section class="grid grid-cols-3 gap-6">

  <!-- Analytics -->
  <BaseCard class="col-span-2">

    <div class="mb-6 flex items-center justify-between">

      <div>

        <h2 class="text-xl font-semibold text-white">
          Traffic Analytics
        </h2>

        <p class="mt-1 text-sm text-gray-400">
          Vehicle traffic trend for the last 24 hours
        </p>

      </div>

      <BaseBadge>
        Live
      </BaseBadge>

    </div>

    <div
      class="flex h-80 items-center justify-center rounded-xl border border-dashed border-gray-700 bg-[#1A2332]"
    >
      <p class="text-gray-500">
        Chart Coming Soon
      </p>
    </div>

  </BaseCard>

  <!-- Alerts -->

  <BaseCard>

    <h2 class="text-xl font-semibold text-white">
      Recent Alerts
    </h2>

    <p class="mb-6 mt-1 text-sm text-gray-400">
      Latest traffic events
    </p>

    <div class="space-y-4">

      <div class="rounded-xl bg-red-500/10 p-4">
        <p class="font-medium text-red-400">
          🚨 Accident Detected
        </p>

        <p class="mt-1 text-sm text-gray-400">
          Highway KM 12
        </p>
      </div>

      <div class="rounded-xl bg-yellow-500/10 p-4">
        <p class="font-medium text-yellow-400">
          ⚠ Heavy Traffic
        </p>

        <p class="mt-1 text-sm text-gray-400">
          City Center
        </p>
      </div>

      <div class="rounded-xl bg-green-500/10 p-4">
        <p class="font-medium text-green-400">
          ✅ Road Clear
        </p>

        <p class="mt-1 text-sm text-gray-400">
          South Ring Road
        </p>
      </div>

    </div>

  </BaseCard>

</section>

<section class="mt-6 grid grid-cols-3 gap-6">

  <div class="col-span-2">

    <LiveCameraCard />

  </div>

  <AIPredictionCard />

</section>

<section class="mt-6 grid grid-cols-3 gap-6">

    <RecentEventsCard/>

    <WeatherCard/>

    <SystemStatusCard/>

</section>

</div>

</template>