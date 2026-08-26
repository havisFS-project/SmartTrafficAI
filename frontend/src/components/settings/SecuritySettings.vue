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
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Security
      </h2>

      <p class="app-text-muted mt-1 text-sm">
        Manage your account security and authentication
      </p>
    </div>

    <div class="space-y-4">
      <div
        class="app-surface-soft flex flex-col gap-4 rounded-xl p-5 sm:flex-row sm:items-center sm:justify-between"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <LockClosedIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Password
            </h3>

            <p class="app-text-muted mt-1 text-sm">
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

      <div
        class="app-surface-soft flex items-center justify-between gap-4 rounded-xl p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <ShieldCheckIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Two-Factor Authentication
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              Add an extra layer of protection to your account
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="twoFactorEnabled"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/30"
          :class="twoFactorEnabled ? 'bg-[#008170]' : 'app-toggle-off'"
          @click="twoFactorEnabled = !twoFactorEnabled"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="twoFactorEnabled ? 'translate-x-5' : 'translate-x-0'"
          />
        </button>
      </div>

      <div
        class="app-surface-soft flex items-center justify-between gap-4 rounded-xl p-5"
      >
        <div class="flex items-center gap-4">
          <div class="rounded-xl bg-[#005B41]/10 p-3">
            <KeyIcon class="h-6 w-6 text-[#00A884]" />
          </div>

          <div>
            <h3 class="app-text font-medium">
              Login Alerts
            </h3>

            <p class="app-text-muted mt-1 text-sm">
              Get notified when your account is accessed
            </p>
          </div>
        </div>

        <button
          type="button"
          role="switch"
          :aria-checked="loginAlertsEnabled"
          class="relative h-7 w-12 shrink-0 rounded-full p-1 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-[#008170]/30"
          :class="loginAlertsEnabled ? 'bg-[#008170]' : 'app-toggle-off'"
          @click="loginAlertsEnabled = !loginAlertsEnabled"
        >
          <span
            class="block h-5 w-5 rounded-full bg-white shadow-md transition-transform duration-200"
            :class="loginAlertsEnabled ? 'translate-x-5' : 'translate-x-0'"
          />
        </button>
      </div>
    </div>
  </section>
</template>