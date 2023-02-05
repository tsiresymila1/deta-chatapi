<template>
  <button
    :="$attrs"
    class="relative flex items-center text-sm text-gray-600  border border-transparent rounded-md focus:outline-none"
    @click="toggleshow"
    >
    <slot></slot>
  </button>
</template>

<script lang="ts" setup>
interface Props extends ButtonHTMLAttributes {
  dataTarget: string;
}
defineProps<Props>();
</script>
<script lang="ts">
import { ButtonHTMLAttributes, defineComponent } from "vue";
export default defineComponent({
  name: "vt-dropdown",
  data: () => {
    return {
      show: false as boolean,
    };
  },
  methods: {
    toggleshow: function () {
      const elm = document.querySelector(`${this.dataTarget}`)!;
      if (elm) {
        elm.classList.toggle("hidden");
        this.show = !this.show;
      }
    },
  },
  mounted() {
    const elm = document.querySelectorAll(
      `${this.dataTarget} > .dropdown-item`
    )!;
    elm.forEach((e) => {
      e.addEventListener("click", (e) => {
        e.stopPropagation();
        this.toggleshow();
      });
    });
  },
  unmounted() {
    const elm = document.querySelectorAll(
      `${this.dataTarget} > .dropdown-item`
    )!;
    elm.forEach((e) => {
      e.removeEventListener("click", () => {
        console.log("removed")
      });
    });
  },
});
</script>
