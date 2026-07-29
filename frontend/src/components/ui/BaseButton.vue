<script setup>
defineProps({
  variant: {
    type: String,
    default: "primary",
  },
})
</script>

<template>
  <button
    :class="[
      'rounded-xl px-5 py-3 font-medium transition-all duration-300',

      variant === 'primary'
        ? 'bg-[#008170] text-white hover:bg-[#00A884]'
        : 'bg-white/5 text-white hover:bg-white/10',
    ]"
  >
    <slot />
  </button>
</template>