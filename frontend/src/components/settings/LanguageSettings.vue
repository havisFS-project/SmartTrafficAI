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
    class="rounded-2xl border border-white/5 bg-[#232D3F] p-6"
  >
    <div class="mb-6">
      <h2 class="text-xl font-semibold text-white">
        Language
      </h2>

      <p class="mt-1 text-sm text-gray-400">
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
            : 'border-white/10 bg-[#1B2435] hover:border-white/20'
        "
        @click="selectedLanguage = language.code"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <LanguageIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              {{ language.name }}
            </h3>

            <p class="mt-1 text-sm text-gray-400">
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