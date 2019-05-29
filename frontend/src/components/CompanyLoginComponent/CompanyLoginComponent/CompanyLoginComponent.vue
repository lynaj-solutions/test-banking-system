
<template>

  <div style="display: flex; flex-direction: column; justify-content: center;">

    <!-- email -->
    <div class="ui input div-email-class">
      <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.email.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder="E-mail" v-model="form.email">
    </div>

    <p v-if="$v.form.email.$error" class="help is-danger">This e-mail address is invalid</p>
    <!-- end of email -->
    <!-- password -->
    <div class="ui input">
      <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.password.$error) ? 'ui-input-box-div-is-danger' : '']" type="password" style="width: 80%;" placeholder="Password" v-model:trim="form.password">
    </div>

    <span class="help is-danger" v-if="$v.form.email.$error && !$v.form.password.required">Password is required.</span>
    <span class="help is-danger" v-if="form.password.length > 0 && !(!$v.form.email.$error && $v.form.password.minLength)">Password must have at least {{ $v.form.password.$params.minLength.min }} letters.</span>

    <!-- end of password -->

    <vue-recaptcha
      ref="recaptcha"
      @verify="onCaptchaVerified"
      @expired="onCaptchaExpired"
      size="invisible"
      sitekey="6LdG_JgUAAAAAHp9zdX0Tz_LbW6iYyIGlY0MJj3m">
    </vue-recaptcha>

    <transition name="fade">

      <div style="margin-top: 2em;" v-if="!loading">

        <button v-on:click="login" class="large ui button button-login-formatted-button">

          Login

        </button>

      </div>

      <div v-else>
        <circle-loader class="spinner-class" loading=true color="black" size="135" sizeUnit="px"/>
      </div>

    </transition>

     <div style="display: flex;flex-direction: row;justify-content: space-around;">
       <div v-on:click="register" style="display: flex;flex-direction: row;font-size: 1em !important;line-height: 3em;justify-content: space-evenly;border: 2px solid;border-radius: 6em;-webkit-box-shadow: -20px 20px 0px 0px rgba(0,0,0,0.75);box-shadow: -4px 7px 0px 3px rgba(0,0,0,0.75);margin-bottom: 2em;width: 23%;">
          <div data-v-3ee86246="" class="next-main-div-button next deactivated" style="display: flex;flex-direction: row;border-radius: 1em;background-color: transparent !important;box-shadow: none;">
          <img src="https://image.flaticon.com/icons/svg/65/65251.svg" style="background: transparent;background-color: transparent;margin: 10px 2px 10px 10px;color: transparent !important;"></div>
       </div>

    </div>

  </div>


</template>

<style lang="scss">
  @import './CompanyLoginComponent.css';
</style>

<script type="text/javascript">
import { store } from '../../../store/store'
import VueSwal from 'vue-swal'
import { CircleLoader } from '@saeris/vue-spinners'
import {validationMixin} from 'vuelidate'
import {required, email, minLength} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'
import VueRecaptcha from 'vue-recaptcha'
import VueRouter from 'vue-router'


export default {
  name: 'CompanyLoginComponent',
  mixins: [validationMixin],
  validations: {
    form: {
      email: {
        required,
        email
      },
      password: {
        required,
        minLength: minLength(6)
      }
    }
  },
  watch: {
    COMPUTED_AuthError (newObject, oldObject) {
      if(newObject == true) {
        this.$swal('Used login credentials are wrong!!');
        store.commit('setAuthError', false)
      }
    },
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      form: {
        email: '',
        password: ''
      },
      loading: false
    }
  },
  computed: {
    COMPUTED_AuthError () {
      return store.getters.GET_userObject_auth_authError
    },
    self_store () {
      return store
    }
  },
  methods: {
    login () {
      var self = this
      this.$v.$touch()
      if (!self.$v.$invalid) {
        var obtainedData = {
          token: self.form,
          router: this.$router
        }
        self.loading = true
        store.dispatch('loginUser', obtainedData).then(() => {
          self.loading = false;
        }).catch(error => {
          self.loading = false;
          console.log(error)
        })
      }
    },
    register () {
      store.commit('MUTATE_currentAction', 'register')
    },
    resetPassword () {
      store.commit('MUTATE_currentAction', 'resetPasword')
    },
    onCaptchaVerified: function (recaptchaToken) {
      const self = this
      self.$refs.recaptcha.reset()
      var obtainedData = self.form
      console.log('onCaptchaVerified: ' + recaptchaToken)
      obtainedData.recaptchaToken = recaptchaToken;

      var obtainedData = {
        token: self.form,
        router: this.$router
      }

      store.dispatch('loginUser', obtainedData).then(() => {
        self.loading = false
      }).catch(error => {
        console.log(error)
      })
    },
    // reseting captcha
    onCaptchaExpired: function () {
      this.$refs.recaptcha.reset()
    }

  },
  components: {
    VueSwal,
    Vuelidate,
    CircleLoader,
    VueRouter,
    VueRecaptcha
  },
  mounted: function () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })
  }
}

</script>
