<script setup>
defineProps({
  message: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div
    class="flex w-full"
    :class="
      message.role === 'user'
        ? 'justify-end'
        : 'justify-start'
    "
  >
    <div
      class="max-w-[80%]"
      :class="
        message.role === 'user'
          ? 'order-1'
          : ''
      "
    >
      <div
        class="rounded-2xl px-4 py-3"
        :class="
          message.role === 'user'
            ? 'bg-[#008170] text-white'
            : 'app-surface-soft app-text'
        "
      >
        <p class="whitespace-pre-line text-sm leading-6">
          {{ message.content }}
        </p>
      </div>

      <p
        class="app-text-muted mt-1 text-xs"
        :class="
          message.role === 'user'
            ? 'text-right'
            : 'text-left'
        "
      >
        {{ message.time }}
      </p>
    </div>
  </div>
</template>