<script setup>
import { Cog6ToothIcon } from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="app-surface app-border flex items-center justify-between rounded-3xl border p-7"
  >
    <div>
      <h1 class="app-text text-4xl font-bold">
        Settings
      </h1>

      <p class="app-text-muted mt-2 text-lg">
        Manage your SmartTrafficAI preferences
      </p>
    </div>

    <div class="rounded-2xl bg-[#005B41]/10 p-4">
      <Cog6ToothIcon class="h-8 w-8 text-[#00A884]" />
    </div>
  </section>
</template>