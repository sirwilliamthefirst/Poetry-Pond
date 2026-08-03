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
                                    proxyUrl: process.env.BACKEND_API_BASE,
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