<script setup>
import CameraToolbar from "@/components/cctv/CameraToolbar.vue"
import CameraCard from "@/components/cctv/CameraCard.vue"

const cameras = [
  {
    id: 1,
    title: "Camera 01",
    location: "Main Intersection",
    status: "Live",
    fps: 96,
  },
  {
    id: 2,
    title: "Camera 02",
    location: "Highway",
    status: "Offline",
    fps: 0,
  },
  {
    id: 3,
    title: "Camera 03",
    location: "City Center",
    status: "Live",
    fps: 94,
  },
  {
    id: 4,
    title: "Camera 04",
    location: "South Ring Road",
    status: "Live",
    fps: 97,
  },
  {
    id: 5,
    title: "Camera 05",
    location: "Airport Road",
    status: "Maintenance",
    fps: 0,
  },
  {
    id: 6,
    title: "Camera 06",
    location: "North Highway",
    status: "Live",
    fps: 91,
  },
]
</script>

<template>
  <div class="space-y-6">
    <CameraToolbar />

    <section
      class="grid gap-6 sm:grid-cols-1 md:grid-cols-2 xl:grid-cols-3"
    >
      <CameraCard
        v-for="camera in cameras"
        :key="camera.id"
        :title="camera.title"
        :location="camera.location"
        :status="camera.status"
        :fps="camera.fps"
      />
    </section>
  </div>
</template>