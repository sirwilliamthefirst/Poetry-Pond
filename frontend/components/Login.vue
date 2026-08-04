<script setup>
import { ref } from 'vue'
import { useAuthStore } from '~/stores/auth'

const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)

function closeModal() {
    isOpen.value = false
    email.value = ''
    password.value = ''
    errorMessage.value = ''
}

async function handleSubmit() {
    errorMessage.value = ''
    isSubmitting.value = true

    try {
        await authStore.login(email.value, password.value)
        closeModal()
    } catch (err) {
        errorMessage.value = 'Invalid email or password.'
    } finally {
        isSubmitting.value = false
    }
}
</script>


<template>
    <Teleport defer to="#modals">

        <div>
            <div class="overlay">
                <form class="poemPage fade-in" @submit.prevent="handleSubmit">
                    <h2>Log In</h2>

                    <label for="email">Email</label>
                    <input id="email" v-model="email" type="email" autocomplete="email" required />

                    <label for="password">Password</label>
                    <input id="password" v-model="password" type="password" autocomplete="current-password" required />

                    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>

                    <div class="actions">
                        <button type="button" @click="closeModal">Cancel</button>
                        <button type="submit" :disabled="isSubmitting">
                            {{ isSubmitting ? 'Logging in...' : 'Log In' }}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </Teleport>

</template>



<style scoped>
.login-trigger {
    cursor: pointer;
    font-weight: 500;
}

.overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    width: 320px;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.modal label {
    font-size: 0.85rem;
    margin-top: 0.5rem;
}

.modal input {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.error {
    color: #c0392b;
    font-size: 0.85rem;
}

.actions {
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
    margin-top: 1rem;
}
</style>