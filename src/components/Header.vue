<script setup lang="ts"></script>

<template>
  <header>
    <svg class="hamburger-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
      <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
      <g id="SVGRepo_iconCarrier">
        <path d="M4 18L20 18" stroke="#E8EFB2" stroke-width="2" stroke-linecap="round"></path>
        <path d="M4 12L20 12" stroke="#E8EFB2" stroke-width="2" stroke-linecap="round"></path>
        <path d="M4 6L20 6" stroke="#E8EFB2" stroke-width="2" stroke-linecap="round"></path>
      </g>
    </svg>
  </header>
</template>

<style>
.hamburger-icon {
  position: fixed;
  top: 0;
  right: 0;
  width: clamp(2rem, 5%, 4rem);
  z-index: 1;
}
</style>
