<template>
  <div class="flex">
    <vt-tab>
      <vt-tab-button :active="activeIndex === 0" @click="navtab(0)" >
        Projects
      </vt-tab-button>
      <vt-tab-button :active="activeIndex === 1" @click="navtab(1)">
        Working items
      </vt-tab-button>
      <vt-tab-button :active="activeIndex === 2" @click="navtab(2)">
        Pull request
      </vt-tab-button>
    </vt-tab>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import VtTabButton from "./../components/Dashboard/TabButton.vue";
import VtTab from "./../components/Dashboard/Tab.vue";
export default defineComponent({
  components: {VtTabButton, VtTab},
  data: () =>{
      return {
        activeIndex: 0 as number
      }
  },
  methods: {
    navtab : function(index: number){
      this.activeIndex = index
    }
  }
});
</script>
