// pinia store (auth.js)
import { defineStore } from 'pinia'
export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null,
    refreshToken: null,
    user: null,
  }),
  actions: {
    async login(email, password) {
      const { $api } = useNuxtApp() 

      const data  = await $api('/api/user/login', {
        method: 'POST',
        body: { email, password }
      })
      this.accessToken = data.access_token
      this.refreshToken = data.refresh_token
      return
    }
  }
})