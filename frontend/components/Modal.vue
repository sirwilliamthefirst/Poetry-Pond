<script setup lang="ts">
import { ref } from 'vue'

const emits = defineEmits(['closeModal'])
function closeModal() {
    emits('closeModal')
}
</script>

<template>
    <Teleport defer to="#modals">
        <div class="modal-bg" @click="closeModal">
            <div class="fade-in aligner" @click.stop>
                <slot></slot>
            </div>
        </div>
    </Teleport>
</template>
<style>
.modal-bg {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.5);
}

.aligner {
    position: absolute;
    top: 10%;
}

.fade-in {
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