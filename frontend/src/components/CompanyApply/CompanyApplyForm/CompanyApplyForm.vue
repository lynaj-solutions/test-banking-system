<template>

  <div>


    <transition name="fadeslower">
      <div v-if="COMPUTED_displaySuccess && COMPUTED_allowToDisplayMessage">

        <div>
          Your application has ben successfuly sent!
        </div>

      </div>
    </transition>

    <transition name="fadeslower">
      <div v-if="COMPUTED_displayWarning && COMPUTED_allowToDisplayMessage">

        <div
          style="margin-top: 2em !important; display: flex !important;justify-content: center;font-size: 3em;line-height: 2em;background: rgba(255,98,41,1);background: -moz-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: -webkit-gradient(left top, right top, color-stop(0%, rgba(255,98,41,1)), color-stop(20%, rgba(246,126,85,0.98)), color-stop(60%, rgba(255,63,5,0.93)), color-stop(78%, rgba(255,98,41,0.91)), color-stop(89%, rgba(248,71,18,0.9)), color-stop(96%, rgba(242,72,27,0.89)), color-stop(100%, rgba(238,73,32,0.89)));background: -webkit-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: -o-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: -ms-linear-gradient(left, rgba(255,98,41,1) 0%, rgba(246,126,85,0.98) 20%, rgba(255,63,5,0.93) 60%, rgba(255,98,41,0.91) 78%, rgba(248,71,18,0.9) 89%, rgba(242,72,27,0.89) 96%, rgba(238,73,32,0.89) 100%);background: #ffe1e1;filter: progid: DXImageTransform.Microsoft.gradient( startColorstr='#ff6229', endColorstr='#ee4920', GradientType=1 );max-width: 22em;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;display: flex;flex-direction: column;border-radius: 10px 10px 10px 10px;-moz-border-radius: 10px 10px 10px 10px;-webkit-border-radius: 10px 10px 10px 10px;-webkit-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);-moz-box-shadow: -35px 35px 1px 0px rgba(0,0,0,0.75);box-shadow: -8px 7px 5px 0px rgba(255, 61, 61, 0.8);margin: auto;text-shadow: -3px 1px 0px rgb(241, 137, 137);text-align: center;">
          Something went wrong! Please, try again later!
        </div>

      </div>
    </transition>


    <section v-if="!COMPUTED_displaySuccess && !COMPUTED_displayWarning" class="section">
      <div class="container">
        <div class="div-main-container-apply-form">
          <div>

            <template>

              <div style="text-align: left;display: flex;flex-direction: column;justify-content: center;">

                <div id="top" class="apply-form-first-step-sub-div" style="float: left;display: block;margin: auto;">


                  <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
                    <label class="label">Recipient</label>
                    <div class="control">
                      <multiselect
                        :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.recipient.$error) ? 'ui-input-box-div-is-danger' : '']"
                        :searchable="true" :close-on-select="true" :show-labels="false"
                        placeholder="Choose recipient email" :multiple="false" v-model="form.recipient"
                        :options="arrayOfRecipients"></multiselect>
                    </div>
                    <p v-if="$v.form.recipient.$error" class="help is-danger">This field is required.</p>
                  </div>


                  <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
                    <label class="label">From Currency</label>
                    <div class="control">
                      <multiselect
                        :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.fromCurrency.$error) ? 'ui-input-box-div-is-danger' : '']"
                        :searchable="true" :close-on-select="true" :show-labels="false"
                        placeholder="Choose proper currency" :multiple="false" v-model="form.fromCurrency"
                        :options="arrayOfCurrencies"></multiselect>
                    </div>
                    <p v-if="$v.form.fromCurrency.$error" class="help is-danger">This field is required.</p>
                  </div>

                  <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
                    <label class="label">To Currency</label>
                    <div class="control">
                      <multiselect
                        :class="['input ui-input-box-div ui-input-box-div-text', ($v.form.toCurrency.$error) ? 'ui-input-box-div-is-danger' : '']"
                        :searchable="true" :close-on-select="true" :show-labels="false"
                        placeholder="Choose proper currency" :multiple="false" v-model="form.toCurrency"
                        :options="arrayOfCurrencies"></multiselect>
                    </div>
                    <p v-if="$v.form.toCurrency.$error" class="help is-danger">This field is required.</p>
                  </div>

                  <div style="margin: 3em 3em 3em 3em;width: 100%;" class="field">
                    <label class="label">Transaction Value</label>
                    <div class="control">

                      <input placeholder="5000"
                             :class="['input ui-input-box-div input-input-box-div-text', ($v.form.value.$error) ? 'ui-input-box-div-is-danger' : '']"
                             type="text" style="width: 80%;"
                             v-model="form.value">
                    </div>
                    <p v-if="$v.form.value.$error" class="help is-danger">This field is required.<br>Only integer/float
                      values are valid.</p>
                  </div>

                </div>
              </div>

            </template>

          </div>

        </div>

        <!--Post job offer button-->
        <transition name="fade">
          <div v-if="!loading">

            <div style="margin-top: 2em !important;" @click="initializeTransfer" data-v-3ee86246=""
                 class="bottom only-next">

              <button class="next-main-div-button stepper-button next deactivated" id="transferspan" data-v-3ee86246="">
                Transfer
              </button>

            </div>

          </div>

          <div v-else>
            <circle-loader class="spinner-class" loading=true color="black" size="135" sizeUnit="px"/>
          </div>
        </transition>

      </div>
    </section>
  </div>
</template>

<style lang="scss">
  @import './CompanyApplyForm.css';
</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<script type="text/javascript">
  import {store} from '../../../store/store'
  import VueSwal from 'vue-swal'
  import Vuelidate, {validationMixin} from 'vuelidate'
  import {between, required} from 'vuelidate/lib/validators'
  import VueRecaptcha from 'vue-recaptcha'
  import Toasted from 'vue-toasted'
  import Multiselect from 'vue-multiselect'

  var VueScrollTo = require('vue-scrollto');

  export default {
    name: 'CompanyApplyForm',
    mixins: [validationMixin],
    validations: {
      form: {
        recipient: {
          required
        },
        fromCurrency: {
          required
        },
        toCurrency: {
          required
        },
        value: {
          required,
          between: between(0, 100000000)
        }
      }
    },
    data() {
      return {
        arrayOfRecipients: [],
        arrayOfCurrencies: [],
        windowWidth: window.innerWidth,
        displayWarning: false,
        displaySuccess: false,
        allowToDisplayMessage: false,
        form: {
          recipient: '',
          fromCurrency: '',
          toCurrency: '',
          value: '',
          loading: false
        }
      }
    },
    components: {
      VueScrollTo,
      Toasted,
      VueSwal,
      Vuelidate,
      VueRecaptcha,
      'multiselect': Multiselect
    },
    methods: {
      METHOD_resetCurrentView() {
        store.commit('MUTATE_currentAction', '')
      },
      METHOD_checkBalance(fromCurrency, transferValue) {
        try{
          var matchedBalance = store.getters['user/GET_BALANCES'].filter(
            queriedBalance => queriedBalance.currency == fromCurrency
          );
        } catch(e) {
          var matchedBalance = [{ value: 0 }];
        }

        console.log('matchedBalance : ' + matchedBalance.toString());
        if (matchedBalance !== undefined && matchedBalance != '' && matchedBalance.length > 0) {
          // checking if user has enough funds to process this transfer
          if (matchedBalance[0].value >= transferValue) {
            return true;
          } else {
            return false;
          }
        } else {
          return false;
        }
      },
      initializeTransfer() {
        var self = this;
        this.$v.$touch();
        // is logged in
        if (!self.$v.$invalid) {
          {
            if(self.form.value !== undefined) {
              var transferValue = self.form.value;
            } else {
              var transferValue = 0;
            }
            if (this.METHOD_checkBalance(self.form.fromCurrency, self.form.value) == true) {
              var obtainedData = {
                data: self.form,
                token: localStorage.getItem('jwt')
              };

              store.dispatch('user/initializeTransfer', obtainedData).then((response) => {
                this.$swal('Congratulation! Your transfer has been succesfully created!').then(() => {
                  this.$router.push('/');
                });
                self.loading = false;
                self.METHOD_resetCurrentView()
              }).catch(error => {
                this.$swal('Oopss! Something went wrong')
              })
              // } else {
              //   this.$route.push(store.getters.GET_LINKS_OBJECT.job_offers);
              // }
            } else {
              this.$swal('You have to raise more capital before processing this transfer.')
            }

          }
        }
      }
    },
    watch: {
      clickedNext(val) {
        if (val === true) {
          this.$v.form.$touch()
        }
      }
    },
    mounted() {
      var self = this;
      store.dispatch('user/fetchAvailableCurrencies').then((response) => {
        self.arrayOfCurrencies = store.getters['user/GET_CURRENCIES'].map(
          currency => currency.abbreviation
        );
        store.dispatch('user/fetchTransferRecipients').then(() => {
          self.arrayOfRecipients = store.getters['user/GET_RECIPIENTS'].map(
            recipient => recipient.email
          );
        }).catch((e) => {
          console.log(e);
        })
      }).catch((e) => {
        console.log(e);
      });

      window.addEventListener('resize', () => {
        this.windowWidth = window.innerWidth
      });
      if (!this.$v.$invalid) {
        this.$emit('can-continue', {value: true})
      } else {
        this.$emit('can-continue', {value: false})
      }
    }
  }

</script>
