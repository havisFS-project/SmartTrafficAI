<script setup>
import { XMarkIcon } from "@heroicons/vue/24/outline"

defineProps({
  report: {
    type: Object,
    default: null,
  },
  open: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(["close"])
</script>

<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition duration-200"
      enter-from-class="opacity-0"
      leave-active-class="transition duration-150"
      leave-to-class="opacity-0"
    >
      <div
        v-if="open && report"
        class="fixed inset-0 z-[100] flex items-center justify-center bg-black/70 p-4 backdrop-blur-sm"
        @click.self="emit('close')"
      >
        <div
          class="w-full max-w-2xl overflow-hidden rounded-2xl border border-white/10 bg-[#232D3F] shadow-2xl"
        >
          <!-- Header -->
          <div
            class="flex items-center justify-between border-b border-white/5 px-6 py-5"
          >
            <div>
              <h2 class="text-xl font-semibold text-white">
                Report Details
              </h2>

              <p class="mt-1 text-sm text-gray-400">
                {{ report.id }}
              </p>
            </div>

            <button
              class="rounded-xl p-2 text-gray-400 transition hover:bg-white/5 hover:text-white"
              @click="emit('close')"
            >
              <XMarkIcon class="h-6 w-6" />
            </button>
          </div>

          <!-- Content -->
          <div class="space-y-6 p-6">
            <!-- Basic Information -->
            <div class="grid gap-4 sm:grid-cols-2">
              <div>
                <p class="text-xs uppercase tracking-wider text-gray-500">
                  Camera
                </p>

                <p class="mt-1 font-medium text-white">
                  {{ report.camera }}
                </p>
              </div>

              <div>
                <p class="text-xs uppercase tracking-wider text-gray-500">
                  Location
                </p>

                <p class="mt-1 font-medium text-white">
                  {{ report.location }}
                </p>
              </div>

              <div>
                <p class="text-xs uppercase tracking-wider text-gray-500">
                  Date
                </p>

                <p class="mt-1 text-gray-300">
                  {{ report.date }}
                </p>
              </div>

              <div>
                <p class="text-xs uppercase tracking-wider text-gray-500">
                  Vehicles
                </p>

                <p class="mt-1 text-gray-300">
                  {{ report.vehicles }}
                </p>
              </div>
            </div>

            <!-- Traffic Status -->
            <div class="rounded-xl bg-[#1B2435] p-5">
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm text-gray-400">
                    Traffic Status
                  </p>

                  <span
                    class="mt-2 inline-flex rounded-full px-3 py-1 text-xs font-semibold"
                    :class="{
                      'bg-red-500/10 text-red-400':
                        report.status === 'Heavy Traffic',

                      'bg-yellow-500/10 text-yellow-400':
                        report.status === 'Medium',

                      'bg-green-500/10 text-green-400':
                        report.status === 'Normal',

                      'bg-blue-500/10 text-blue-400':
                        report.status === 'Low Traffic',
                    }"
                  >
                    {{ report.status }}
                  </span>
                </div>

                <div class="text-right">
                  <p class="text-sm text-gray-400">
                    AI Confidence
                  </p>

                  <p class="mt-1 text-2xl font-bold text-[#00A884]">
                    98%
                  </p>
                </div>
              </div>
            </div>

            <!-- Vehicle Breakdown -->
            <div>
              <h3 class="mb-4 text-sm font-semibold uppercase tracking-wider text-gray-400">
                Vehicle Breakdown
              </h3>

              <div class="grid grid-cols-2 gap-3 sm:grid-cols-4">
                <div class="rounded-xl bg-[#1B2435] p-4">
                  <p class="text-sm text-gray-500">Cars</p>
                  <p class="mt-1 text-xl font-bold text-white">82</p>
                </div>

                <div class="rounded-xl bg-[#1B2435] p-4">
                  <p class="text-sm text-gray-500">Motorcycles</p>
                  <p class="mt-1 text-xl font-bold text-white">71</p>
                </div>

                <div class="rounded-xl bg-[#1B2435] p-4">
                  <p class="text-sm text-gray-500">Buses</p>
                  <p class="mt-1 text-xl font-bold text-white">12</p>
                </div>

                <div class="rounded-xl bg-[#1B2435] p-4">
                  <p class="text-sm text-gray-500">Trucks</p>
                  <p class="mt-1 text-xl font-bold text-white">19</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>