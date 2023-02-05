import { createApp } from "vue";
import { createPinia } from "pinia";
import { createRouter, createWebHistory } from "vue-router";
import VueSocketIO from "vue-3-socket.io";
// import { io } from "https://cdn.socket.io/4.3.2/socket.io.esm.min.js"
import {io} from 'socket.io-client'

import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import Toast from "vue-toastification";
import { OhVueIcon, addIcons } from "oh-vue-icons";
import * as FaIcons from "oh-vue-icons/icons/fa";
import * as BIcons from "oh-vue-icons/icons/bi";
import InputVue from "./components/common/Input.vue";
import SelectVue from "./components/common/Select.vue";
import ButtonVue from "./components/common/Button.vue";
import DropDownVue from "./components/common/DropDown.vue";

import "@vuepic/vue-datepicker/dist/main.css";
import "vue-toastification/dist/index.css";
import "./style.css";

import App from "./App.vue";
import { routes } from "./route";

const app = createApp(App);

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const router = createRouter({
  history: createWebHistory(),
  routes,
});

addIcons(...Object.values({ ...FaIcons }), ...Object.values({ ...BIcons }));
app.use(new VueSocketIO({
  debug: true,
  connection:io("/", {
    transports: ["polling", "websocket"]
  }),
}))




app.use(pinia);
app.use(router);
app.component("VIcon", OhVueIcon);
app.component("VtInput", InputVue);
app.component("VtButton", ButtonVue);
app.component("VtSelect", SelectVue);
app.component("VtDropdown", DropDownVue);
app.use(Toast, {
  hideProgressBar: true,
  transition: "Vue-Toastification__fade",
  maxToasts: 1,
  newestOnTop: true,
  timeout: 0,
  toastClassName: "toast-app",
  position: "bottom-right",
  containerClassName: "toast-container-app",
  bodyClassName: "toast-body-app",
});

router.isReady().then(() => app.mount("#app"));

