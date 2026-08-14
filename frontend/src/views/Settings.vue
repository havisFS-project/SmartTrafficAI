<script setup>
import SettingsHeader from "@/components/settings/SettingsHeader.vue"
import ProfileSettings from "@/components/settings/ProfileSettings.vue"
import AppearanceSettings from "@/components/settings/AppearanceSettings.vue"
import NotificationSettings from "@/components/settings/NotificationSettings.vue"
import SecuritySettings from "@/components/settings/SecuritySettings.vue"
import ApplicationSettings from "@/components/settings/ApplicationSettings.vue"
import LanguageSettings from "@/components/settings/LanguageSettings.vue"
</script>

<template>
  <div class="space-y-6">
    <SettingsHeader />

    <ProfileSettings />

    <AppearanceSettings />

    <NotificationSettings />

    <SecuritySettings />

    <ApplicationSettings />

    <LanguageSettings />
  </div>
</template>