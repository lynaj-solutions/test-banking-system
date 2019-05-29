
<template>
      

      <div :class="COMPUTED_horizontalVerticalClass" >

        <sui-segment class="div-class-company-main-menu-box-component">

          <template v-if="windowWidth >= 1200">
            <company-main-menu-box-component @changedMenuItem="METHOD_change_path_menu" :menuItems="localMenuItems" class="div-class-company-main-menu-box-component"/>
          </template>
          <template v-else>
            <company-main-menu-box-component @changedMenuItem="METHOD_change_path_menu" :menuItems="COMPUTED_localMenuItemsMobile" class="div-class-company-main-menu-box-component"/>

          </template>

        </sui-segment>

        <!-- component containig table with processed transactions -->
        <template v-if="COMPUTED_router_path == self_store.getters.GET_LINKS_OBJECT.transactions">

          <sui-segment style="width: 100%;display: block;margin: auto;">
            <company-table-with-transactions id="top"/>
          </sui-segment>

        </template>

        <!-- component containig form that allows user to create a new job offer -->

        <template v-else>

          <sui-segment style="width: 100%;">
            <company-apply-form :formObject="local_test_item" :screeningQuestions="screeningQuestions"/>
          </sui-segment>
        </template>

        <template v-if="windowWidth >= 1200">
           <sui-segment class="company-main-info-box-segment" >
            <company-info-box />
            <!--    balance table-->
            <company-main-balance-table></company-main-balance-table>

          </sui-segment>

        </template>



    </div>


</template>

<style lang="scss">
  @import './CompanyMainPanelComponent.css';
</style>

<script type="text/javascript">

  import {store} from '../../../store/store'
  import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
  import CompanyApplyForm from '../../CompanyApply/CompanyApplyForm/CompanyApplyForm.vue'
  import CompanyMainMenuBoxComponent from '../CompanyMainMenuBoxComponent/CompanyMainMenuBoxComponent.vue'
  import CompanyTableWithTransactions from '../CompanyTableWithTransactions/CompanyTableWithTransactions.vue'
  import CompanyMainBalanceTable from '../CompanyMainBalanceTable/CompanyMainBalanceTable.vue'
  import VueRouter from 'vue-router'

  var VueScrollTo = require('vue-scrollto');

export default {
  name: 'CompanyMainPanelComponent',
  data () {
    return {
      windowWidth: window.innerWidth,
      currently_viewed_job_offer: {},
      localMenuItems: [
        {
          'id': 0,
          'class': 'gamepad icon',
          'title': 'My Transactions',
          'path': store.getters.GET_LINKS_OBJECT.transactions
        },
        {
          'id': 1,
          'class': 'video camera icon',
          'title': 'Homepage',
          'path': store.getters.GET_LINKS_OBJECT.homepage
        },
      ]
    }
  },
  created () {
  },
  props: {

  },
  methods: {
    isEmpty: function (obj) {
      for (var key in obj) {
        if (obj.hasOwnProperty(key)) { return false }
      }
      return true
    },
    METHOD_change_path: function (nameOfThePath) {
      if (nameOfThePath == '/login') {
        store.commit('MUTATE_currentAction', 'login')
      }
      this.$router.push(nameOfThePath);
      VueScrollTo.scrollTo('#top', 500)
    },
    METHOD_change_path_menu: function (menuItemId) {
      var self = this;
      this.COMPUTED_localMenuItemsMobile.forEach(function (menuItem) {
        if (menuItem.id == menuItemId.id) {
          self.METHOD_change_path(menuItem.path)
        }
      })
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })
  },
  computed: {
    COMPUTED_localMenuItemsMobile() {
      let extendedMenuItemsArray = [...this.localMenuItems,
        {
          'id': 3,
          'class': 'video camera icon',
          'title': 'Post a Job',
          'path': store.getters.GET_LINKS_OBJECT.transferCreate
        }
      ];
      console.log('extendedMenuItemsArray: ' + JSON.stringify(extendedMenuItemsArray));
      return extendedMenuItemsArray;
    },
    COMPUTED_horizontalVerticalClass() {
      if(this.windowWidth <= 1200) {
        return 'ui vertical segments';
      } else {
        return 'ui horizontal segments'
      }
    },
    COMPUTED_styleMainDiv() {
      if(this.windowWidth <= 1200) {
         return `display: flex; flex-direction: column;`
      } else {
         return `display: flex; flex-direction: row;`
      }
    },
    COMPUTED_router_path () {
      return this.$route.path
    },
    COMPUTED_router_path_name () {
      return this.$route.name
    },
    COMPUTED_currently_viewed_job_offer () {
      return store.getters.GET_currently_viewed_transaction
    },
    COMPUTED_local_currently_viewed_job_offer () {
      return this.currently_viewed_job_offer
    },
    self_store () {
      return store
    }
  },
  watch: {
    COMPUTED_currently_viewed_job_offer (newObject, oldObject) {
      this.currently_viewed_job_offer = newObject
    }
  },
  components: {
    CompanyMainBalanceTable,
    CompanyInfoBox,
    CompanyApplyForm,
    VueRouter,
    VueScrollTo,
    CompanyTableWithTransactions,
    CompanyMainMenuBoxComponent
  },
  watch: {
  }
}

</script>
