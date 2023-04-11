<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavbarComponent from "@/components/NavbarComponent.vue";
</script>

<template>
  <div class="page">
    <NavbarComponent/>
    <div class="page-wrapper">
      <div class="page-body">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
