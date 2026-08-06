<script setup>
import ReportsHeader from "@/components/reports/ReportsHeader.vue"
import ReportsToolbar from "@/components/reports/ReportsToolbar.vue"
import ReportsSummaryCard from "@/components/reports/ReportsSummaryCard.vue"

import {
  DocumentTextIcon,
  CheckCircleIcon,
  ExclamationTriangleIcon,
  ClockIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <div class="space-y-6">
    <ReportsHeader />
    <ReportsToolbar />

    <section 
      class="grid gap-6 sm:grid-cols-2 xl:grid-cols-4"
    >
      <ReportsSummaryCard
        title="Total Reports"
        value="1,248"
        subtitle="This month"
        :icon="DocumentTextIcon"
        color="bg-cyan-500/10 text-cyan-400"
      />

      <ReportsSummaryCard
        title="Resolved"
        value="1,102"
        subtitle="88% completed"
        :icon="CheckCircleIcon"
        color="bg-green-500/10 text-green-400"
      />

      <ReportsSummaryCard
        title="Critical"
        value="18"
        subtitle="Need attention"
        :icon="ExclamationTriangleIcon"
        color="bg-red-500/10 text-red-400"
      />

      <ReportsSummaryCard
        title="Pending"
        value="128"
        subtitle="Waiting review"
        :icon="ClockIcon"
        color="bg-yellow-500/10 text-yellow-400"
      />
    </section>
  </div>
</template>