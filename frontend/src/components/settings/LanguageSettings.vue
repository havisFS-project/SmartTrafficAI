<script setup>
import { ref } from "vue"
import {
  LanguageIcon,
  CheckIcon,
} from "@heroicons/vue/24/outline"

const selectedLanguage = ref("en")

const languages = [
  {
    code: "en",
    name: "English",
    description: "Use English throughout the application.",
  },
  {
    code: "id",
    name: "Bahasa Indonesia",
    description: "Gunakan Bahasa Indonesia di seluruh aplikasi.",
  },
]
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Language
      </h2>

      <p class="app-text-muted mt-1 text-sm">
        Choose your preferred application language
      </p>
    </div>

    <div class="space-y-3">
      <button
        v-for="language in languages"
        :key="language.code"
        type="button"
        class="flex w-full items-center justify-between rounded-xl border p-4 text-left transition-all duration-200"
        :class="
          selectedLanguage === language.code
            ? 'border-[#008170] bg-[#005B41]/10'
            : 'app-surface-soft app-border hover:opacity-90'
        "
        @click="selectedLanguage = language.code"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <LanguageIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              {{ language.name }}
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              {{ language.description }}
            </p>
          </div>
        </div>

        <div
          v-if="selectedLanguage === language.code"
          class="rounded-full bg-[#008170] p-1"
        >
          <CheckIcon class="h-4 w-4 text-white" />
        </div>
      </button>
    </div>
  </section>
</template>