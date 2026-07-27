<script setup lang="ts">
const props = defineProps({
  originX: String,
  originY: String,
  id: Number,
})
const emit = defineEmits(['deleteRipple'])
</script>

<template>
  <div :="$attrs" class="ripple" @animationend="$emit('deleteRipple', props.id)"></div>
</template>

<style>
@keyframes ripple-ring {
  from {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.5;
  }
  to {
    transform: translate(-50%, -50%) scale(7);
    opacity: 0;
  }
}
.ripple {
  position: absolute;
  width: 20px;
  height: 20px;
  z-index: 1;
  border: 1px solid rgba(255, 255, 255, 0.5);
  background: transparent;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  animation: ripple-ring 2s ease-out forwards;
  pointer-events: none;
  user-select: none;
}
</style>
