<script setup>
import { ref } from "vue"
import {
  SparklesIcon,
  XMarkIcon,
  PaperAirplaneIcon,
} from "@heroicons/vue/24/outline"

const isOpen = ref(false)
const message = ref("")
</script>

<template>
  <div class="fixed bottom-6 right-6 z-50">
    <!-- Floating Button -->

    <button
      type="button"
      @click="isOpen = !isOpen"
      class="flex h-16 w-16 items-center justify-center rounded-full bg-gradient-to-r from-[#005B41] to-[#008170] shadow-2xl transition hover:scale-110"
    >
      <SparklesIcon class="h-8 w-8 text-white" />
    </button>

    <!-- Chat Window -->

    <Transition
      enter-active-class="duration-300"
      leave-active-class="duration-200"
      enter-from-class="translate-y-5 opacity-0"
      leave-to-class="translate-y-5 opacity-0"
    >
      <div
        v-if="isOpen"
        class="app-surface app-border absolute bottom-20 right-0 w-96 overflow-hidden rounded-2xl border shadow-2xl"
      >
        <!-- Header -->

        <div
          class="app-surface-soft flex items-center justify-between px-5 py-4"
        >
          <div>
            <h2 class="app-text font-semibold">
              SmartTraffic AI
            </h2>

            <p class="text-xs text-green-400">
              Online
            </p>
          </div>

          <button
            type="button"
            class="app-text-muted rounded-lg p-1 transition hover:bg-black/5 hover:text-current dark:hover:bg-white/5"
            @click="isOpen = false"
          >
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>

        <!-- Body -->

        <div class="space-y-4 p-5">
          <div
            class="app-surface-soft app-text-muted rounded-xl p-4 text-sm"
          >
            👋 Hello Havis!

            <br />
            <br />

            Ask me anything about traffic,
            CCTV,
            prediction,
            congestion,
            or accidents.
          </div>
        </div>

        <!-- Input -->

        <div
          class="app-border flex items-center gap-3 border-t p-4"
        >
          <input
            v-model="message"
            type="text"
            placeholder="Ask SmartTraffic AI..."
            class="app-surface-soft app-text app-border w-full rounded-xl border px-4 py-3 outline-none transition-all duration-300 placeholder:text-gray-500 focus:border-[#00A884] focus:ring-4 focus:ring-[#008170]/20 focus:shadow-[0_0_16px_rgba(0,168,132,0.2)]"
          />

          <button
            type="button"
            class="shrink-0 rounded-xl bg-[#008170] p-3 text-white transition hover:bg-[#00A884]"
          >
            <PaperAirplaneIcon class="h-5 w-5" />
          </button>
        </div>
      </div>
    </Transition>
  </div>
</template>