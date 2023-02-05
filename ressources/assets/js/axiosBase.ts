import axios, { AxiosError, AxiosRequestConfig } from "axios";
import { useAuth } from "./store/auth";
import Toast from "vue-toastification";
import { useToast } from "vue-toastification";

export const axiosBase = axios.create({
  baseURL: import.meta.env.VITE_ROTULU_API_BASE_URL,
  withCredentials: true,
});

axiosBase.interceptors.request.use((config: AxiosRequestConfig<any>) => {
  const userStore = useAuth();
  if (userStore.isAuth) {
    if (config.headers) {
      config.headers["Authorization"] = userStore.berear;
    }
    config.headers = { Authorization: userStore.berear };
  }
  return config;
});

axiosBase.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error: AxiosError) => {
    const originalConfig = error.config;
    // if (error.response?.status === 401 && !originalConfig._retry) {
    //   originalConfig._retry = true;
    //   try {
    //     const userStore = useUserStore();
    //     // Refresh the token and retry once
    //     const accessToken = await userStore.refreshToken();
    //     originalConfig.headers.Authorization = "Bearer " + accessToken;
    //     return axiosPrivate(originalConfig);
    //   } catch (_error) {
    //     console.error("Refresh token failed");
    //     console.error(_error);
    //     return Promise.reject(_error);
    //   }
    // }
    const toast = useToast();
    toast.error(error.message);
    console.log("Error", error.message);
    return Promise.reject(error);
  }
);
