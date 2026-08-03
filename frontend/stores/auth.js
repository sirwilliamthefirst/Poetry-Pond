// pinia store (auth.js)
export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null,
    refreshToken: null,
    user: null,
  }),
  actions: {
    async login(email, password) {
      const { data } = await $fetch('/api/user/login', {
        method: 'POST',
        body: { email, password }
      })
      this.accessToken = data.access_token
      this.refreshToken = data.refresh_token
    }
  }
})