/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueCarousel from 'vue-carousel'
import user from './modules/user'

Vue.use(Vuex);
Vue.use(VueCarousel);

export const store = new Vuex.Store({
  modules: {
    user
  },
  state: {
    userObject: {
      auth: {
        loggedIn: '',
        userToken: '',
        profile: '',
        validation: '',
        authError: ''
      },
      loginStatus: false,
      currentAction: '',
      postedJobOffers: []
    },

    linksObject: {
      homepage: '/',
      main_menu: '/menu',
      transactions: '/menu/transactions',
      job_applications: '/menu/applications',
      job_applications_specified_offer: '/menu/applications/:job_offer_title',
      transferCreate: '/menu/create',
      company_information: '/menu/information'
    }
  },
  mutations: {
    // User Authorization
    login(state) {
      localStorage.setItem('loggedIn', true);
    },
    logout(state) {
      localStorage.setItem('loggedIn', false);
      localStorage.setItem('jwt', null);
    },
    setProfile(state, payload) {
      state.userObject.auth.profile = payload
    },
    setValidationEmail(state, bool) {
      state.userObject.auth.validation.email = bool
    },
    setAuthError(state, bool) {
      state.userObject.auth.authError = bool
    },
    // Mutating Show more BTN flag
    MUTATE_SHOW_MORE_BTN(state, flag_value) {
      state.show_more_btn_flag = flag_value;
    },
    MUTATE_currentAction(state, action) {
      state.userObject.currentAction = action
    }

  },
  getters: {
    GET_SHOW_MORE_BTN: state => state.show_more_btn_flag,
    GET_current_action: state => state.userObject.currentAction,
    GET_USER_isLogged: state => state.userObject.loginStatus,
    GET_LINKS_OBJECT: state => state.linksObject,

    // AUTH GETTERS
    GET_userObject_auth_userToken: state => {
      return localStorage.getItem('jwt');
    },
    GET_userObject_auth_loggedIn: state => localStorage.getItem('loggedIn'),
    GET_userObject_auth_profile: state => state.userObject.auth.profile,
    GET_userObject_auth_validation_email: state => state.userObject.auth.validation.email,
    GET_userObject_auth_authError: state => state.userObject.auth.authError
  },
  actions: {
    // Authorization
    informUserNotLoggedIn({commit, dispatch}, payload) {
      // informing user about fact, that he has been logged out
      payload.swal(
        {
          text: "You have to login - the session is no more valid.",
        }).then(() => {
        // making login window visible
        commit('MUTATE_currentAction', 'login');
        // sync redirecting user to the home page
        payload.router.push('/');
      })
    },
    handleToken({commit, dispatch}, response) {

      localStorage.setItem('jwt', response.data.token);
      commit('login');
      commit('setAuthError', false)


    },
    logoutUser({commit, dispatch}, payload) {
      return new Promise((resolve, reject) => {
        // axios.get('/logout'
        // ).then(response => {
        //   commit('logout');
        //   commit('MUTATE_currentAction', 'createATransfer');
        //   payload.router.push('/');
        //   resolve();
        // })
        // .catch(error => {
        //   reject();
        // })
        commit('logout');
        commit('MUTATE_currentAction', 'createATransfer');
        payload.router.push('/');
        resolve();
      })
    },
    loginUser({commit, dispatch}, payload) {
      return new Promise((resolve, reject) => {
        axios.post('/api/v1/auth/obtain_token/', payload.token
        ).then(response => {
          if (response.status == 200) {
            dispatch('handleToken', response);

            commit('login');
            // making sure that login window will not be displayed anymore
            commit('MUTATE_currentAction', 'createATransfer');
            payload.router.push(store.getters.GET_LINKS_OBJECT.main_menu);
          } else {
            commit('setAuthError', true)
          }
          resolve()
        })
          .catch(error => {
            commit('setAuthError', true);
            reject({data: "Something went wrong"});
          })
      })
    },
    refreshToken({commit, dispatch}, payload) {

      let formattedPayload = {
        'token': payload
      };

      console.log('wysylam formattedPayload: ' + formattedPayload);

      return axios.post('/api/v1/auth/refresh_token/', formattedPayload)
        .then(response => {
          dispatch('handleToken', response);
        })
        .catch(e => {
          commit('setAuthError', true);
        })
    },
    postRegister({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.post(
          '/api/v1/users/register/',
          payload
        )
          .then(response => {



            if (response.status === 201) {

              commit('login');
              commit('setProfile', response.data);

              resolve();

            } else if (response.status === 200) {
              reject("Email already in use!");

            } else if (response.status === 400) {
              commit('setRegistrationError', true);
              reject("Something went wrong");

            }
          })
          .catch(e => {

            console.log("console.log(e);: " + JSON.stringify(e));

            reject("Something went wrong");
          })
      })
    },

  }
});
