<template>
  <div class="flex h-screen bg-gray-100 dark:bg-[#0F0F0F]">

    <Sidebar />

    <div class="flex flex-col flex-1">

      <Navbar />

      <main class="flex-1 p-6 overflow-auto">
        <router-view />
      </main>

    </div>

  </div>
</template>

<script setup>
import Sidebar from '@/components/navigation/Sidebar.vue'
import Navbar from '@/components/navigation/Navbar.vue'
</script>