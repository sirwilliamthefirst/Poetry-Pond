import { useAuthStore } from '~/stores/auth'

export default defineNuxtPlugin(() => {
  const authStore = useAuthStore()
  const retriedRequests = new WeakSet<object>()
  const config = useRuntimeConfig()
  const baseURL = (import.meta.client
  ? config.public.proxyUrl
  : config.public.proxyUrlSSR) as string
  

  const api = $fetch.create({
    baseURL,
    onRequest({ options }) {
      console.log('Resolved baseURL:', baseURL, 'client?', import.meta.client)
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