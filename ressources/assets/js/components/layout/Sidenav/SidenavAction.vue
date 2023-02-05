<template>
  <button
    :="$attrs"
    class="flex my-1 text-gray-300 pl-8 py-4 hover:text-gray-300 cursor-pointer bg-[var(--app-second-color) hover:bg-[var(--app-second-color)] mx-4 rounded-lg focus:bg-[var(--app-second-color)]"
    :class="active ? 'bg-[var(--app-second-color)]' : ''"
    @click="redirect"
  >
    <span class="mr-4">
      <slot name="icon"></slot>
    </span>
    <div class="font-bold text-[18px]">{{ $props.label }}</div>
  </button>
</template>
<script lang="ts" setup>
interface SidenavActionProps extends ButtonHTMLAttributes {
  label: string;
  to: string;
}
defineProps<SidenavActionProps>();
</script>
<script lang="ts">
import { ButtonHTMLAttributes, defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      active: false,
    };
  },
  mounted() {
    this.updateColor();
    this.$router.afterEach(() => {
      this.updateColor();
    });
  },
  methods: {
    redirect: function () {
      this.$router.push(this.to);
    },
    updateColor: function () {
      console.log(this.$route.fullPath as string, this.to);
      if (this.to === "/") {
        this.active = (this.$route.fullPath as string) === this.to;
      } else {
        this.active = (this.$route.fullPath as string).startsWith(this.to);
      }
    },
  },
});
</script>
