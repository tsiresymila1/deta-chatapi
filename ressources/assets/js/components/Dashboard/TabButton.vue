<template>
  <button
    :="$attrs"
    :class="`text-gray-600 py-4 px-6 block hover:text-[var(--app-base-color)] focus:outline-none ${
      active
        ? 'text-[var(--app-base-color)] border-b-2 font-medium border-[var(--app-base-color)]'
        : 'text-[var(--app-base-color)] border-b-2 font-medium border-[transparent]'
    }`"
  >
    <slot></slot>
  </button>
</template>

<script lang="ts" setup>
import { ButtonHTMLAttributes } from "vue";
interface Props extends ButtonHTMLAttributes {
  active?: boolean;
}
defineProps<Props>();
</script>
