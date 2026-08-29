<script setup>
import { SparklesIcon } from "@heroicons/vue/24/outline"
</script>

<template>
  <div class="flex items-start gap-3">
    <div class="rounded-xl bg-[#008170]/10 p-2">
      <SparklesIcon class="h-5 w-5 text-[#00A884]" />
    </div>

    <div>
      <div
        class="app-surface-soft inline-flex items-center gap-1 rounded-2xl px-4 py-3"
      >
        <span class="h-2 w-2 animate-bounce rounded-full bg-[#00A884]" />
        <span
          class="h-2 w-2 animate-bounce rounded-full bg-[#00A884] [animation-delay:150ms]"
        />
        <span
          class="h-2 w-2 animate-bounce rounded-full bg-[#00A884] [animation-delay:300ms]"
        />
      </div>

      <p class="app-text-muted mt-1 text-xs">
        SmartTraffic AI is thinking...
      </p>
    </div>
  </div>
</template>