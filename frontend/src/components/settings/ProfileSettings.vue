<script setup>
import { CameraIcon } from "@heroicons/vue/24/outline"
</script>

<template>
  <section
    class="rounded-2xl border border-white/5 bg-[#232D3F] p-6"
  >
    <div class="mb-6">
      <h2 class="text-xl font-semibold text-white">
        Profile
      </h2>

      <p class="mt-1 text-sm text-gray-400">
        Manage your account information
      </p>
    </div>

    <div class="flex flex-col gap-6 md:flex-row md:items-center">
      <div class="relative">
        <div
          class="flex h-20 w-20 items-center justify-center rounded-full bg-gradient-to-r from-[#005B41] to-[#008170] text-2xl font-bold text-white ring-2 ring-[#008170]/20"
        >
          HF
        </div>

        <button
          class="absolute -bottom-1 -right-1 rounded-full border-2 border-[#232D3F] bg-[#008170] p-2 text-white transition hover:bg-[#00A884]"
        >
          <CameraIcon class="h-4 w-4" />
        </button>
      </div>

      <div class="grid flex-1 gap-5 md:grid-cols-2">
        <div>
          <label class="mb-2 block text-sm text-gray-400">
            Full Name
          </label>

          <input
            value="Havis"
            class="w-full rounded-xl border border-white/10 bg-[#1B2435] px-4 py-3 text-white outline-none transition focus:border-[#00A884]"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm text-gray-400">
            Role
          </label>

          <input
            value="Administrator"
            disabled
            class="w-full rounded-xl border border-white/10 bg-[#1B2435] px-4 py-3 text-gray-500 outline-none"
          />
        </div>

        <div class="md:col-span-2">
          <label class="mb-2 block text-sm text-gray-400">
            Email
          </label>

          <input
            value="havis@example.com"
            type="email"
            class="w-full rounded-xl border border-white/10 bg-[#1B2435] px-4 py-3 text-white outline-none transition focus:border-[#00A884]"
          />
        </div>
      </div>
    </div>

    <div class="mt-6 flex justify-end">
      <button
        class="rounded-xl bg-[#008170] px-5 py-3 font-medium text-white transition hover:bg-[#00A884]"
      >
        Save Changes
      </button>
    </div>
  </section>
</template>