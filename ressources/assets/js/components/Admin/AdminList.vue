<template>
  <div>
    <div
      class="flex justify-between bg-[rgba(57,74,121,0.2)] py-8 px-6 rounded-md"
    >
      <vt-input
        autocomplete="off"
        class="placeholder:text-[var(--app-second-color)] bg-transparent"
        focusclass="border-[var(--app-base-color)] "
        containerclass="md:w-1/2 xl:w-4/12 rounded-md"
        id="email"
        type="text"
        placeholder="Search"
        border="border border-[var(--app-base-color)]"
      >
        <template v-slot:addon
          ><v-icon
            class="text-[var(--app-second-color)]"
            name="fa-search"
          ></v-icon
        ></template>
      </vt-input>
      <div class="md:w-1/2 xl:w-4/12 text-end">
        <vt-button
          class="bg-[var(--app-base-color)] rounded-md active:bg-[var(--app-second-color)] text-white"
          @click="go_to_add()"
        >
          <div class="flex">
            <v-icon name="fa-plus" class="text-white mt-[1px] mr-2" />
            Ajouter
          </div>
        </vt-button>
      </div>
    </div>
    <div class="flex mb-4 overflow-y-hidden mt-8">
      <table class="border-slate-400 w-full text-start table-fixed">
        <thead>
          <tr>
            <th :class="table_header">Id</th>
            <th :class="table_header">Name</th>
            <th :class="table_header">Email</th>
            <th :class="table_header">Username</th>
            <th :class="table_header">Role</th>
            <th :class="table_header"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user of users" :key="JSON.stringify(user)">
            <td :class="table_col">{{ user.id }}</td>
            <td :class="table_col">{{ user.name }}</td>
            <td :class="table_col">{{ user.email }}</td>
            <td :class="table_col">{{ user.username }}</td>
            <td :class="table_col">{{ user.email }}</td>
            <td :class="table_col">
              <div class="flex space-x-2 justify-center">
                <vt-button :class="btn_class">
                  <v-icon name="fa-eye"></v-icon>
                </vt-button>
                <vt-button :class="btn_class">
                  <v-icon name="fa-edit"></v-icon>
                </vt-button>
                <vt-button :class="btn_class">
                  <v-icon name="fa-trash"></v-icon>
                </vt-button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { axiosBase } from "../../axiosBase";
import { IUser } from "../../type";

export default defineComponent({
  data() {
    return {
      btn_class:
        "hover:text-white text-[var(--app-base-color)]  hover:bg-[var(--app-base-color)] rounded-none border border-[var(--app-base-color)]",
      table_col: "border-b-[1px] border-[#193779ae] py-[1rem] pl-6",
      table_header:
        "border-b-[1px] text-white border-[#193779ae] bg-[var(--app-base-color)] py-[1rem] pl-6 text-start",
      users: [] as IUser[],
    };
  },
  mounted() {
    axiosBase.get("/api/users").then((resp) => {
      this.users = resp.data;
    });
  },
  methods: {
    go_to_add: function () {
      this.$router.push({ name: "add_admin" });
    },
  },
});
</script>
