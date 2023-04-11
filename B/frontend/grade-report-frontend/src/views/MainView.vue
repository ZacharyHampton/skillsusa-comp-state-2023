<template>
  <div class="container-xl">
    <div class="row row-deck row-cards">
        <ClassCardComponent name="ABC"></ClassCardComponent>
    </div>
  </div>
</template>

<script>
import ClassCardComponent from "@/components/class/ClassCardComponent.vue";
export default {
  name: "MainView",
  components: {ClassCardComponent}
}
</script>

<style scoped>

</style>