<script setup>
defineProps({
  modelValue: String,
  placeholder: String,
})
</script>

<template>
  <input
    :value="modelValue"
    :placeholder="placeholder"
    class="w-full rounded-xl border border-white/5 bg-[#232D3F] px-4 py-3 text-white placeholder:text-gray-500 transition-all duration-300 focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/30 focus:outline-none"
  />
</template>