<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  sockets: {
    connect: function () {
      console.log('Socket to notification channel connected')
    },
    message: function(data){
      console.log("Data received : ", data)
    }
  },
  mounted(){
    this.$socket.emit('message', {test: "data"})
  }
});
</script>
<template>
  <router-view></router-view>
</template>
