import Vue from 'vue'
import './plugins/vuetify'
import VueSocketIO from 'vue-socket.io'

Vue.use(new VueSocketIO({
  connection: 'http://localhost:8000',
  options: { path: '/socket.io/' }
}))

import App from './App'

import router from './router'

router.push('/room')

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
