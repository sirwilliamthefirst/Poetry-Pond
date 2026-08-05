<script setup lang="ts">
import { poemCollection } from "@/data/poems";
import { computed, onMounted, ref, onUnmounted } from "vue";
import TiptapViewer from "./TiptapViewer.vue";

const props = defineProps<{ id: number }>();
const poem = computed(() => ({
  id: props.id,
  title: poemCollection[props.id]?.title,
  author: poemCollection[props.id]?.author,
  html: poemCollection[props.id]?.html,
}));

const poemPageRef = ref<HTMLElement | null>(null);

const adjustFontSize = () => {
  if (!poemPageRef.value || window.innerWidth > 768) return;

  const paragraphs = poemPageRef.value.querySelectorAll("p");
  const style = window.getComputedStyle(poemPageRef.value);
  const paddingLeft = parseFloat(style.paddingLeft);
  const paddingRight = parseFloat(style.paddingRight);
  const availableWidth =
    poemPageRef.value.clientWidth - paddingLeft - paddingRight;

  let fontSize = 18;
  let allFit = false;

  while (!allFit && fontSize > 6) {
    allFit = true;
    paragraphs.forEach((p: HTMLElement) => {
      p.style.fontSize = `${fontSize}px`;
      if (p.scrollWidth > availableWidth) {
        allFit = false;
      }
    });
    if (!allFit) fontSize -= 0.25;
  }
};

onMounted(() => {
  adjustFontSize();
  window.addEventListener("resize", adjustFontSize);
});

onUnmounted(() => {
  window.removeEventListener("resize", adjustFontSize);
});
</script>

<template>
  <Teleport defer to="#modals">
    <div ref="poemPageRef" class="poemPage fade-in">
      <h1>{{ poem.title }}</h1>
      <NuxtLink to="/profile">
        <h2>{{ poem.author }}</h2>
      </NuxtLink>
      <TiptapViewer :content="poem.html" @ready="adjustFontSize"></TiptapViewer>
    </div>
  </Teleport>
</template>

<style>
.stanza {
  padding: 1% 1%;
}
</style>
