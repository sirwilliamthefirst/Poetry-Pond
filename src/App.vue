<script setup lang="ts">
import Pond from './components/Pond.vue'
import Header from './components/Header.vue'
</script>

<template>
  <Header></Header>

  <div class="pond_container">
    <Pond></Pond>
  </div>
</template>

<style>
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
</style>
