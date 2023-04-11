<template>
  <div class="col-4">
    <div class="card">
      <div class="card-body">
        <h2>{{ name }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ClassCardComponent",
  props: {
    name: String
  }
}
</script>

<style scoped>

</style>