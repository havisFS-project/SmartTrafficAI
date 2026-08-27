<script setup>
import { ref, onMounted, onUnmounted } from "vue"

import {
  getTheme,
  toggleTheme,
} from "@/utils/theme"

import {
  HomeIcon,
  VideoCameraIcon,
  ChartBarIcon,
  DocumentChartBarIcon,
  Cog6ToothIcon,
  SparklesIcon,
  MoonIcon,
  SunIcon,
} from "@heroicons/vue/24/outline"

const currentTheme = ref(getTheme())

const menus = [
  {
    name: "Dashboard",
    icon: HomeIcon,
    path: "/",
    badge: null,
  },
  {
    name: "CCTV",
    icon: VideoCameraIcon,
    path: "/cctv",
    badge: 3,
  },
  {
    name: "Analytics",
    icon: ChartBarIcon,
    path: "/analytics",
    badge: null,
  },
  {
    name: "Reports",
    icon: DocumentChartBarIcon,
    path: "/reports",
    badge: null,
  },
  {
    name: "AI Assistant",
    icon: SparklesIcon,
    path: "/chatbot",
    badge: "AI",
  },
]

const systems = [
  {
    name: "Backend",
    status: "Online",
  },
  {
    name: "AI Engine",
    status: "Ready",
  },
  {
    name: "MongoDB",
    status: "Connected",
  },
]

const changeTheme = () => {
  currentTheme.value = toggleTheme()
}

const handleThemeChange = (event) => {
  currentTheme.value = event.detail
}

onMounted(() => {
  window.addEventListener(
    "theme-changed",
    handleThemeChange,
  )
})

onUnmounted(() => {
  window.removeEventListener(
    "theme-changed",
    handleThemeChange,
  )
})
</script>

<template>
  <aside class="app-surface flex h-screen w-72 flex-col">
    <!-- Logo -->
    <div class="app-border border-b px-7 py-8">
      <h1 class="text-2xl font-bold tracking-wide text-[#00A884]">
        SmartTrafficAI
      </h1>

      <p class="app-text-muted mt-2 text-sm">
        AI Powered Traffic Monitoring
      </p>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 overflow-y-auto py-6 scrollbar-thin scrollbar-thumb-[#005B41]">
      <!-- Overview -->
      <div>
        <p
          class="app-text-muted px-7 pb-3 text-xs font-semibold uppercase tracking-[0.25em]"
        >
          Overview
        </p>

        <RouterLink
          v-for="menu in menus"
          :key="menu.name"
          :to="menu.path"
          custom
          v-slot="{ navigate, isActive }"
        >
          <a
            :href="menu.path"
            @click="navigate"
            :class="[
              'group relative mx-3 mb-2 flex items-center gap-4 rounded-xl px-5 py-3 transition-all duration-300',
              isActive
                ? 'bg-[#005B41] text-white shadow-lg'
                : 'app-text-muted hover:bg-[#005B41]/10 hover:text-current',
            ]"
          >
            <!-- Active Indicator -->
            <div
              v-if="isActive"
              class="absolute left-0 h-8 w-1 rounded-r-full bg-[#00A884]"
            />

            <!-- Icon -->
            <component
              :is="menu.icon"
              :class="[
                'h-6 w-6 transition-transform duration-300 group-hover:scale-110',
                isActive ? 'text-white' : 'app-text-muted',
              ]"
            />

            <!-- Label -->
            <span
              :class="[
                'font-medium transition-transform duration-300 group-hover:translate-x-1',
                isActive ? 'text-white' : 'app-text-muted',
              ]"
            >
              {{ menu.name }}
            </span>

            <!-- Badge -->
            <span
              v-if="menu.badge"
              class="ml-auto rounded-full bg-[#008170] px-2 py-1 text-xs font-semibold text-white"
            >
              {{ menu.badge }}
            </span>
          </a>
        </RouterLink>
      </div>

      <!-- System -->
      <div class="mt-10">
        <p
          class="app-text-muted px-7 pb-4 text-xs font-semibold uppercase tracking-[0.25em]"
        >
          System
        </p>

        <div class="space-y-4 px-7">
          <div
            v-for="system in systems"
            :key="system.name"
            class="flex items-center gap-3 rounded-lg px-3 py-2 transition hover:bg-black/5"
          >
            <div class="h-2 w-2 rounded-full bg-[#00A884]" />

            <div>
              <p class="app-text text-sm font-medium">
                {{ system.name }}
              </p>

              <p class="text-xs text-[#00D68F]">
                {{ system.status }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Divider -->
      <div class="app-border mx-6 my-8 border-t" />

      <!-- Preferences -->
      <div>
        <p
          class="app-text-muted px-7 pb-4 text-xs font-semibold uppercase tracking-[0.25em]"
        >
          Preferences
        </p>

        <div class="space-y-2 px-3">
          <RouterLink
            to="/settings"
            custom
            v-slot="{ navigate, isActive }"
          >
            <a
              :href="isActive ? '/settings' : '/settings'"
              @click="navigate"
              :class="[
                'group relative mx-3 flex w-auto items-center gap-4 rounded-xl px-5 py-3 transition-all duration-300',
                isActive
                  ? 'bg-[#005B41] text-white shadow-lg'
                  : 'app-text-muted hover:bg-[#005B41]/10 hover:text-current',
              ]"
            >
              <!-- Active Indicator -->
              <div
                v-if="isActive"
                class="absolute left-0 h-8 w-1 rounded-r-full bg-[#00A884]"
              />

              <!-- Icon -->
              <Cog6ToothIcon
                :class="[
                  'h-6 w-6 transition-transform duration-300 group-hover:scale-110',
                  isActive ? 'text-white' : 'app-text-muted',
                ]"
              />

              <!-- Label -->
              <span
                :class="[
                  'font-medium transition-transform duration-300 group-hover:translate-x-1',
                  isActive ? 'text-white' : 'app-text-muted',
                ]"
              >
                Settings
              </span>
            </a>
          </RouterLink>

          <button
            type="button"
            class="group relative mx-3 flex w-[calc(100%-1.5rem)] items-center gap-4 rounded-xl px-5 py-3 transition-all duration-300"
            :class="
              currentTheme === 'dark'
                ? 'app-text-muted hover:bg-[#005B41]/10 hover:text-current'
                : 'app-text-muted hover:bg-[#005B41]/10 hover:text-current'
            "
            @click="changeTheme"
          >
            <!-- Icon -->
            <component
              :is="currentTheme === 'dark' ? SunIcon : MoonIcon"
              class="h-6 w-6 transition-transform duration-300 group-hover:scale-110"
            />

            <!-- Label -->
            <span
              class="font-medium transition-transform duration-300 group-hover:translate-x-1"
            >
              {{ currentTheme === "dark" ? "Light Mode" : "Dark Mode" }}
            </span>
          </button>
        </div>
      </div>
    </nav>

    <!-- Footer -->
    <div class="app-border border-t p-5">
      <div class="flex items-center gap-4">
        <div
          class="flex h-12 w-12 items-center justify-center rounded-full bg-gradient-to-r from-[#005B41] to-[#008170] font-bold text-white shadow-lg"
        >
          HF
        </div>

        <div>
          <p class="app-text font-semibold">
            Havis
          </p>

          <p class="app-text-muted text-sm">
            Administrator
          </p>

          <p class="app-text-muted mt-1 text-xs">
            Version 0.1.0
          </p>
        </div>
      </div>
    </div>
  </aside>
</template>