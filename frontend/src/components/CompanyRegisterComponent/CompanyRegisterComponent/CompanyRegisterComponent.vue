<template>
  
  <div style="display: flex; flex-direction: column; justify-content: center;">





        <!-- First Name -->

        <div class="ui input div-email-class">
          <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.firstName.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder="First Name"
                     v-model="form.firstName">
        </div>

        <p v-if="$v.form.firstName.$error" class="help is-danger">This field is required</p>


        <!-- Last Name -->
        
        <div class="ui input div-email-class">
          <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.lastName.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder="Last Name"
                     v-model="form.lastName">
        </div>

        <p v-if="$v.form.lastName.$error" class="help is-danger">This field is required</p>
      
        <!-- Email -->

        <div class="ui input div-email-class">
          <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.email.$error) ? 'ui-input-box-div-is-danger' : '']" type="text" style="width: 80%;" placeholder="E-mail" v-model="form.email">
        </div>

        <p v-if="$v.form.email.$error" class="help is-danger">This e-mail address is invalid</p>

        <!-- Password -->

        <div class="ui input div-email-class">
          <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.password.$error) ? 'ui-input-box-div-is-danger' : '']" type="password" style="width: 80%;" placeholder="Password" v-model:trim="form.password">
        </div>

        <span class="help is-danger" v-if="$v.form.email.$error && !$v.form.password.required">Password is required.</span>
        <span class="help is-danger" v-if="form.password.length > 0 && !(!$v.form.email.$error && $v.form.password.minLength)">Password must have at least {{ $v.form.password.$params.minLength.min }} letters.</span>

        <!-- Password Repeat -->
        <div class="ui input div-email-class">
          <input :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.repeatPassword.$error) ? 'ui-input-box-div-is-danger' : '']" type="password" style="width: 80%;" placeholder="Repeat Password"
                     v-model="form.repeatPassword">
        </div>

        <span class="help is-danger" v-if="$v.form.repeatPassword.$rror && !$v.form.repeatPassword.required">Password is required.</span>
        <span class="help is-danger" v-if="$v.form.repeatPassword.$error && !$v.form.repeatPassword.sameAsPassword">Passwords must be identical.</span>

        <!-- Password Repeat -->

        <transition name="fade">

        <div style="margin-top: 2em;" v-if="!loading">

          <button v-on:click="register" class="large ui button button-login-formatted-button">

            Register

          </button>

        </div>



        <div v-else>
          <circle-loader class="spinner-class" loading="true" color="black" size=135 sizeUnit="px"/>
        </div>

      </transition>

       <div v-on:click="login" style="display: flex;flex-direction: row;justify-content: space-around;">
         <div style="display: flex;flex-direction: row;font-size: 1em !important;line-height: 3em;justify-content: space-evenly;border: 2px solid;border-radius: 6em;-webkit-box-shadow: -20px 20px 0px 0px rgba(0,0,0,0.75);box-shadow: -4px 7px 0px 3px rgba(0,0,0,0.75);margin-bottom: 2em;width: 23%;">
            <div data-v-3ee86246="" class="next-main-div-button next deactivated" style="display: flex;flex-direction: row;border-radius: 1em;background-color: transparent !important;box-shadow: none;">
            <img src="https://image.flaticon.com/icons/svg/65/65251.svg" style="background: transparent;background-color: transparent;margin: 10px 2px 10px 10px;color: transparent !important;"></div>
        </div>
      </div>
  </div>

</template>

<style lang="scss">
  @import './CompanyRegisterComponent.css';
</style>

<script type="text/javascript">
import { store } from '../../../store/store'
import VueSwal from 'vue-swal'
import Toasted from 'vue-toasted'
import { CircleLoader } from '@saeris/vue-spinners'
import {validationMixin} from 'vuelidate'
import {required, email, minLength, sameAs} from 'vuelidate/lib/validators'
import Vuelidate from 'vuelidate'
export default {
  name: 'CompanyRegisterComponent',
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
      },
      repeatPassword: {
        sameAsPassword: sameAs('password')
      },
      firstName: {
        required
      },
      lastName: {
        required
      }
    }
  },
  data () {
    return {
      windowWidth: window.innerWidth,
      form: {
        email: '',
        password: '',
        repeatPassword: '',
        firstName: '',
        lastName: ''
      },
      loading: false
    }
  },
  computed: {
    self_store () {
      return store
    }
  },
  methods: {
    login () {
      store.commit('MUTATE_currentAction', 'login')
    },
    register () {
      var self = this
      this.$v.$touch()
      if (!this.$v.$invalid) {

          console.log('wysylam')
          this.loading = true
          store.dispatch('postRegister', self.form).then((data) => {

            self.login();
            this.$swal('You account has been created. :-)');

          }).catch(error => {

            let toast = self.$toasted.show('<div style="display: flex;flex-direction: column;justify-content: center;"><div style="margin-top: 1em;">' + error + '</div></div>', {
              theme: 'bubble',
              position: 'top-right',
              duration: 25000
            })
            console.log(JSON.stringify(error));

          }).finally( () => {
            self.loading = false;
          })
        }
    }
  },
  components: {
    VueSwal,
    Vuelidate,
    CircleLoader,
    Toasted
  },
  mounted: function () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    })
  }
}

</script>
