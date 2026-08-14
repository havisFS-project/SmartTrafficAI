<template>
  <div class="flex h-screen">
    <Sidebar />

    <div class="flex-1 flex flex-col">
      <Navbar />

      <main class="app-bg flex-1 overflow-auto p-8">
        <RouterView />
      </main>
    </div>
  </div>
  <FloatingAssistant/>
</template>

<script setup>
import Sidebar from '@/components/navigation/Sidebar.vue'
import Navbar from '@/components/navigation/Navbar.vue'
import FloatingAssistant from "@/components/ai/FloatingAssistant.vue"
import { RouterView } from 'vue-router'
</script>