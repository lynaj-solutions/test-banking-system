/* eslint-disable */
import axios from 'axios'
import isAfter from "date-fns/is_after";
import subtractMinutes from "date-fns/sub_minutes";
import addSeconds from "date-fns/add_seconds";
import differenceInMinutes from "date-fns/difference_in_minutes";
import differenceInMilliSeconds from "date-fns/difference_in_milliseconds";

const state = {
  loggedIn: false,
  profile: {},
  validation: {email: true},
  authError: false,
  userToken: '',
  userTokenExpirationDate: ''
}

const mutations = {
  login (state) {
    state.loggedIn = true
  },
  setUserToken (state, token) {
    state.userToken = token
  },
  logout (state) {
    state.loggedIn = false
  },
  setProfile (state, payload) {
    state.profile = payload
  },
  setValidationEmail (state, bool) {
    state.validation.email = bool
  },
  setAuthError (state, bool) {
    state.authError = bool
  }
}

const actions = {
  handleToken(context, response) {
    context.commit('setUserToken', response.data.token)
    context.commit('login')
    context.commit('setAuthError', false)

    const tokenExpiryDate = addSeconds(new Date(), 3600);
    const tenMinutesBeforeExpiry = subtractMinutes(tokenExpiryDate, 10);
    const now = new Date();

    setTimeout(
      refreshToken, 
      differenceInMilliSeconds(
        tenMinutesBeforeExpiry
        , now
      )
    );
  },
  postLogin (context, payload) {
    return axios.post('/api/v1/auth/obtain_token/', payload)
      .then(response => {
        handleToken(context, response);   
      })
      .catch(e => {
        context.commit('setAuthError', true)
        console.log(e)
      })
  },
  refreshToken (context, payload) {
    return axios.post('/api/v1/auth/refresh_token/', payload)
      .then(response => {
        handleToken(context, response);
      })
      .catch(e => {
        context.commit('setAuthError', true)
        console.log(e)
      })
  },
  postRegister (context, payload) {
    return axios.post('/api/users/register/', payload)
      .then(response => {
        if (response.data.status === 210) {
          context.commit('setValidationEmail', false)
        } else {
          context.commit('setValidationEmail', true)
          context.commit('login')
          context.commit('setProfile', response.data)
        }
      })
      .catch(e => { console.log(e) })
  },
  getProfile (context) {
    return axios.get('/api/users/profile')
      .then(response => {
        context.commit('login')
        context.commit('setProfile', response.data)
      })
      .catch(e => {
        context.commit('logout')
        console.log(e)
      })
  },
  editUser (context, payload) {
    var avatar = payload.avatar
    delete payload.avatar

    return axios.patch('/api/users/' + payload.id, payload)
      .then(response => {
        // Image upload
        if (typeof avatar === 'object') {
          let data = new FormData()
          data.append('avatar', avatar)
          return axios.patch('/api/users/' + payload.id, data)
        }
      })
      .catch(e => { console.log(e) })
  },
  deleteUser (context, userId) {
    return axios.delete('/api/users/' + userId)
      .then(response => {})
      .catch(e => { console.log(e) })
  },
  passwordReset (context, user) {
    return axios.post('/api/users/password_reset/', user)
      .then(response => { context.commit('setEmailFail', false) })
      .catch(e => { context.commit('setEmailFail', true) })
  },
}

export default {
  state,
  getters,
  mutations,
  actions
}
