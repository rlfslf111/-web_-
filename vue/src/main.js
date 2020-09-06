import Vue from 'vue'
import VueCookies from 'vue-cookies'
import App from './App.vue'
import router from './router'

import Paginate from 'vuejs-paginate'
Vue.component('paginate', Paginate)

Vue.use(VueCookies)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
