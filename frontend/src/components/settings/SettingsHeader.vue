<script setup>
import { Cog6ToothIcon } from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="flex items-center justify-between rounded-3xl border border-white/5 bg-[#232D3F] p-7"
  >
    <div>
      <h1 class="text-4xl font-bold text-white">
        Settings
      </h1>

      <p class="mt-2 text-lg text-gray-400">
        Manage your SmartTrafficAI preferences
      </p>
    </div>

    <div
      class="hidden rounded-2xl bg-[#005B41]/20 p-4 sm:block"
    >
      <Cog6ToothIcon class="h-8 w-8 text-[#00A884]" />
    </div>
  </section>
</template>