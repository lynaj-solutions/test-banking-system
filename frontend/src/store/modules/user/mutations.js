/* eslint-disable */
import * as types from './types'
import Vue from 'vue'

export const state = {
  userObject: {
    loginStatus: false,
    currentAction: '',
    RECIPIENTS: [],
    CURRENCIES: [],
    BALANCES: [],
    TRANSACTIONS: [],
  }
};

export const mutations = {
  [types.CURRENCIES.SAVE_ALL] (state, { payload }) {
    state.userObject.CURRENCIES = payload;
  },
  [types.RECIPIENTS.SAVE_ALL] (state, { payload }) {
    state.userObject.RECIPIENTS = payload;
  },
  [types.BALANCES.SAVE_ALL] (state, { payload }) {
    state.userObject.BALANCES = payload;
  },
  [types.TRANSACTIONS.SAVE_ALL] (state, { payload }) {
    state.userObject.TRANSACTIONS = payload;
  },

  // AUTHORIZATION
  [types.LOG_USER_IN] (state) {
    state.userObject.loginStatus = USER_LOGIN_STATUS.LOGGED_IN
  },
  [types.LOG_USER_OFF] (state) {
    state.userObject.loginStatus = USER_LOGIN_STATUS.LOGGED_OFF
  },

};
