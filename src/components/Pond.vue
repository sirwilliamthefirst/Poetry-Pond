<script setup lang="ts">
import { ref, provide } from 'vue'
import { poemCollection } from '../data/poems.ts'
import Ripple from './Ripple.vue'
import Page from './Page.vue'

provide('poemCollection', poemCollection)
const ripples = ref<{ x: number; y: number; id: number }[]>([])
const lastClick = ref({ x: 0, y: 0 })
let rippleNextId = 0

function createRipple(event: MouseEvent) {
  console.log('create ripple!')
  const target = event.currentTarget as HTMLElement
  const rect = target.getBoundingClientRect()
  const x = event.clientX - rect.left
  const y = event.clientY - rect.top
  rippleNextId++
  console.log('click pos: ' + x + ', ' + y)
  let id = rippleNextId
  ripples.value.push({ x, y, id })
  lastClick.value = { x, y }
}

function filterRipple(id: number) {
  console.log(ripples.value.length, id)

  ripples.value = ripples.value.filter((x) => x.id != id)
  console.log(ripples.value.length)
}
</script>

<template>
  <div class="pond_title"><h1>Poetry Pond</h1></div>
  <div @click="createRipple" class="pond">
    <template v-for="ripple in ripples" :key="ripple.id">
      <Ripple
        @deleteRipple="filterRipple"
        :id="ripple.id"
        :style="{ left: ripple.x + 'px', top: ripple.y + 'px' }"
      ></Ripple>
    </template>
    <template v-for="poem in poemCollection" :key="poem.id">
      <Page :lastRipple="lastClick" :id="poem.id"></Page>
    </template>
  </div>

  <div class="modals" id="modals"></div>
</template>

<style>
.pond {
  background: radial-gradient(circle, lightblue, rgb(72, 72, 124));
  width: 100%;
  height: 100%;
  position: fixed;
}
.modals {
  position: absolute;
  background-attachment: fixed;
  z-index: 3;
  margin: auto;
  width: 70%; /* Mobile first */
  left: 50%;
  top: 10%;
  max-height: 90vh;
  scrollbar-width: none;
  -ms-overflow-style: none;
  transform: translate(-50%, 0%);
  display: flex;
  justify-content: center;
}

@media (min-width: 769px) {
  .modals {
    width: 40%;
  }
}

@keyframes wavy {
  0% {
    opacity: 1;
    top: 2%;
  }
  50% {
    top: 3%;
  }
  100% {
    top: 2%;
    opacity: 1;
  }
}

@font-face {
  font-family: 'cloudy_font';
  src: url('../assets/cotton-cloud.regular.ttf') format('truetype');
}
.pond_title {
  position: fixed;
  color: white;
  width: 100%;
  text-align: center;
  top: 2%;
  z-index: 1;
  font-family: 'cloudy_font';
  pointer-events: none;
  opacity: 1;
  font-size: 1rem;
  animation: wavy 4s ease-in-out infinite;
}
</style>
