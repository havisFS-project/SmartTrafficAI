<script setup>
import { ref } from "vue"

import {
  EyeIcon,
  TrashIcon,
} from "@heroicons/vue/24/outline"

import ReportsPagination from "./ReportsPagination.vue"
import ReportDetailModal from "./ReportDetailModal.vue"

const selectedReport = ref(null)

const showDetail = (report) => {
  selectedReport.value = report
}

const closeDetail = () => {
  selectedReport.value = null
}


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
</script>

<template>
  <section class="overflow-hidden rounded-2xl border border-white/5 bg-[#232D3F]">
    <div class="border-b border-white/5 px-6 py-5">
      <div>
        <h2 class="text-xl font-semibold text-white">
          Traffic Reports
        </h2>

        <p class="mt-1 text-sm text-gray-400">
          Historical traffic analysis records
        </p>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full min-w-[900px] text-left">
        <thead class="bg-[#1B2435]">
          <tr>
            <th class="px-6 py-4 text-sm font-semibold text-gray-400">
              Report ID
            </th>

            <th class="px-6 py-4 text-sm font-semibold text-gray-400">
              Date
            </th>

            <th class="px-6 py-4 text-sm font-semibold text-gray-400">
              Camera
            </th>

            <th class="px-6 py-4 text-sm font-semibold text-gray-400">
              Location
            </th>

            <th class="px-6 py-4 text-sm font-semibold text-gray-400">
              Status
            </th>

            <th class="px-6 py-4 text-sm font-semibold text-gray-400">
              Vehicles
            </th>

            <th class="px-6 py-4 text-right text-sm font-semibold text-gray-400">
              Actions
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="report in reports"
            :key="report.id"
            class="border-t border-white/5 transition hover:bg-white/[0.03]"
          >
            <td class="px-6 py-4 font-medium text-white">
              {{ report.id }}
            </td>

            <td class="px-6 py-4 text-sm text-gray-400">
              {{ report.date }}
            </td>

            <td class="px-6 py-4 text-sm text-gray-300">
              {{ report.camera }}
            </td>

            <td class="px-6 py-4 text-sm text-gray-300">
              {{ report.location }}
            </td>

            <td class="px-6 py-4">
              <span
                class="rounded-full px-3 py-1 text-xs font-semibold"
                :class="{
                  'bg-red-500/10 text-red-400':
                    report.status === 'Heavy Traffic',

                  'bg-yellow-500/10 text-yellow-400':
                    report.status === 'Medium',

                  'bg-green-500/10 text-green-400':
                    report.status === 'Normal',

                  'bg-blue-500/10 text-blue-400':
                    report.status === 'Low Traffic',
                }"
              >
                {{ report.status }}
              </span>
            </td>

            <td class="px-6 py-4 font-medium text-white">
              {{ report.vehicles }}
            </td>

            <td class="px-6 py-4">
              <div class="flex justify-end gap-2">
                <button
                  class="rounded-lg p-2 text-gray-400 transition hover:bg-[#008170]/10 hover:text-[#00A884]"
                  title="View report"
                  @click="showDetail(report)"
                >
                  <EyeIcon class="h-5 w-5" />
                </button>

                <button
                  class="rounded-lg p-2 text-gray-400 transition hover:bg-red-500/10 hover:text-red-400"
                  title="Delete report"
                >
                  <TrashIcon class="h-5 w-5" />
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <ReportsPagination
        :current-page="1"
        :total-pages="5"
    />
    <ReportDetailModal
        :open="selectedReport !== null"
        :report="selectedReport"
        @close="closeDetail"
    />
  </section>
</template>