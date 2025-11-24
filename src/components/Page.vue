<script setup lang="ts">
import { ref, useTemplateRef, watchEffect, onMounted, watch, inject } from 'vue'
import { poemCollection } from '@/data/poems'
import Poem from './Poem.vue'

const props = defineProps<{ lastRipple: { x: number; y: number }; id: number }>()

const myElement = useTemplateRef('element')
const svgElement = useTemplateRef('svgElement')
const xPos = ref(0)
const yPos = ref(0)
const rotatation = ref(0)
const open = ref(false)
const poemRef = ref(null)

let dy = 0
let dx = 0
let dr = 0
let parent = myElement.value?.parentElement

onMounted(() => {
  dy = 1 * (Math.random() - 0.5)
  dx = 1 * (Math.random() - 0.5)
  parent = myElement.value?.parentElement
  if (parent) {
    const rect = myElement.value!.getBoundingClientRect()
    xPos.value = Math.random() * (parent.clientWidth - rect.width)
    yPos.value = Math.random() * (parent.clientHeight - rect.height)
  }
})

watch(
  () => [props.lastRipple.x, props.lastRipple.y],
  () => {
    const element = svgElement.value
    const parent = myElement.value?.parentElement
    if (!parent || !element) return

    const rect = element.getBoundingClientRect()
    const parentRect = parent.getBoundingClientRect()

    // Convert element center to parent-relative coordinates
    const centerX = rect.left - parentRect.left + rect.width / 2
    const centerY = rect.top - parentRect.top + rect.height / 2

    const xSide = centerX - props.lastRipple.x
    const ySide = centerY - props.lastRipple.y
    const dist = Math.sqrt(xSide ** 2 + ySide ** 2)
    const angle = Math.atan2(ySide, xSide)
    const force = Math.min(50 / (dist + 1), 1)

    dx += Math.cos(angle) * force
    dy += Math.sin(angle) * force

    // Rotational force
    const targetAngle = angle
    let angleDiff = targetAngle - rotatation.value

    // Normalize to shortest path
    while (angleDiff > Math.PI) angleDiff -= 2 * Math.PI
    while (angleDiff < -Math.PI) angleDiff += 2 * Math.PI

    dr += angleDiff * force * 0.5
  },
)

function animatePaper() {
  //Drift
  xPos.value += dx
  yPos.value += dy
  rotatation.value += dr
  if (parent) {
    const rect = myElement.value!.getBoundingClientRect()
    if (xPos.value > parent.clientWidth || xPos.value < 0 - rect.width) {
      xPos.value = Math.max(Math.min(parent.clientWidth, xPos.value), 0 - rect.width)
      dx = dx * -1
    }
    if (yPos.value > parent.clientHeight || yPos.value < 0 - rect.height) {
      yPos.value = Math.max(Math.min(parent.clientHeight, yPos.value), 0 - rect.height)
      dy = dy * -1
    }
  }

  //Slow down due to water drag
  dx = Math.abs(dx) < 0.005 ? 0 : dx - Math.sign(dx) * 0.002
  dy = Math.abs(dy) < 0.005 ? 0 : dy - Math.sign(dy) * 0.002
  dr = Math.abs(dr) < 0.005 ? 0 : dr - Math.sign(dr) * 0.002
  requestAnimationFrame(animatePaper)
}
animatePaper()
</script>

<template>
  <div
    ref="element"
    class="page-container"
    :style="{
      position: 'absolute',
      top: `${yPos}px`,
      left: `${xPos}px`,
    }"
  >
    <svg
      ref="svgElement"
      viewBox="0 0 128 128"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      aria-hidden="true"
      role="img"
      class="iconify iconify--noto page"
      :style="{
        transform: `rotate(${rotatation}deg)`,
      }"
      @click.stop="open = true"
      preserveAspectRatio="xMidYMid meet"
      fill="#000000"
    >
      <!-- SVG content stays the same -->
      <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
      <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
      <g id="SVGRepo_iconCarrier">
        <path fill="#ffffff" d="M87.85 6.19H16.8v115.45h94.62V28.8z"></path>
        <g
          fill="none"
          stroke="#b0bec5"
          stroke-width="3.865"
          stroke-linecap="round"
          stroke-miterlimit="10"
        >
          <path d="M33.34 41.05H94.5"></path>
          <path d="M33.34 55.68H94.5"></path>
          <path d="M33.34 70.3H94.5"></path>
          <path d="M33.34 84.93H94.5"></path>
          <path d="M33.34 99.56h26.15"></path>
        </g>
        <path
          d="M109.45 23.59L92.79 6.88A10.555 10.555 0 0 0 85.54 4h-68.5c-1.55 0-2.81 1.26-2.81 2.81v114.38c0 1.55 1.26 2.81 2.81 2.81h93.93c1.55 0 2.81-1.26 2.81-2.81V31.28c-.01-2.91-2.21-5.69-4.33-7.69zm.32 96.41H18.23V8h64.66c2.12 0 3.85 1.72 3.85 3.85v17.88h17.34c3.14 0 5.69 1.73 5.69 5.69V120z"
          fill="#6fbff0"
        ></path>
      </g>
    </svg>
    <span class="poetrytext">{{ poemCollection[props.id]?.title }}</span>
  </div>
  <div v-if="open" class="modal-bg" @click.stop="open = false">
    <Poem :id="props.id" ></Poem>
  </div>
</template>

<style>
.page-container {
  width: 5%;
  height: 5%;
  position: absolute;
  text-align: center;
}

.modal-bg {
  width: 100vw;
  height: 100vh;
  z-index: 3;
  top: 0;
  left: 0;
  background-color: rgb(0, 0, 0, 0.5);
  position: fixed;
  justify-content: center;
  align-items: center;
  display: flex;
}

.page {
  width: 100%;
  height: 100%;
}

.poetrytext {
  bottom: 150%;
  visibility: hidden;
  overflow: hidden;
  white-space: nowrap;
  background-color: black;
  color: #fff;
  position: relative;
  z-index: 2;
  pointer-events: none;
  margin: auto;
}

.page-container:hover .poetrytext {
  visibility: visible;
  animation: fade-in-text 1s forwards;
  animation-delay: 0.5s;
  transition-delay: 0.5s;
}

@keyframes fade-in-text {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.75;
  }
}
</style>
