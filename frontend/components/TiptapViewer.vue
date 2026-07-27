<template>
  <EditorContent :editor="editor" />
</template>

<script setup>
import { useEditor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'

const props = defineProps({
  content: { type: String, required: true } // JSONB from your DB
})

const emit = defineEmits(['ready'])

const editor = useEditor({
  content: props.content,
  extensions: [StarterKit],
  editable: false,
  immediatelyRender: false,
  onCreate: () => emit('ready'),
})
</script>