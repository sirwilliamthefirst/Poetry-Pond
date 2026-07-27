<script setup lang="ts">
import { poemCollection } from "@/data/poems";
import { reactive, computed, onMounted, ref, onUnmounted } from "vue";
import TiptapEditor from "./TiptapEditor.vue";


interface Poem {
  title: string
  author: string
}

const props = defineProps<{ poem: Poem }>();


const form = reactive({
  title: props.poem.title,
  author: props.poem.author,
})

const poemPageRef = ref<HTMLElement | null>(null);
const editorRef = ref<InstanceType<typeof TiptapEditor> | null>(null)

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

async function handleSubmit() {
  if (!editorRef.value?.editor) return
  const content = editorRef.value?.editor.getJSON()

  await $fetch('/api/poems', {
    method: 'POST',
    body: {
      title: form.title,
      author: form.author,
      content,
    },
  })
}


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

    <form class="poemPage fade-in" @submit.prevent="handleSubmit">
      <input v-model="form.title" type="text" class="title-input" placeholder="Title" />
      <input v-model="form.author" type="text" class="author-input" placeholder="Author" />

      <TiptapEditor ref="editorRef" content="" />

      <button type="submit" class="save-btn">Submit</button>
    </form>
  </Teleport>

</template>


<style>
.stanza {
  padding: 1% 1%;
}

.title-input,
.author-input {
  background: transparent;
  border: none;
  outline: none;
  text-align: center;
  width: 100%;
  font-family: inherit;
  color: inherit;
}

.title-input::placeholder,
.author-input::placeholder {
  color: inherit;
  opacity: 0.5;
}

input.title-input {
  font-weight: inherit;
  font-size: clamp(1.5rem, 5vw, 2rem);
}

input.author-input {
  font-weight: bold;
  font-size: clamp(0.75rem, 2.5vw, 0.9rem);
}

.save-btn {
  margin-top: 16px;
  padding: 10px 28px;
  border: none;
  border-radius: 999px;
  background-color: #3a5a40;
  color: #faf4ed;
  font-size: 1rem;
  font-family: inherit;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
}

.save-btn:hover {
  background-color: #2f4a34;
}

.save-btn:active {
  transform: scale(0.97);
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