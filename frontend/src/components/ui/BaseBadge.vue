<script setup>
defineProps({
  color: {
    default: "green",
  },
})
</script>

<template>
  <span
    class="rounded-full bg-[#008170] px-3 py-1 text-xs font-semibold text-white"
  >
    <slot />
  </span>
</template>