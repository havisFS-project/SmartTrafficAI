<script setup>
import BaseCard from "./BaseCard.vue"
const props = defineProps({
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

const colors = {
  green: {
    bg: "bg-[#005B41]/20",
    icon: "text-[#00A884]",
  },

  blue: {
    bg: "bg-blue-500/20",
    icon: "text-blue-400",
  },

  yellow: {
    bg: "bg-yellow-500/20",
    icon: "text-yellow-400",
  },

  red: {
    bg: "bg-red-500/20",
    icon: "text-red-400",
  },
}
</script>

<template>
  <BaseCard>

    <div class="flex items-start justify-between">

      <div>

        <p class="text-sm text-gray-400">
          {{ title }}
        </p>

        <h2 class="mt-3 text-3xl font-bold text-white">
          {{ value }}
        </h2>

        <p class="mt-2 text-sm text-gray-500">
          {{ subtitle }}
        </p>

      </div>

      <div
        :class="[
          'flex h-12 w-12 items-center justify-center rounded-xl',
          colors[color].bg,
        ]"
      >

        <component
          :is="icon"
          v-if="icon"
          :class="[
            'h-6 w-6',
            colors[color].icon,
          ]"
        />

      </div>

    </div>

  </BaseCard>
</template>