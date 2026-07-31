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
</script>

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

<!-- Welcome -->

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

<!-- Statistics -->

</div>

</template>