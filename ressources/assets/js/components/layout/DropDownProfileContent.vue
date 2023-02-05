<template>
  <div
    :="$attrs"
    :class="`hidden absolute right-[-10px] z-10 w-56 py-2 top-[60px] border border-[#dadada] overflow-hidden bg-white rounded-md shadow-xl dark:bg-gray-800 ${
      $attrs.class ?? ''
    }`"
  >
    <div
      class="flex items-center p-3 -mt-2 text-sm text-gray-600 transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white"
    >
      <img
        class="flex-shrink-0 object-cover mx-1 rounded-full w-9 h-9"
        :src="avatar"
        alt="jane avatar"
      />
      <div class="mx-1">
        <h1 class="text-sm font-semibold text-gray-700 dark:text-gray-200">
          Jane Doe
        </h1>
        <p class="text-sm text-gray-500 dark:text-gray-400">
          janedoe@exampl.com
        </p>
      </div>
    </div>
    <hr class="border-gray-300 dark:border-gray-700" />
    <button
      class="w-full px-4 py-3 text-sm text-gray-600 capitalize transition-colors duration-200 transform dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white"
      @click="logout"
    >
      Sign Out
    </button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import avatar from "../../assets/avatar.svg";
import { useAuth } from "../../store/auth";
const auth = useAuth();

export default defineComponent({
  data: () => {
    return {
      avatar,
    };
  },
  methods: {
    logout: function () {
      auth.logout();
      this.$router.push("/login");
    },
  },
});
</script>
