<template>
  <EditorContent :editor="editor" />
</template>

<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'

const props = defineProps({
  content: { type: String, required: true } // JSONB from your DB
})


const editor = useEditor({
  content: props.content,
  extensions: [StarterKit],
  editable: true,
  immediatelyRender: false,
})

defineExpose({ editor })
</script>