import { defineStore } from "pinia";
import { IUser } from "../type";
import { v4 as uuidv4 } from "uuid";

type AuthState = {
  user?: IUser | null;
  token?: string | null;
};

export const useAuth = defineStore("auth", {
  state: (): AuthState => ({ user: null, token: null }),
  getters: {
    berear: (state) => `${state.token ?? ""}`,
    isAuth: (state) => state.user !== null,
  },
  actions: {
    login(token: string, user: any) {
      this.user = user as IUser;
      this.token = token;
    },
    logout() {
      this.user = null;
      this.token = null;
    },
  },
  persist: {
    storage: sessionStorage,
  },
});
