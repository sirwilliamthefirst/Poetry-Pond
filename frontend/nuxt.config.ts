// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
 ssr: true,

devtools: {
  enabled: true,
  timeline: {
    enabled: true
  }
},

debug: true,

 compatibilityDate: '2024-11-01',
 css: ['~/assets/css/main.css'],

 runtimeConfig: {
                    // Keys within public are also exposed client-side
                    public: {
                                    proxyUrl: process.env.BACKEND_API_BASE_CLIENT as string,
                                    proxyUrlSSR: process.env.BACKEND_API_BASE_SSR as string,
                    }
    },

 modules: ['@nuxt/eslint', '@pinia/nuxt'],

 vite: {
   server: {
     watch: {
       usePolling: true,
     },
   },
 },
})