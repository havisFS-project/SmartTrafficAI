<script setup>
import ReportsHeader from "@/components/reports/ReportsHeader.vue"
import ReportsToolbar from "@/components/reports/ReportsToolbar.vue"
import ReportsSummaryCard from "@/components/reports/ReportsSummaryCard.vue"
import ReportsTable from "@/components/reports/ReportsTable.vue"

import {
  DocumentTextIcon,
  CheckCircleIcon,
  ExclamationTriangleIcon,
  ClockIcon,
} from "@heroicons/vue/24/outline"
</script>

<template>
  <div class="space-y-6">
    <!-- Header -->
    <ReportsHeader />

    <!-- Toolbar -->
    <ReportsToolbar />

    <!-- Summary -->
    <section class="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">
      <ReportsSummaryCard
        title="Total Reports"
        value="1,248"
        subtitle="This month"
        :icon="DocumentTextIcon"
        color="cyan"
      />

      <ReportsSummaryCard
        title="Resolved"
        value="1,102"
        subtitle="88% completed"
        :icon="CheckCircleIcon"
        color="green"
      />

      <ReportsSummaryCard
        title="Critical"
        value="18"
        subtitle="Need attention"
        :icon="ExclamationTriangleIcon"
        color="red"
      />

      <ReportsSummaryCard
        title="Pending"
        value="128"
        subtitle="Waiting review"
        :icon="ClockIcon"
        color="yellow"
      />
    </section>

    <!-- Reports Table -->
    <ReportsTable />
  </div>
</template>