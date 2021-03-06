import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import axios from "axios";
import axiosSetup from "./refresh_api.js";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

// a function to handle all Authorization headers related actions
axiosSetup()

axios.defaults.baseURL = "http://localhost:8000"

createApp(App).use(store).use(router).mount("#app");
