<script setup lang="ts">
import { ref } from 'vue'

const isMenuOpen = ref(false)
const menuWidth = ref(0)
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
  menuWidth.value = isMenuOpen.value ? 10 : 0
}
</script>

<template>
  <div v-if="isMenuOpen" class="backdrop" @click.stop()="isMenuOpen = false"></div>

  <div id="mySidenav" class="sidenav" :class="{ open: isMenuOpen }">
    <a href="https://forms.gle/AREQP5MJMg3sevg89">Submit</a>
  </div>

  <svg
    v-if="!isMenuOpen"
    @click="toggleMenu"
    class="hamburger-icon"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
    <g id="SVGRepo_iconCarrier">
      <path d="M4 18L20 18" stroke="#E8EFB2" stroke-width="2" stroke-linecap="round"></path>
      <path d="M4 12L20 12" stroke="#E8EFB2" stroke-width="2" stroke-linecap="round"></path>
      <path d="M4 6L20 6" stroke="#E8EFB2" stroke-width="2" stroke-linecap="round"></path>
    </g>
  </svg>
</template>

<style>
.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1; /* Below sidenav but above content */
}

.hamburger-icon {
  position: fixed;
  top: 0;
  right: 0;
  width: clamp(2rem, 5%, 4rem);
  z-index: 1;
}
.hamburger-icon:hover path {
  stroke: #ffffff;
}
.sidenav {
  height: 100%; /* 100% Full-height */
  opacity: 0;
  width: 0;
  background: #e8efb2;
  border-left: 1px groove #00d4ff;
  position: fixed; /* Stay in place */
  z-index: 2; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 100%;
  transform: translate(-100%, 0%);
  overflow-x: hidden; /* Disable horizontal scroll */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
}

.sidenav.open {
  width: clamp(30px, 25vw, 150px);
  opacity: 1;
}

/* The navigation menu links */
.sidenav a {
  padding: 8px 8px 8px 8px;
  text-decoration: none;
  font-size: clamp(1.5rem, 3vw, 3rem);
  color: #818181;
  display: block;
  transition: 0.3s;
}

/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  color: #f1f1f1;
}

/* Position and style the close button (top right corner) */
.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav a {
    font-size: 18px;
  }
}
</style>
