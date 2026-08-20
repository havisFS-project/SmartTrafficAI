<script setup>
const systems = [
  {
    name: "Backend",
    status: "Online",
  },
  {
    name: "AI Engine",
    status: "Running",
  },
  {
    name: "MongoDB",
    status: "Connected",
  },
  {
    name: "YOLO Model",
    status: "Loaded",
  },
]
</script>

<template>
  <div
    class="app-surface app-border h-full rounded-2xl border p-6 shadow-lg"
  >
    <h2 class="app-text text-xl font-semibold">
      System Status
    </h2>

    <p class="app-text-muted mb-6 text-sm">
      Realtime Services
    </p>

    <div class="space-y-5">
      <div
        v-for="system in systems"
        :key="system.name"
        class="flex items-center justify-between"
      >
        <span class="app-text">
          {{ system.name }}
        </span>

        <div class="flex items-center gap-2">
          <div
            class="h-2 w-2 animate-pulse rounded-full bg-green-500"
          />

          <span class="text-sm text-green-400">
            {{ system.status }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>