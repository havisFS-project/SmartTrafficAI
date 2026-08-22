<script setup>
import { ref } from "vue"

import {
  EyeIcon,
  TrashIcon,
} from "@heroicons/vue/24/outline"

import ReportsPagination from "./ReportsPagination.vue"
import ReportDetailModal from "./ReportDetailModal.vue"

const selectedReport = ref(null)

const reports = [
  {
    id: "TR-0001",
    date: "06 Aug 2026, 21:40",
    camera: "Camera 01",
    location: "Highway KM 12",
    status: "Heavy Traffic",
    vehicles: 184,
  },
  {
    id: "TR-0002",
    date: "06 Aug 2026, 21:25",
    camera: "Camera 03",
    location: "City Center",
    status: "Normal",
    vehicles: 92,
  },
  {
    id: "TR-0003",
    date: "06 Aug 2026, 21:10",
    camera: "Camera 04",
    location: "South Ring Road",
    status: "Low Traffic",
    vehicles: 56,
  },
  {
    id: "TR-0004",
    date: "06 Aug 2026, 20:55",
    camera: "Camera 02",
    location: "Airport Road",
    status: "Medium",
    vehicles: 128,
  },
]

const statusClasses = {
  "Heavy Traffic": "bg-red-500/10 text-red-400",
  Medium: "bg-yellow-500/10 text-yellow-400",
  Normal: "bg-green-500/10 text-green-400",
  "Low Traffic": "bg-blue-500/10 text-blue-400",
}

const showDetail = (report) => {
  selectedReport.value = report
}

const closeDetail = () => {
  selectedReport.value = null
}
</script>

<template>
  <section
    class="app-surface app-border overflow-hidden rounded-2xl border"
  >
    <!-- Header -->
    <div class="app-border border-b px-6 py-5">
      <h2 class="app-text text-xl font-semibold">
        Traffic Reports
      </h2>

      <p class="app-text-muted mt-1 text-sm">
        Historical traffic analysis records
      </p>
    </div>

    <!-- Table -->
    <div class="overflow-x-auto">
      <table class="w-full min-w-[900px] text-left">
        <thead class="app-surface-soft">
          <tr>
            <th
              class="app-text-muted px-6 py-4 text-xs font-semibold uppercase tracking-wider"
            >
              Report ID
            </th>

            <th
              class="app-text-muted px-6 py-4 text-xs font-semibold uppercase tracking-wider"
            >
              Date
            </th>

            <th
              class="app-text-muted px-6 py-4 text-xs font-semibold uppercase tracking-wider"
            >
              Camera
            </th>

            <th
              class="app-text-muted px-6 py-4 text-xs font-semibold uppercase tracking-wider"
            >
              Location
            </th>

            <th
              class="app-text-muted px-6 py-4 text-xs font-semibold uppercase tracking-wider"
            >
              Status
            </th>

            <th
              class="app-text-muted px-6 py-4 text-xs font-semibold uppercase tracking-wider"
            >
              Vehicles
            </th>

            <th
              class="app-text-muted px-6 py-4 text-right text-xs font-semibold uppercase tracking-wider"
            >
              Actions
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="report in reports"
            :key="report.id"
            class="app-border border-t transition hover:bg-black/[0.03] dark:hover:bg-white/[0.03]"
          >
            <td class="app-text px-6 py-4 font-medium">
              {{ report.id }}
            </td>

            <td class="app-text-muted px-6 py-4 text-sm">
              {{ report.date }}
            </td>

            <td class="app-text px-6 py-4 text-sm">
              {{ report.camera }}
            </td>

            <td class="app-text px-6 py-4 text-sm">
              {{ report.location }}
            </td>

            <td class="px-6 py-4">
              <span
                class="rounded-full px-3 py-1 text-xs font-semibold"
                :class="statusClasses[report.status]"
              >
                {{ report.status }}
              </span>
            </td>

            <td class="app-text px-6 py-4 font-medium">
              {{ report.vehicles }}
            </td>

            <td class="px-6 py-4">
              <div class="flex justify-end gap-2">
                <button
                  type="button"
                  title="View report"
                  class="app-text-muted rounded-lg p-2 transition hover:bg-[#008170]/10 hover:text-[#00A884]"
                  @click="showDetail(report)"
                >
                  <EyeIcon class="h-5 w-5" />
                </button>

                <button
                  type="button"
                  title="Delete report"
                  class="app-text-muted rounded-lg p-2 transition hover:bg-red-500/10 hover:text-red-400"
                >
                  <TrashIcon class="h-5 w-5" />
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <ReportsPagination
      :current-page="1"
      :total-pages="5"
    />

    <!-- Detail Modal -->
    <ReportDetailModal
      :open="selectedReport !== null"
      :report="selectedReport"
      @close="closeDetail"
    />
  </section>
</template>