import { RouteRecordRaw } from "vue-router";

export const routes: RouteRecordRaw[] = [
  {
    name: "home",
    path: "/",
    component: import("./components/layout/Dashboard.vue"),
    children: [
      {
        name: "dashboard",
        path: "",
        component: import("./pages/Dashboard.vue"), 
      },
      {
        name: "admin",
        path: "admin",
        component: import("./pages/Admin.vue"),
        children: [
          {
            name : "add_list",
            path: "",
            component: import('./components/Admin/AdminList.vue')
          },
          {
            name : "add_admin",
            path: "add",
            component: import('./components/Admin/AdminForm.vue')
          }
        ]
      },
    ],
  },
  {
    name: "login",
    path: "/login",
    component: import("./pages/Login.vue"),
  },
  {
    name: "register",
    path: "/register",
    component: import("./pages/Register.vue"),
  },
  {
    name: "notfound",
    path: "/:pathMatch(.*)*",
    component: import("./pages/NotFound.vue"),
  },
];
