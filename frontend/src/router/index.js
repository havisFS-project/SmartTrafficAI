import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
import CCTV from '@/views/CCTV.vue'
import Analytics from '@/views/Analytics.vue'
import Reports from '@/views/Reports.vue'
import Chatbot from '@/views/Chatbot.vue'
import Settings from '@/views/Settings.vue'
import Login from '@/views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: '/cctv',
      name: 'cctv',
      component: CCTV,
    },
    {
      path: '/analytics',
      name: 'analytics',
      component: Analytics,
    },
    {
      path: '/reports',
      name: 'reports',
      component: Reports,
    },
    {
      path: '/chatbot',
      name: 'chatbot',
      component: Chatbot,
    },
    {
      path: '/settings',
      name: 'settings',
      component: Settings,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
  ],
})

export default router