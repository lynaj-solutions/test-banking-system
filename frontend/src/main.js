/* eslint-disable */
import Vue from 'vue'
import { store } from './store/store'
import router from '@/router'
import App from './App.vue'
import SuiVue from 'semantic-ui-vue'
import * as svgicon from 'vue-svgicon'
import VueCurrencyFilter from 'vue-currency-filter'
import 'semantic-ui-css/semantic.min.css'
import VueResource from 'vue-resource'
import VueResourceMock from 'vue-resource-mock'
import VueRouter from 'vue-router'
import VueHead from 'vue-head'
import VueMetamask from 'vue-metamask'
import NxCard from 'nx-card'
import VueFuse from 'vue-fuse'
import VueSpinners from 'vue-spinners'
import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'
import VueSwal from 'vue-swal'
// Font awesome
import library from '@fortawesome/fontawesome-svg-core'
import faUserSecret from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import faSpinner from '@fortawesome/free-solid-svg-icons'
import faAlignLeft from '@fortawesome/free-solid-svg-icons'
import VueResizeText from 'vue-resize-text'
import Toasted from 'vue-toasted'
import Multiselect from 'vue-multiselect'
import MenuIcon from "vue-material-design-icons/Menu.vue"
import "vue-material-design-icons/styles.css"

Vue.component("menu-icon", MenuIcon)
Vue.component('multiselect', Multiselect)
Vue.use(Toasted)
Vue.use(VueSwal)
Vue.use(VueResizeText)

Vue.component('font-awesome-icon', FontAwesomeIcon)
// End of Font Awesome
Vue.use(VueSpinners)

Vue.config.productionTip = false

Vue.use(SequentialEntrance)
Vue.use(VueFuse)
Vue.use(NxCard)
Vue.use(VueResource)
Vue.use(VueHead)
Vue.use(VueRouter)
Vue.use(VueCurrencyFilter)
Vue.use(SuiVue)

Vue.use(svgicon, {
  classPrefix: 'AppIcon-'
})

Vue.use(VueCurrencyFilter,
  {
    symbol: '$',
    thousandsSeparator: '.',
    fractionCount: 2,
    fractionSeparator: ',',
    symbolPosition: 'front',
    symbolSpacing: true
  })

var vm = new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
