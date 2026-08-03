import { useAuthStore } from '~/stores/auth'

export default defineNuxtPlugin(() => {
  const authStore = useAuthStore()
  const retriedRequests = new WeakSet<object>()

  const api = $fetch.create({
    onRequest({ options }) {
      if (authStore.accessToken) {
        const headers = new Headers(options.headers)
        headers.set('Authorization', `Bearer ${authStore.accessToken}`)
        options.headers = headers
      }
    },
    async onResponseError({ request, response, options }) {
      if (response.status === 401 && !retriedRequests.has(options)) {
        try {
          await authStore.refresh()
          retriedRequests.add(options)

          const headers = new Headers(options.headers)
          headers.set('Authorization', `Bearer ${authStore.accessToken}`)
          options.headers = headers

          return $fetch(request, options as any)
        } catch {
          authStore.logout()
          navigateTo('/login')
        }
      }
    },
  })

  return {
    provide: {
      api,
    },
  }
})