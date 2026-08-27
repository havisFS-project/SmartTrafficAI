<script setup>
import ChatMessage from "./ChatMessage.vue"

const messages = [
  {
    id: 1,
    role: "assistant",
    content:
      "Hello Havis! 👋\nHow can I help you with traffic monitoring today?",
    time: "21:40",
  },
  {
    id: 2,
    role: "user",
    content:
      "How is the traffic condition at Highway KM 12?",
    time: "21:41",
  },
  {
    id: 3,
    role: "assistant",
    content:
      "Traffic is currently heavy at Highway KM 12. AI detection reports increased vehicle density compared with the previous 15 minutes.",
    time: "21:41",
  },
  {
    id: 4,
    role: "user",
    content:
      "What do you recommend?",
    time: "21:42",
  },
  {
    id: 5,
    role: "assistant",
    content:
      "I recommend increasing the green-light duration and monitoring the intersection for the next 15 minutes.",
    time: "21:42",
  },
]
</script>

<template>
  <div class="mx-auto w-full max-w-4xl space-y-5">
    <ChatMessage
      v-for="message in messages"
      :key="message.id"
      :message="message"
    />
  </div>
</template>