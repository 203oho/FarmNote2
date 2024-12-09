import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import {DefaultConfig} from "http-client";
import 'vuetify/dist/vuetify.min.css';
import PrimeVue from 'primevue/config';
import {Select} from "primevue";
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-default.css';
import 'ol/ol.css';
import 'vuetify/styles'; // Vuetify 3 style imports


DefaultConfig.config = {
    basePath: import.meta.env.VITE_API_URL
};


const app = createApp(App)
app.use(ToastPlugin,{position: 'top'});
app.use(PrimeVue);
app.component('Select', Select)
app.use(router)

app.mount('#app')
