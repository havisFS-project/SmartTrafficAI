<script setup>
import { ref } from "vue"

import {
  SparklesIcon,
  LightBulbIcon,
  VideoCameraIcon,
  ChartBarIcon,
  ExclamationTriangleIcon,
  PaperAirplaneIcon,
} from "@heroicons/vue/24/outline"

import ChatMessageList from "@/components/chatbot/ChatMessageList.vue"

const message = ref("")
const hasMessages = ref(false)

const suggestions = [
  {
    label: "Traffic Condition",
    icon: ChartBarIcon,
    prompt: "What is the current traffic condition?",
  },
  {
    label: "CCTV Status",
    icon: VideoCameraIcon,
    prompt: "What is the current CCTV status?",
  },
  {
    label: "Traffic Prediction",
    icon: LightBulbIcon,
    prompt: "What is the latest traffic prediction?",
  },
  {
    label: "Accident Detection",
    icon: ExclamationTriangleIcon,
    prompt: "Are there any detected accidents?",
  },
]

const selectSuggestion = (prompt) => {
  message.value = prompt
}

const sendMessage = () => {
  const trimmedMessage = message.value.trim()

  if (!trimmedMessage) {
    return
  }

  hasMessages.value = true
}
</script>

<template>
  <div
    class="app-surface app-border flex min-h-[calc(100vh-2rem)] flex-col overflow-hidden rounded-2xl border"
  >
    <!-- Header -->
    <header
      class="app-border flex items-center justify-between border-b px-6 py-5"
    >
      <div class="flex items-center gap-4">
        <div class="rounded-xl bg-[#005B41]/10 p-3">
          <SparklesIcon class="h-7 w-7 text-[#00A884]" />
        </div>

        <div>
          <h1 class="app-text text-xl font-semibold">
            SmartTraffic AI
          </h1>

          <p class="app-text-muted text-sm">
            AI Traffic Assistant
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <span class="h-2.5 w-2.5 animate-pulse rounded-full bg-green-400" />

        <span class="text-sm font-medium text-green-400">
          Online
        </span>
      </div>
    </header>

    <!-- Chat Area -->
    <main class="flex min-h-0 flex-1 flex-col">
      <!-- Chat / Welcome Area -->
      <div class="min-h-0 flex-1 overflow-y-auto px-6 py-8">
        <template v-if="hasMessages">
          <ChatMessageList />
        </template>

        <template v-else>
          <!-- Welcome Screen -->
          <div
            class="flex h-full flex-col items-center justify-center"
          >
            <div
              class="mb-6 rounded-2xl bg-[#008170]/10 p-5"
            >
              <SparklesIcon
                class="h-10 w-10 text-[#00A884]"
              />
            </div>

            <div class="text-center">
              <h2 class="app-text text-3xl font-bold">
                Hello, Havis! 👋
              </h2>

              <p
                class="app-text-muted mx-auto mt-3 max-w-xl"
              >
                Ask me anything about traffic, CCTV,
                congestion, predictions, or accidents.
              </p>
            </div>

            <div
              class="mt-8 grid w-full max-w-2xl gap-3 sm:grid-cols-2"
            >
              <button
                v-for="suggestion in suggestions"
                :key="suggestion.label"
                type="button"
                class="app-surface-soft app-border app-text flex items-center gap-3 rounded-xl border px-4 py-4 text-left transition-all duration-200 hover:-translate-y-0.5 hover:border-[#008170]/40 hover:bg-[#008170]/5"
                @click="selectSuggestion(suggestion.prompt)"
              >
                <component
                  :is="suggestion.icon"
                  class="h-5 w-5 shrink-0 text-[#00A884]"
                />

                <span class="text-sm font-medium">
                  {{ suggestion.label }}
                </span>
              </button>
            </div>
          </div>
        </template>
      </div>

      <!-- Input Area -->
      <footer
        class="app-surface app-border shrink-0 border-t p-5"
      >
        <div
          class="mx-auto flex w-full max-w-4xl items-end gap-3"
        >
          <textarea
            v-model="message"
            rows="1"
            placeholder="Ask SmartTraffic AI..."
            class="app-surface-soft app-text app-border min-h-12 flex-1 resize-none rounded-xl border px-4 py-3 outline-none transition-all duration-300 placeholder:text-gray-500 focus:border-[#00A884] focus:ring-4 focus:ring-[#008170]/20 focus:shadow-[0_0_18px_rgba(0,168,132,0.2)]"
            @keydown.enter.exact.prevent="sendMessage"
          />

          <button
            type="button"
            class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-[#008170] text-white transition hover:bg-[#00A884]"
            @click="sendMessage"
          >
            <PaperAirplaneIcon class="h-5 w-5" />
          </button>
        </div>

        <p class="app-text-muted mt-3 text-center text-xs">
          SmartTraffic AI provides traffic-related assistance.
        </p>
      </footer>
    </main>
  </div>
</template>