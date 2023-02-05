<template>
  <div className="h-screen bg-slate-50  inline-flex w-[100%] select-none ">
    <vt-sidenav :toggle="toggle"> </vt-sidenav>
    <div className="flex flex-col w-[100%] ">
      <vt-navbar :ontoggle="ontoggle"></vt-navbar>
      <div
        className="h-[100%] px-8 py-8 flex items-start flex-col bg-[var(--app-base-bg)] overflow-y-scroll"
      >
        <router-view></router-view>
      </div>
      <div
        v-show="!toggle"
        :class="`md:hidden absolute bg-black bg-opacity-20 h-screen w-screen z-20`"
        @click="ontoggle"
      ></div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import VtSidenav from "./Sidenav/Sidenav.vue";
import VtNavbar from "./NavBar.vue";
import { useAuth } from "../../store/auth";
export default defineComponent({
  components: { VtSidenav, VtNavbar },
  data: () => {
    return {
      toggle: (document.body.clientWidth < 768) as boolean,
    };
  },
  methods: {
    ontoggle: function () {
      this.toggle = !this.toggle;
    },
  },
  mounted() {
    this.$router.afterEach(() => {
      if (document.body.clientWidth < 768) {
        this.ontoggle();
      }
    });
  },
  beforeRouteEnter: (_, __, next) => {
    const { isAuth } = useAuth();
    if (isAuth) {
      next((___) => {
        console.log("")
      });
    } else {
      next("/login");
    }
  },
});
</script>
