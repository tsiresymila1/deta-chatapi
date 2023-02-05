<template>
  <nav
    class="w-[100%] bg-[var(--app-navbar-color)] shadow-sm border-gray-200 px-6 py-3 flex items-start"
  >
    <div
      class="px-0 flex flex-wrap items-center justify-between w-[100%] my-auto"
    >
      <div class="flex my-auto">
        <span @click="ontoggle">
          <v-icon
            name="fa-bars"
            class="text-[var(--app-base-color)] cursor-pointer mt-[4px] mt-2"
          >
          </v-icon>
        </span>
        <div class="text-[#000000b6] font-bold flex ml-2 mt-2">
          <template v-for="(loc, index) in locations">
            <span v-if="index === 0 && index === locations.length -1" :key="`${new Date().toDateString()}-${loc}`" >
              <span class="ml-2">{{
                loc.charAt(0).toUpperCase() + loc.slice(1)
              }}</span>
            </span>
            <span v-else-if="index !== locations.length -1" :key="`${new Date().toDateString()}-${loc}`">
              <router-link class="decoration-none font-bold text-[var(--app-text-color)] hover:text-[var(--app-text-color)]" :to="'/' + loc">
                <span class="ml-2">{{
                  loc.charAt(0).toUpperCase() + loc.slice(1)
                }}</span>
              </router-link>
              <span class="ml-2">/</span>
            </span>
            <span v-else :key="`${new Date().toDateString()}-${index}`">
                <span class="ml-2">{{
                  loc.charAt(0).toUpperCase() + loc.slice(1)
                }}</span>
            </span>
          </template>
        </div>
      </div>
      <div class="flex flex-end">
        <div class="relative m-auto py-2 px-2">
          <v-icon name="fa-bell"></v-icon>
          <div class="w-[10px] h-[10px] absolute top-0 right-0">
            <span class="flex h-3 w-3">
              <span
                class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[var(--app-base-color)] opacity-75"
              ></span>
              <span
                class="relative inline-flex rounded-full h-3 w-3 bg-[var(--app-base-color)]"
              ></span>
            </span>
          </div>
        </div>
        <div class="relative inline-block">
          <vt-dropdown class="z-0" dataTarget="#dropProfile">
            <span className="mx-4">Jane Doe</span>
            <img src="../../assets/avatar.svg" alt="" className="w-[40px] h-[40px]" />
            <v-icon class="ml-2" name="fa-chevron-down"></v-icon>
          </vt-dropdown>
          <vt-dropdown-profile-content
            id="dropProfile"
          ></vt-dropdown-profile-content>
        </div>
      </div>
    </div>
  </nav>
</template>
<script lang="ts" setup>
defineProps<{ ontoggle: () => void }>();
</script>
<script lang="ts">
import { defineComponent } from "vue";
import VtDropdownProfileContent from "./DropDownProfileContent.vue";
type LoationType = string[];

export default defineComponent({
  components: { VtDropdownProfileContent },
  data: function () {
    return {
      locations: [] as LoationType,
    };
  },
  methods: {
    goto: function (path: string) {
      this.$router.push(path);
    },
  },
  mounted() {
    this.$router.beforeEach((to) => {
      this.locations = (to.fullPath as string)
        .split("/")
        .filter((e: string) => e !== "")
        .reduce<LoationType>((d: any[], n: any) => {
          d.push(n);
          return d;
        }, []);
        console.log("path :",this.locations)
    });
  },
});
</script>
