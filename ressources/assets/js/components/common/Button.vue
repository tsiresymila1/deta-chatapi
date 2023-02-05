<template>
  <button
    :="$attrs"
    :class="`font-[Conduit] px-4 py-2 rounded-md active:bg-opacity-75 hover:bg-opacity-75 ${$attrs.class}`"
    >
    <slot></slot>
  </button>
</template>
<script lang="ts" setup>
interface Props extends ButtonHTMLAttributes {
  error?: null
}
defineProps<Props>();
</script>
<script lang="ts">
import { ButtonHTMLAttributes, defineComponent, defineProps } from "vue";

export default defineComponent({
  name: "vt-button",
});
</script>
