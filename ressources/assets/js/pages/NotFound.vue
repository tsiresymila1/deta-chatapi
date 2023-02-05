<template>
  <div class="flex items-center justify-center h-screen">
    <div class="flex flex-col">
      <div class="col py-4">
        <img src="../assets/notfound.jpg" style="height: 120px !important" />
      </div>
      <div>NOT FOUND</div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {};
  },
});
</script>

<style scoped>
#notfound {
  padding: 2rem;
  text-align: center;
  justify-content: center;
  height: 100vh;
}
.card {
  border: none;
  padding: 8px !important;
  padding-bottom: 24px !important;
}
.card-body {
  padding: 8px 22px !important;
}
.btn {
  border-radius: 0 !important;
}
</style>
