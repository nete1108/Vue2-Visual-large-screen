import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import dataV from '@jiaminghi/data-view'
import '@/assets/css/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import * as echarts from 'echarts';



Vue.use(dataV);
Vue.use(VueAxios, axios);
Vue.prototype.$axios = axios;
Vue.prototype.$echarts = echarts;

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
