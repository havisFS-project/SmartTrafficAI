<script setup>
import { computed, onMounted, ref } from "vue"

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

import {
  getCameras,
  getPredictions,
  getTrafficData,
  getTrafficStatistics,
} from "@/services/api"

const cameras = ref([])

const trafficData = ref([])

const trafficStats = ref({
  total_records: 0,
  total_vehicles: 0,
  average_speed: 0,
  density: {},
})

const trafficLoading = ref(false)
const trafficError = ref("")


const loadAnalyticsData = async () => {
  trafficLoading.value = true
  trafficError.value = ""

  try {
    const [
      cameraResponse,
      trafficResponse,
      statisticsResponse,
    ] = await Promise.all([
      getCameras(),
      getTrafficData(),
      getTrafficStatistics(),
    ])

    cameras.value = cameraResponse.data
    trafficData.value = trafficResponse.data
    trafficStats.value = statisticsResponse
  } catch (error) {
    trafficError.value = error.message
  } finally {
    trafficLoading.value = false
  }
}

const trafficHotspots = computed(() => {
  if (!trafficData.value.length) {
    return []
  }

  const cameraMap = new Map(
    cameras.value.map((camera) => [
      camera.camera_id,
      camera,
    ]),
  )

  const latestByCamera = new Map()

  for (const record of trafficData.value) {
    const existing = latestByCamera.get(record.camera_id)

    if (
      !existing ||
      new Date(record.timestamp) > new Date(existing.timestamp)
    ) {
      latestByCamera.set(record.camera_id, record)
    }
  }

  return Array.from(latestByCamera.values()).map(
    (record) => {
      const camera = cameraMap.get(record.camera_id)

      return {
        camera_id: record.camera_id,
        location:
          camera?.location ?? record.camera_id,
        density: record.density ?? "Unknown",
        latitude: camera?.latitude ?? null,
        longitude: camera?.longitude ?? null,
      }
    },
  )
})


const currentDensity = computed(() => {
  const density = trafficStats.value.density

  if (!density || Object.keys(density).length === 0) {
    return "Unknown"
  }

  return Object.entries(density).sort(
    (a, b) => b[1] - a[1],
  )[0][0]
})


onMounted(() => {
  loadAnalyticsData()
  loadPredictions()
})

const predictions = ref([])
const predictionLoading = ref(false)
const predictionError = ref("")

const loadPredictions = async () => {
  predictionLoading.value = true
  predictionError.value = ""

  try {
    const response = await getPredictions()

    predictions.value = response.data
  } catch (error) {
    predictionError.value = error.message
  } finally {
    predictionLoading.value = false
  }
}

const latestTrafficData = computed(() => {
  if (!trafficData.value.length) {
    return null
  }

  return trafficData.value[
    trafficData.value.length - 1
  ]
})

const latestVehicleDistribution = computed(() => {
  return latestTrafficData.value?.vehicle_distribution ?? {}
})

const latestPrediction = computed(() => {
  if (!predictions.value.length) {
    return null
  }

  return predictions.value[0]
})
</script>

<template>
  <div class="space-y-6">

    <!-- Header -->

    <AnalyticsHeader />

    <!-- Toolbar -->

    <AnalyticsToolbar />

    <!-- Stat Cards -->

    <section class="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">
      <AnalyticsStatCard
        title="Vehicles"
        :value="
          trafficLoading
            ? '...'
            : trafficStats.total_vehicles.toLocaleString()
        "
        subtitle="Recorded Traffic"
        :icon="TruckIcon"
        color="green"
      />

      <AnalyticsStatCard
        title="Average Speed"
        :value="
          trafficLoading
            ? '...'
            : `${trafficStats.average_speed} km/h`
        "
        subtitle="Realtime"
        :icon="BoltIcon"
        color="blue"
      />

      <AnalyticsStatCard
        title="AI Accuracy"
        value="98.7%"
        subtitle="YOLO v11"
        :icon="CpuChipIcon"
        color="cyan"
      />

      <AnalyticsStatCard
        title="Traffic Density"
        :value="currentDensity"
        subtitle="Current"
        :icon="SignalIcon"
        color="yellow"
      />
    </section>

    <!-- Trend -->

    <section class="grid gap-6 xl:grid-cols-3">

      <div class="xl:col-span-2">
        <TrafficTrendChart
          :traffic-data="trafficData"
        />
      </div>

      <TrafficDensityChart
        :density="latestTrafficData?.density ?? 'Unknown'"
      />

    </section>

    <!-- Distribution -->

    <section class="grid gap-6 md:grid-cols-2">

      <VehicleDistribution
        :distribution="latestVehicleDistribution"
        :total-vehicles="latestTrafficData?.vehicle_count ?? 0"
      />

      <PredictionHistory
        :predictions="predictions"
      />

    </section>

    <!-- AI -->

    <section class="grid gap-6 xl:grid-cols-2">

      <AIInsight
        :traffic-data="latestTrafficData"
        :prediction="latestPrediction"
      />

      <HeatmapCard
        :hotspots="trafficHotspots"
      />

    </section>

  </div>
</template>