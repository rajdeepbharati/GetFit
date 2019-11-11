import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import App from '@/App.vue'

import store from '@/store'
import router from '@/router'

Vue.use(Buefy)
Vue.config.productionTip = false

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
