<script setup>
import { ref } from "vue"
import {
  MoonIcon,
  SunIcon,
  CheckIcon,
} from "@heroicons/vue/24/outline"

import {
  getTheme,
  setTheme,
} from "@/utils/theme"

const theme = ref(getTheme())

const changeTheme = (selectedTheme) => {
  theme.value = selectedTheme
  setTheme(selectedTheme)
}
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Appearance
      </h2>

      <p class="app-text-muted mt-1 text-sm">
        Customize how SmartTrafficAI looks
      </p>
    </div>

    <div class="grid gap-4 md:grid-cols-2">
      <!-- Dark Mode -->
      <button
        type="button"
        class="relative rounded-2xl border p-5 text-left transition-all duration-300"
        :class="
          theme === 'dark'
            ? 'border-[#008170] bg-[#005B41]/10'
            : 'app-surface-soft app-border hover:opacity-90'
        "
        @click="changeTheme('dark')"
      >
        <div class="flex items-start justify-between">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <MoonIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div
            v-if="theme === 'dark'"
            class="rounded-full bg-[#008170] p-1"
          >
            <CheckIcon class="h-4 w-4 text-white" />
          </div>
        </div>

        <h3 class="app-text mt-5 font-semibold">
          Dark Mode
        </h3>

        <p class="app-text-muted mt-1 text-sm">
          Recommended for monitoring environments
        </p>
      </button>

      <!-- Light Mode -->
      <button
        type="button"
        class="relative rounded-2xl border p-5 text-left transition-all duration-300"
        :class="
          theme === 'light'
            ? 'border-[#008170] bg-[#005B41]/10'
            : 'app-surface-soft app-border hover:opacity-90'
        "
        @click="changeTheme('light')"
      >
        <div class="flex items-start justify-between">
          <div class="rounded-xl bg-yellow-400/10 p-3">
            <SunIcon class="h-6 w-6 text-yellow-400" />
          </div>

          <div
            v-if="theme === 'light'"
            class="rounded-full bg-[#008170] p-1"
          >
            <CheckIcon class="h-4 w-4 text-white" />
          </div>
        </div>

        <h3 class="app-text mt-5 font-semibold">
          Light Mode
        </h3>

        <p class="app-text-muted mt-1 text-sm">
          Better visibility in bright environments
        </p>
      </button>
    </div>
  </section>
</template>