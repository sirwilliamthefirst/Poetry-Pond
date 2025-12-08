<script setup lang="ts">
import { poemCollection } from '@/data/poems'
import { computed, onMounted, ref, nextTick, onUnmounted } from 'vue'

const props = defineProps<{ id: number }>()
const poem = computed(() => ({
  id: props.id,
  title: poemCollection[props.id]?.title,
  author: poemCollection[props.id]?.author,
  html: poemCollection[props.id]?.html,
}))

const poemPageRef = ref<HTMLElement | null>(null)

const adjustFontSize = () => {
  if (!poemPageRef.value || window.innerWidth > 768) return

  const paragraphs = poemPageRef.value.querySelectorAll('p')
  const style = window.getComputedStyle(poemPageRef.value)
  const paddingLeft = parseFloat(style.paddingLeft)
  const paddingRight = parseFloat(style.paddingRight)
  const availableWidth = poemPageRef.value.clientWidth - paddingLeft - paddingRight

  let fontSize = 18
  let allFit = false

  while (!allFit && fontSize > 6) {
    allFit = true
    paragraphs.forEach((p: HTMLElement) => {
      p.style.fontSize = `${fontSize}px`
      if (p.scrollWidth > availableWidth) {
        allFit = false
      }
    })
    if (!allFit) fontSize -= 0.25
  }
}

onMounted(() => {
  adjustFontSize()
  window.addEventListener('resize', adjustFontSize)
})

onUnmounted(() => {
  window.removeEventListener('resize', adjustFontSize)
})
</script>

<template>
  <Teleport defer to="#modals">
    <div ref="poemPageRef" class="poemPage fade-in">
      <h1>{{ poem.title }}</h1>
      <h2>{{ poem.author }}</h2>
      <div v-html="poem.html"></div>
    </div>
  </Teleport>
</template>

<style>
.stanza {
  padding: 1% 1%;
}

.poemPage {
  background-color: #faf4ed;
  position: fixed;
  z-index: 3;
  width: max-content;
  min-width: 60vw;
  max-width: 90vw;
  border: 1cap;
  padding: 3% 5%;
}

.poemPage > * {
  text-align: center;
  width: 100%;
  font-size: 1.2rem;
  margin: auto;
  overflow: visible;
}
.poemPage > h1 {
  text-align: center;
  width: 100%;
  font-size: clamp(1.5rem, 5vw, 2rem);
}

.poemPage > h2 {
  margin: auto;
  text-align: center;
  width: 100%;
  font-size: clamp(0.75rem, 2.5vw, 0.9rem);
  font-weight: bold;
}

.poemPage p {
  width: 100%;
  margin: 5px;
  font-size: clamp(1rem, 2vw, 2rem);
  overflow: visible;
}
@media (max-width: 768px) {
  .poemPage {
    max-width: 85vw;
    padding: 3% 2.5%;
  }
  .poemPage p {
    white-space: nowrap;
    font-size: clamp(0.6rem, 4vw, 2rem);
  }
}

.poemPage.fade-in {
  animation: fadeInPoem 0.6s ease;
}

@keyframes fadeInPoem {
  from {
    opacity: 0;
    transform: scale(0.95);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
