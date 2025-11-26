<script setup lang="ts">
import { poemCollection } from '@/data/poems'
import { toEditorSettings } from 'typescript'
import { computed, onMounted, reactive, ref } from 'vue'

interface Poem {
  id: number
  title: string
  author: string
  html: string
}

const props = defineProps<{ id: number }>()
const poem = computed(() => ({
  id: props.id,
  title: poemCollection[props.id]?.title,
  author: poemCollection[props.id]?.author,
  html: poemCollection[props.id]?.html,
}))
</script>

<template>
  <Teleport defer to="#modals">
    <div class="poemPage fade-in">
      <h1>{{ poem.title }}</h1>
      <h2>{{ poem.author }}</h2>
      <span v-html="poem.html"></span>
    </div>
  </Teleport>
</template>

<style>
.stanza {
  padding: 0.5% 0.5%;
}
.poemPage {
  background-color: #faf4ed;
  position: fixed;
  z-index: 3;
  width: 100%;
  border: 1cap;
  padding: 3% 10% 3% 10%;
}
.poemPage > * {
  text-align: center;
  width: 100%;
  font-size: 1.2rem;
}
.poemPage > h1 {
  text-align: center;
  width: 100%;
  font-size: 2rem;
}
.poemPage > h2 {
  margin: auto;
  text-align: center;
  width: 100%;
  font-size: 0.9rem;
  font-weight: bold;
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
