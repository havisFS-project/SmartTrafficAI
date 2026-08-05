<script setup>

const predictions = [

{

time:"09:45",

location:"Highway KM 12",

status:"Heavy Traffic",

confidence:"98%",

color:"bg-red-500",

},

{

time:"09:30",

location:"City Center",

status:"Normal",

confidence:"96%",

color:"bg-green-500",

},

{

time:"09:10",

location:"Airport Road",

status:"Low Traffic",

confidence:"95%",

color:"bg-blue-500",

},

]

</script>

<template>

<div
class="rounded-2xl
border
border-white/5
bg-[#232D3F]
p-6">

<h2
class="text-xl
font-semibold
text-white">

AI Prediction History

</h2>

<p
class="mb-6
text-sm
text-gray-400">

Latest AI traffic predictions

</p>

<div
class="space-y-4">

<div

v-for="item in predictions"

:key="item.time"

class="rounded-xl
bg-[#1B2435]
p-4">

<div
class="flex
items-center
justify-between">

<div>

<p
class="font-semibold
text-white">

{{ item.location }}

</p>

<p
class="text-sm
text-gray-400">

{{ item.time }}

</p>

</div>

<span
:class="item.color"

class="rounded-full
px-3
py-1
text-xs
font-semibold
text-white">

{{ item.status }}

</span>

</div>

<div
class="mt-3
text-sm
text-gray-400">

Confidence

<span
class="ml-2
font-semibold
text-[#00A884]">

{{ item.confidence }}

</span>

</div>

</div>

</div>

</div>

</template>