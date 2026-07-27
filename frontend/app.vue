<script setup lang="ts">
const router = useRouter();
</script>
<template>
  <div>
    <NuxtRouteAnnouncer />
    <Header></Header>
    <div class="pond_container">
      <NuxtPage />
    </div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.desktop-header {
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  width: 20vw;
  z-index: 1;
  margin: auto;
  float: right;
  height: min-content;
}
.pond_container {
  position: fixed;
  width: 100vw;
  height: 100vh;
  margin: 0 auto; /* centers horizontally */
  overflow: auto;
}

.modal-bg {
  width: 100vw;
  height: 100vh;
  z-index: 3;
  top: 0;
  left: 0;
  background-color: rgb(0, 0, 0, 0.5);
  position: fixed;
  justify-content: center;
  align-items: center;
  display: flex;
}
</style>
