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
        class="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm"
        @click.self="emit('close')"
      >
        <div
          class="app-surface app-border w-full max-w-2xl overflow-hidden rounded-2xl border shadow-2xl"
        >
          <!-- Header -->
          <div
            class="app-border flex items-center justify-between border-b px-6 py-5"
          >
            <div>
              <h2 class="app-text text-xl font-semibold">
                Report Details
              </h2>

              <p class="app-text-muted mt-1 text-sm">
                {{ report.id }}
              </p>
            </div>

            <button
              type="button"
              class="app-text-muted rounded-xl p-2 transition hover:bg-black/5 hover:text-current dark:hover:bg-white/5"
              @click="emit('close')"
            >
              <XMarkIcon class="h-6 w-6" />
            </button>
          </div>

          <!-- Content -->
          <div class="space-y-6 p-6">
            <!-- Basic Information -->
            <div class="grid gap-5 sm:grid-cols-2">
              <div>
                <p class="app-text-muted text-xs uppercase tracking-wider">
                  Camera
                </p>

                <p class="app-text mt-1 font-medium">
                  {{ report.camera }}
                </p>
              </div>

              <div>
                <p class="app-text-muted text-xs uppercase tracking-wider">
                  Location
                </p>

                <p class="app-text mt-1 font-medium">
                  {{ report.location }}
                </p>
              </div>

              <div>
                <p class="app-text-muted text-xs uppercase tracking-wider">
                  Date
                </p>

                <p class="app-text mt-1">
                  {{ report.date }}
                </p>
              </div>

              <div>
                <p class="app-text-muted text-xs uppercase tracking-wider">
                  Vehicles
                </p>

                <p class="app-text mt-1 font-medium">
                  {{ report.vehicles }}
                </p>
              </div>
            </div>

            <!-- Traffic Status -->
            <div class="app-surface-soft rounded-xl p-5">
              <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div>
                  <p class="app-text-muted text-sm">
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

                <div class="sm:text-right">
                  <p class="app-text-muted text-sm">
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
              <h3
                class="app-text-muted mb-4 text-xs font-semibold uppercase tracking-wider"
              >
                Vehicle Breakdown
              </h3>

              <div class="grid grid-cols-2 gap-3 sm:grid-cols-4">
                <div class="app-surface-soft rounded-xl p-4">
                  <p class="app-text-muted text-sm">
                    Cars
                  </p>

                  <p class="app-text mt-1 text-xl font-bold">
                    82
                  </p>
                </div>

                <div class="app-surface-soft rounded-xl p-4">
                  <p class="app-text-muted text-sm">
                    Motorcycles
                  </p>

                  <p class="app-text mt-1 text-xl font-bold">
                    71
                  </p>
                </div>

                <div class="app-surface-soft rounded-xl p-4">
                  <p class="app-text-muted text-sm">
                    Buses
                  </p>

                  <p class="app-text mt-1 text-xl font-bold">
                    12
                  </p>
                </div>

                <div class="app-surface-soft rounded-xl p-4">
                  <p class="app-text-muted text-sm">
                    Trucks
                  </p>

                  <p class="app-text mt-1 text-xl font-bold">
                    19
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>