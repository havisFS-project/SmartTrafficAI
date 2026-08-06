<script setup>
defineProps({
  title: String,
  value: String,
  subtitle: String,
  icon: Object,
  color: String,
})
</script>

<template>
  <div
    class="rounded-2xl border border-white/5 bg-[#232D3F] p-6 transition-all duration-300 hover:-translate-y-1 hover:border-[#00A884]/30 hover:shadow-[0_10px_30px_rgba(0,168,132,.15)]"
  >
    <div class="flex items-start justify-between">

      <div>
        <p class="text-sm text-gray-400">
          {{ title }}
        </p>

        <h2 class="mt-3 text-4xl font-bold text-white">
          {{ value }}
        </h2>

        <p class="mt-2 text-sm text-gray-400">
          {{ subtitle }}
        </p>
      </div>

      <div
        :class="color"
        class="rounded-2xl p-4"
      >
        <component
          :is="icon"
          class="h-7 w-7"
        />
      </div>

    </div>
  </div>
</template>