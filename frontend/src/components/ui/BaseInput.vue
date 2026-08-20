<script setup>
defineProps({
  modelValue: {
    type: String,
    default: "",
  },

  placeholder: {
    type: String,
    default: "",
  },
})
</script>

<template>
  <input
    :value="modelValue"
    :placeholder="placeholder"
    class="app-surface-soft app-text app-border w-full rounded-xl border px-4 py-3 transition-all duration-300 outline-none placeholder:text-gray-500 focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/30 focus:shadow-[0_0_18px_rgba(0,168,132,0.25)]"
  />
</template>