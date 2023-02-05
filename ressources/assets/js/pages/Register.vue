<template>
  <div class="flex h-[100vh] bg-white-100 my-0">
    <div class="m-auto">
      <form autocomplete="off">
        <div
          class="bg-white shadow-md border border-gray-100 md:w-[60rem] w-[80vw] p-8 rounded-sm"
        >
          <div class="flex items-center justify-center py-4">
            <h3 class="text-[var(--app-base-color)] text-4xl font-bold">
              Register
            </h3>
          </div>
          <div class="flex flex-col md:flex-row">
            <div class="flex md:w-full lg:w-7/12 flex-col px-4 mt-8">
              <div class="flex justify-center">
                <div
                  class="flex relative w-[250px] h-[250px] justify-center border px-4 py-4 bg-white object-cover"
                >
                  <img :src="avatar" />
                  <div
                    class="absolute top-1 right-1 flex justify-end w-full mt-0"
                  >
                    <v-icon
                      v-if="profile"
                      name="fa-regular-times-circle"
                      width="20"
                      height="20"
                      class="cursor-pointer"
                      @click="remove_select_avatar"
                    ></v-icon>
                  </div>
                </div>
              </div>
              <div class="flex mt-6 justify-center">
                <label for="profile">
                  <v-icon
                    name="fa-camera"
                    width="30"
                    height="30"
                    class="cursor-pointer"
                  ></v-icon>
                </label>

                <input
                  @change="handle_file"
                  id="profile"
                  type="file"
                  class="hidden"
                />
              </div>

              <div className="flex w-full pt-1 pb-2 justify-end mt-8 ">
                <div class="text-[#acacac]">Have already an account ?</div>
                <vt-button
                  type="button"
                  class="bg-transparent text-center text-[var(--app-base-color)] rounded-none py-[2px]"
                  @click="signin"
                >
                  <span>Login</span>
                </vt-button>
              </div>
            </div>
            <div class="space-y-3 flex flex-col md:w-full px-4">
              <vt-input
                autocomplete="off"
                focusclass="border-[var(--app-base-color)]"
                id="email"
                type="text"
                label="Name"
                placeholder="Name"
                @change="onUsernameChange"
                v-model="name"
              >
                <template v-slot:addon
                  ><v-icon name="fa-user"></v-icon
                ></template>
              </vt-input>

              <vt-input
                autocomplete="off"
                focusclass="border-[var(--app-base-color)]"
                id="username"
                type="text"
                label="Username"
                placeholder="Username"
                v-model="username"
              >
                <template v-slot:addon
                  ><v-icon name="fa-user"></v-icon
                ></template>
              </vt-input>
              <vt-input
                autocomplete="off"
                focusclass="border-[var(--app-base-color)]"
                id="email"
                type="text"
                label="E-mail"
                placeholder="E-mail"
                @change="onPasswordChange"
                v-model="email"
              >
                <template v-slot:addon
                  ><v-icon name="fa-regular-envelope"></v-icon
                ></template>
              </vt-input>
              <vt-select
                focusclass="border-[var(--app-base-color)]"
                id="type"
                label="Type"
                v-model="role"
              >
                <template v-slot:addon
                  ><v-icon name="fa-lock"></v-icon
                ></template>
                <option value="USER">Client</option>
                <option value="ADMIN">Admin</option>
              </vt-select>
              <vt-input
                autocomplete="off"
                focusclass="border-[var(--app-base-color)]"
                id="password"
                type="password"
                label="Password"
                placeholder="Password"
                v-model="password"
              >
                <template v-slot:addon
                  ><v-icon name="fa-lock"></v-icon
                ></template>
              </vt-input>
              <vt-input
                autocomplete="off"
                focusclass="border-[var(--app-base-color)]"
                id="cpassword"
                type="password"
                label="Confirm password"
                v-model="cpassword"
                placeholder="Confirm password"
              >
                <template v-slot:addon
                  ><v-icon name="fa-lock"></v-icon
                ></template>
              </vt-input>
              <div className="flex pt-4 pb-4">
                <vt-button
                  :disabled="disabled"
                  type="button"
                  class="w-full disabled:opacity-50 bg-[var(--app-base-color)] text-center text-white rounded-none"
                  @click="singup"
                >
                  <img
                    v-if="isloading"
                    className="w-[20px] h-[20px] inline"
                    src="../assets/loader.gif"
                    alt="spinner"
                  />
                  <span v-else>Register</span>
                </vt-button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script lang="ts">
import { computed, defineComponent, ref, VNodeRef } from "vue";
import { useAuth } from "../store/auth";
import default_avatar from "../assets/avatar.svg";
import { axiosBase } from "../axiosBase";

export default defineComponent({
  setup: () => {
    const auth = useAuth();
    const disabled = ref<boolean>(false);
    const email = ref<string>("");
    const name = ref<string>("");
    const username = ref<string>("");
    const role = ref<string>("");
    const password = ref<string>("");
    const cpassword = ref<string>("");
    const profile = ref<File>();
    const file_input = ref<VNodeRef>();
    return {
      user: computed(() => auth.user),
      register: auth.register,
      disabled,
      name,
      username,
      email,
      role,
      password,
      cpassword,
      file_input,
      profile,
    };
  },
  data: () => {
    return {
      isloading: false as boolean,
      avatar: default_avatar,
    };
  },
  methods: {
    onUsernameChange(evt: Event) {
      console.log(evt.target);
    },
    onPasswordChange(evt: Event) {
      console.log(evt.target);
      this.disabled = false;
    },
    singup: async function () {
      this.isloading = true;
      const data = {
        name: this.name,
        username: this.username,
        password: this.password,
        role: this.role,
        email: this.email,
        profile: this.profile,
      };
      const formData = new FormData();
      Object.keys(data).forEach((key) => formData.append(key, data[key]));
      console.log("Data : ",data)
      axiosBase
        .post("/register", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .finally(() => {
          this.isloading = false;
        })
        .then((resp) => {
          console.log(resp);
        });

    },
    signin: function () {
      this.$router.push({
        name: "login",
      });
    },
    handle_file: function (e: any) {
      console.log("Event :", e.target.files);
      if (e.target.files && e.target.files.length > 0) {
        const file = e.target.files[0];
        this.avatar = URL.createObjectURL(file);
        this.profile = file;
      }
    },
    remove_select_avatar: function () {
      this.avatar = default_avatar;
      this.profile = null;
    },
  },
});
</script>
