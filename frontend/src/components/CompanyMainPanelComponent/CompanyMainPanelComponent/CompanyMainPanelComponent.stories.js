import axios from 'axios'
import MockAdapter from 'axios-mock-adapter'
import { action } from '@storybook/addon-actions'
import { storiesOf } from '@storybook/vue'
import Vue from 'vue'
import Vuex from 'vuex'
import CompanyMainPanelComponent from './CompanyMainPanelComponent.vue'
import SuiVue from 'semantic-ui-vue'
import StoryRouter from 'storybook-vue-router'
import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyMainPanelNewJobComponent from '../../CompanyMainPanelComponent/CompanyMainPanelNewJobComponent/CompanyMainPanelNewJobComponent.vue'

Vue.use(Vuex)
Vue.use(Vuex)
Vue.use(SuiVue)

storiesOf('CompanyMainPanelComponent', module)
  .addDecorator(StoryRouter({}, {
    routes: [
      { path: '/', component: CompanyMainPanelComponent, name: 'main'},
      { path: '/new', component: CompanyMainPanelNewJobComponent },
      {
        path: '/menu',
        component: CompanyMainPanelComponent,
        name: 'menu',
        children: [{
          path: '/transactions',
          name: 'transactions',
          component: CompanyMainPanelComponent
        },
        {
          path: '/applications',
          name: 'applications',
          components: CompanyMainPanelComponent
        }
        ]
      }
    ]}))
  .add('Fully Working', () => {
    return {
      components: { CompanyMainPanelComponent },
      template: '<company-main-panel-component />',
      data: () => ({ })
    }
  }
  )
