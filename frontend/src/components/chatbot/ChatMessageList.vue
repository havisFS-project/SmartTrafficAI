<script setup>
import { nextTick, ref, watch } from "vue"

import ChatMessage from "./ChatMessage.vue"
import TypingIndicator from "./TypingIndicator.vue"

const props = defineProps({
  messages: {
    type: Array,
    required: true,
  },

  isTyping: {
    type: Boolean,
    default: false,
  },
})

const messageContainer = ref(null)

const scrollToBottom = async () => {
  await nextTick()

  if (!messageContainer.value) {
    return
  }

  messageContainer.value.scrollTo({
    top: messageContainer.value.scrollHeight,
    behavior: "smooth",
  })
}

watch(
  [
    () => props.messages.length,
    () => props.isTyping,
  ],
  () => {
    scrollToBottom()
  },
)
</script>

<template>
  <div
    ref="messageContainer"
    class="mx-auto max-h-[calc(100vh-14rem)] w-full max-w-4xl overflow-y-auto pr-2"
  >
    <div class="space-y-5">
      <ChatMessage
        v-for="message in messages"
        :key="message.id"
        :message="message"
      />

      <TypingIndicator v-if="isTyping" />
    </div>
  </div>
</template>