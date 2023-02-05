<template>
  <div
    :class="`h-screen w-[280px] min-w-[280px] md:shadow-[0_-2px_4px_0_rgba(0,0,0,.2)] transition-[margin-left] duration-500  bg-[var(--app-base-color)] absolute md:relative ${
      toggle && 'ml-[-280px]'
    } z-30 sm:z-30`"
  >
    <div className="flex justify-center w-[100%] py-10">
      <img :src="logo" alt="" className=" h-[80px]" />
    </div>
    <div className="flex mt-10 flex-col">
      <vt-sidenav-action to="/" label="Dashboard">
        <template v-slot:icon>
          <v-icon name="bi-window-dash"></v-icon>
        </template>
      </vt-sidenav-action>
      <vt-sidenav-action to="/admin" label="Admin">
        <template v-slot:icon>
          <v-icon name="fa-user"></v-icon>
        </template>
      </vt-sidenav-action>
      <vt-sidenav-action to="/store" label="Stores">
        <template v-slot:icon>
          <v-icon name="fa-users"></v-icon>
        </template>
      </vt-sidenav-action>
    </div>
  </div>
</template>
<script lang="ts" setup>
defineProps<{ toggle: boolean }>();
</script>
<script lang="ts">
import { defineComponent, defineProps } from "vue";
import VtSidenavAction from "./SidenavAction.vue";
import logo from "../../../assets/logo.svg";
export default defineComponent({
  components: { VtSidenavAction },
  data() {
    return {
      logo,
    };
  },
});
</script>
