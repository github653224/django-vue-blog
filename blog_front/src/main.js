import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import highlight from './static/highlight'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import axios from 'axios'
import share from 'vue-shares'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faGithub, faWeibo, faWeixin } from '@fortawesome/free-brands-svg-icons'
library.add(faGithub, faWeibo, faWeixin)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('V-share', share)
Vue.use(mavonEditor)
Vue.prototype.axios = axios
axios.defaults.withCredentials = true
axios.defaults.headers['Content-Type'] = 'application/json'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
Vue.use(highlight)
Vue.config.productionTip = false
Vue.use(ElementUI)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
