<script setup>
import { ref } from "vue"
import {
  SparklesIcon,
  XMarkIcon,
  PaperAirplaneIcon,
} from "@heroicons/vue/24/outline"

const isOpen = ref(false)
const message = ref("")
</script>

<template>

<div class="fixed bottom-6 right-6 z-50">

    <!-- Floating Button -->

    <button
        @click="isOpen = !isOpen"
        class="flex h-16 w-16 items-center justify-center rounded-full
               bg-gradient-to-r from-[#005B41] to-[#008170]
               shadow-2xl transition hover:scale-110">

        <SparklesIcon class="h-8 w-8 text-white"/>

    </button>

    <!-- Chat Window -->

    <transition
        enter-active-class="duration-300"
        leave-active-class="duration-200"
        enter-from-class="opacity-0 translate-y-5"
        leave-to-class="opacity-0 translate-y-5">

        <div
            v-if="isOpen"
            class="absolute bottom-20 right-0 w-96 overflow-hidden rounded-2xl border border-white/10 bg-[#232D3F] shadow-2xl">

            <!-- Header -->

            <div
                class="flex items-center justify-between
                       bg-[#1A2233] px-5 py-4">

                <div>

                    <h2 class="font-semibold text-white">
                        SmartTraffic AI
                    </h2>

                    <p class="text-xs text-green-400">
                        Online
                    </p>

                </div>

                <button @click="isOpen=false">

                    <XMarkIcon class="h-6 w-6 text-gray-400"/>

                </button>

            </div>

            <!-- Body -->

            <div class="space-y-4 p-5">

                <div
                    class="rounded-xl bg-[#1A2233] p-4 text-sm text-gray-300">

                    👋 Hello Havis!

                    <br><br>

                    Ask me anything about traffic,
                    CCTV,
                    prediction,
                    congestion,
                    or accidents.

                </div>

            </div>

            <!-- Input -->

            <div
                class="flex items-center gap-3 border-t border-white/5 p-4">

                <input

                    v-model="message"

                    placeholder="Ask SmartTraffic AI..."

                    class="flex-1 rounded-xl bg-[#1A2233]
                           px-4 py-3 text-white outline-none"/>

                <button
                    class="rounded-xl bg-[#008170] p-3 transition hover:bg-[#00A884]">

                    <PaperAirplaneIcon class="h-5 w-5 text-white"/>

                </button>

            </div>

        </div>

    </transition>

</div>

</template>