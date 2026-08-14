<script setup>
import { ref } from "vue"
import {
  LockClosedIcon,
  ShieldCheckIcon,
  KeyIcon,
} from "@heroicons/vue/24/outline"

const twoFactorEnabled = ref(false)
const loginAlertsEnabled = ref(true)
</script>

<template>
  <section
    class="rounded-2xl border border-white/5 bg-[#232D3F] p-6"
  >
    <div class="mb-6">
      <h2 class="text-xl font-semibold text-white">
        Security
      </h2>

      <p class="mt-1 text-sm text-gray-400">
        Manage your account security and authentication
      </p>
    </div>

    <div class="space-y-4">
      <!-- Password -->
      <div
        class="flex flex-col gap-4 rounded-xl bg-[#1B2435] p-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <LockClosedIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Password
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              Change your account password
            </p>
          </div>
        </div>

        <button
          type="button"
          class="rounded-xl bg-[#008170] px-4 py-2.5 text-sm font-medium text-white transition hover:bg-[#00A884]"
        >
          Change Password
        </button>
      </div>

      <!-- Two-Factor Authentication -->
      <div
        class="flex items-center justify-between gap-4 rounded-xl bg-[#1B2435] p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <ShieldCheckIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Two-Factor Authentication
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              Add an extra layer of protection to your account
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="twoFactorEnabled"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/40"
          :class="
            twoFactorEnabled
              ? 'bg-[#008170]'
              : 'bg-[#475569]'
          "
          @click="twoFactorEnabled = !twoFactorEnabled"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="
              twoFactorEnabled
                ? 'translate-x-5'
                : 'translate-x-0'
            "
          />
        </button>
      </div>

      <!-- Login Alerts -->
      <div
        class="flex items-center justify-between gap-4 rounded-xl bg-[#1B2435] p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/20 p-3">
            <KeyIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="font-medium text-white">
              Login Alerts
            </h3>

            <p class="mt-1 text-sm text-gray-400">
              Get notified when your account is accessed
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="loginAlertsEnabled"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/40"
          :class="
            loginAlertsEnabled
              ? 'bg-[#008170]'
              : 'bg-[#475569]'
          "
          @click="loginAlertsEnabled = !loginAlertsEnabled"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="
              loginAlertsEnabled
                ? 'translate-x-5'
                : 'translate-x-0'
            "
          />
        </button>
      </div>
    </div>
  </section>
</template>