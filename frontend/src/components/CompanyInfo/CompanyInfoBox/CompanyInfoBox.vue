<template>
  <transition name="slide">
    <div style="display: flex; justify-content: center;">

      <transition name="fade">

      <div  v-if="self_store.getters.GET_current_action == '' || self_store.getters.GET_current_action == 'createATransfer'" class="ui card company-info-box-main-class">

        <div v-on:click="createATransfer">

          <div class="ui card company-info-box-main-class" style="height: 7em;">
            <button class="ui bottom attached label company-image-leading-button"
                    style="background-color: rgb(33, 186, 69); color: rgb(255, 255, 255);height: 100% !important;"><i
              class="icon user"></i>Transfer money
            </button>
          </div>

        </div>

      </div>


        <div v-else-if="self_store.getters.GET_current_action == 'login'">
          <company-login-component/>
        </div>

        <div v-else-if="self_store.getters.GET_current_action == 'register'">
          <company-register-component/>
        </div>


      </transition>

    </div>
  </transition>

</template>

<style lang="scss">
  @import './CompanyInfoBox.css';
</style>

<script type="text/javascript">

  import {store} from '../../../store/store'
  import CompanyLoginComponent from '../../CompanyLoginComponent/CompanyLoginComponent/CompanyLoginComponent.vue'
  import CompanyRegisterComponent
    from '../../CompanyRegisterComponent/CompanyRegisterComponent/CompanyRegisterComponent.vue'
  import VueRouter from 'vue-router'

  var VueScrollTo = require('vue-scrollto')

  export default {
    name: 'CompanyInfoBox',
    data() {
      return {
      }
    },
    props: {},
    components: {
      CompanyRegisterComponent,
      CompanyLoginComponent,
      VueScrollTo,
      VueRouter
    },
    computed: {
      self_store() {
        return store
      }
    },
    methods: {
      createATransfer: function () {
        var loggedInStatus = localStorage.getItem('loggedIn');
        if (loggedInStatus !== null
          && loggedInStatus.toString() === "true") {
          this.$router.push(store.getters.GET_LINKS_OBJECT.transferCreate);
          VueScrollTo.scrollTo('#top', 500);
          store.commit('MUTATE_currentAction', 'createATransfer')
        } else {
          store.commit('MUTATE_currentAction', 'login');
        }
      }
    },
    mounted() {
    },
  }

</script>
