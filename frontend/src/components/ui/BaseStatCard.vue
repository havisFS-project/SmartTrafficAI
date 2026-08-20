<script setup>
import BaseCard from "./BaseCard.vue"

defineProps({
  title: {
    type: String,
    required: true,
  },

  value: {
    type: String,
    required: true,
  },

  subtitle: {
    type: String,
    default: "",
  },

  icon: {
    type: Object,
    default: null,
  },

  color: {
    type: String,
    default: "green",
  },
})

const colorMap = {
  green: {
    icon: "text-green-400",
    background: "bg-green-500/10",
  },

  blue: {
    icon: "text-blue-400",
    background: "bg-blue-500/10",
  },

  cyan: {
    icon: "text-cyan-400",
    background: "bg-cyan-500/10",
  },

  yellow: {
    icon: "text-yellow-400",
    background: "bg-yellow-500/10",
  },

  red: {
    icon: "text-red-400",
    background: "bg-red-500/10",
  },
}
</script>

<template>
  <BaseCard class="group">
    <div class="flex items-start justify-between">
      <div>
        <p class="app-text-muted text-sm">
          {{ title }}
        </p>

        <h2 class="app-text mt-3 text-3xl font-bold">
          {{ value }}
        </h2>

        <p class="app-text-muted mt-2 text-sm">
          {{ subtitle }}
        </p>
      </div>

      <div
        :class="[
          'rounded-xl p-3 transition-transform duration-300 group-hover:scale-105',
          colorMap[color]?.background ?? colorMap.green.background,
        ]"
      >
        <component
          v-if="icon"
          :is="icon"
          :class="[
            'h-6 w-6',
            colorMap[color]?.icon ?? colorMap.green.icon,
          ]"
        />
      </div>
    </div>
  </BaseCard>
</template>