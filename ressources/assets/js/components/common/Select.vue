<template>
  <div class="w-full">
    <label
      v-if="$props.label !== null"
      class="flex py-2 text-gray-500 text-sm"
      :for="idELmt"
      >
      {{ $props.label }}
    </label>
    <div
      :class="`flex items-start border ${
        !focus && ($props.border ?? ' border-gray-300')
      } rounded-none p-2 ${$props.containerclass ?? ''} ${
        focus && ($props.focusclass ?? '')
      }`"
      >
      <span v-if="$slots.addon" class="px-1"><slot name="addon"></slot></span>
      <select
        :="$attrs"
        :class="`w-full focus:outline-none px-2 py-1 mt-[2px] bg-transparent placeholder:text-gray-400 text-sm ${
          $props.class ?? ''
        }`"
        @focus="onfocus"
        @blur="onblur"
        >
      <slot></slot>
      </select>
    </div>
  </div>
</template>
<script lang="ts" setup>
interface InputProps extends InputHTMLAttributes {
  label?: string;
  containerclass?: string;
  focusclass?: string;
  border?: string;
}
defineProps<InputProps>();
</script>
<script lang="ts">
import { defineComponent, defineProps, InputHTMLAttributes } from "vue";

export default defineComponent({
  name: "vt-select",
  data: function () {
    const focus = false;
    const idELmt: string =
      (this.$attrs.id as string) ?? new Date().getTime().toString();
    return {
      focus,
      idELmt,
    };
  },
  methods: {
    onfocus: function () {
      this.focus = true;
    },
    onblur: function () {
      this.focus = false;
    },
  },
});
</script>
