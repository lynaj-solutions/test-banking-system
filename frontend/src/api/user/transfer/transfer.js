/* eslint-disable */
import axios from "axios";

export default {
  initializeMoneyTransfer (data, cb) {
    axios.post('/api/v1/transactions/transfer',
      data.data,
      {
        headers: {
          Authorization: 'Bearer ' + data.token
        }
      }
    ).then(response => {
      if (response.status == 200) {
        cb(response);
      }
    })
      .catch(error => {
        cb(error);
      });
  },

  transferFetchAvailableCurrencies(cb) {
    axios.get('/api/v1/currencies/'
      ).then(response => {
        cb(response.results);
      })
      .catch(error => {
        cb(error)
      })
  },

  transferFetchTransferRecipients (cb) {
    axios.get('/api/v1/users/'
      ).then(response => {
        cb(response);
      })
      .catch(error => {
        cb(error)
      })
  }
}

