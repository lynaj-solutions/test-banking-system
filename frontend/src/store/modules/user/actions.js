/* eslint-disable */
import * as transfer from '../../../api/user/transfer/transfer'
import * as types from './types'
import axios from "axios";

export const fetchAvailableCurrencies = ({ commit, state}) => {
  return new Promise((resolve, reject) => {
    const jobOffers = [];
    axios.get('/api/v1/currencies/'
      ).then(response => {
        commit(
          types.CURRENCIES.SAVE_ALL, {payload: response.data.results}
        );
        resolve();
      })
      .catch(error => {
        reject(types.CURRENCIES.SAVE_ALL, {payload: []})
      })
  })
};

export const fetchUserTransactions = ({ commit, state }) => {
 return new Promise((resolve, reject) => {
   if(localStorage.getItem('jwt') == null || localStorage.getItem('jwt') == "null" || localStorage.getItem('jwt') == undefined){
     var localHeaders = {
     };
   } else {
     var localHeaders = {
       headers: {
         Authorization: 'Bearer ' + localStorage.getItem('jwt')
       }
     };
   }

    axios.get('/api/v1/transactions/',
       localHeaders
    ).then(response => {
       commit(
          types.TRANSACTIONS.SAVE_ALL, {payload: response.data.results}
        );
        resolve();
    })
    .catch(error => {
      reject(types.TRANSACTIONS.SAVE_ALL, {payload: []});
    })
  })
}

export const fetchUserBalances = ({ commit, state }) => {
 return new Promise((resolve, reject) => {
    axios.get('/api/v1/balances/',
{
        headers: {
          Authorization: 'Bearer ' + localStorage.getItem('jwt')
        }
      }
    ).then(response => {
       commit(
          types.BALANCES.SAVE_ALL, {payload: response.data.results}
        );
        resolve();
    })
    .catch(error => {
      reject(types.BALANCES.SAVE_ALL, {payload: []});
    })

})
}

export const initializeTransfer = ({ commit, state }, data) => {
   axios.post('/api/v1/transactions/transfer',
      data.data,
      {
        headers: {
          Authorization: 'Bearer ' + data.token
        }
      }
    ).then(response => {
      resolve(response);
    })
    .catch(error => {
      reject(error);
    });
}

export const fetchTransferRecipients = ({ commit, state}) => {
  return new Promise((resolve, reject) => {
      axios.get('/api/v1/users/'
      ).then(response => {
         commit(
            types.RECIPIENTS.SAVE_ALL, {payload: response.data.results}
          );
          resolve();
      })
      .catch(error => {
        reject(types.RECIPIENTS.SAVE_ALL, {payload: []});
      })

  })
};
