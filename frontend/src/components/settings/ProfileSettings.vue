<script setup>
import { CameraIcon } from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="app-surface app-border rounded-2xl border p-6"
  >
    <div class="mb-6">
      <h2 class="app-text text-xl font-semibold">
        Profile
      </h2>

      <p class="app-text-muted mt-1 text-sm">
        Manage your account information
      </p>
    </div>

    <div class="flex flex-col gap-6 md:flex-row md:items-center">
      <!-- Avatar -->
      <div class="relative shrink-0">
        <div
          class="flex h-20 w-20 items-center justify-center rounded-full bg-gradient-to-r from-[#005B41] to-[#008170] text-2xl font-bold text-white ring-2 ring-[#008170]/20"
        >
          HF
        </div>

        <button
          type="button"
          class="absolute -bottom-1 -right-1 rounded-full border-2 border-white bg-[#008170] p-2 text-white shadow-md transition hover:bg-[#00A884] dark:border-[#232D3F]"
        >
          <CameraIcon class="h-4 w-4" />
        </button>
      </div>

      <!-- Form -->
      <div class="grid flex-1 gap-5 md:grid-cols-2">
        <div>
          <label class="app-text-muted mb-2 block text-sm">
            Full Name
          </label>

          <input
            value="Havis"
            class="app-surface-soft app-text app-border w-full rounded-xl border px-4 py-3 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/20"
          />
        </div>

        <div>
          <label class="app-text-muted mb-2 block text-sm">
            Role
          </label>

          <input
            value="Administrator"
            disabled
            class="app-surface-soft app-text-muted app-border w-full rounded-xl border px-4 py-3 outline-none"
          />
        </div>

        <div class="md:col-span-2">
          <label class="app-text-muted mb-2 block text-sm">
            Email
          </label>

          <input
            value="havis@example.com"
            type="email"
            class="app-surface-soft app-text app-border w-full rounded-xl border px-4 py-3 outline-none transition focus:border-[#00A884] focus:ring-2 focus:ring-[#008170]/20"
          />
        </div>
      </div>
    </div>

    <div class="mt-6 flex justify-end">
      <button
        type="button"
        class="rounded-xl bg-[#008170] px-5 py-3 font-medium text-white transition hover:bg-[#00A884]"
      >
        Save Changes
      </button>
    </div>
  </section>
</template>