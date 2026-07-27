<template>
  <div class="flex h-screen">
    <Sidebar />

    <div class="flex-1 flex flex-col">
      <Navbar />

      <main class="flex-1 p-6">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup>
import Sidebar from '@/components/navigation/Sidebar.vue'
import Navbar from '@/components/navigation/Navbar.vue'
import { RouterView } from 'vue-router'
</script>