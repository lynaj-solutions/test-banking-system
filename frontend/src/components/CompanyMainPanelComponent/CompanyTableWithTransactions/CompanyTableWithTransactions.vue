<template>

  <transition name="fade">

    <div v-if="loading_state == true">
      <circle-loader class="spinner-class" loading=true color="black" size="135" sizeUnit="px"/>
    </div>

    <div v-else style="display: flex;justify-content: center;">
      <table class="ui celled padded table ui label"
             style="width: auto; border: 1px solid;box-shadow: 2px azure !important; background-color: #f0f0f0;color: gray;">

        <tr>
          <th>Recipient</th>
          <th>Sender</th>
          <th>From Currency</th>
          <th>To Currency</th>
          <th>Value</th>
          <th>Exchange Rate</th>
          <th>Created At</th>
          <th>Status</th>
        </tr>
        <template v-for="item in self_store.getters['user/GET_TRANSACTIONS']" class="ui celled padded table">
          <tr :style="METHOD_style_tr(item.status)">

            <th>{{ item.recipient }}</th>
            <th>{{ item.sender }}</th>
            <th>{{ item.fromc }}</th>
            <th>{{ item.toc }}</th>
            <th>{{ item.value }}</th>
            <th>{{ item.rate }}</th>
            <th>{{ item.created_at }}</th>
            <th>{{ item.status }}</th>
          </tr>
        </template>
      </table>
    </div>
  </transition>


</template>

<style lang="scss">
  @import './CompanyTableWithTransactions.css';
</style>

<script type="text/javascript">

  import {store} from '../../../store/store'
  import {CircleLoader} from '@saeris/vue-spinners'

  export default {
    name: 'CompanyTableWithTransactions',
    methods: {
      METHOD_style_tr(status) {
        var computedStyle = '';
        if (status !== "Failed") {
          computedStyle = "background: #c9ffc9;";
        } else {
          computedStyle = "background: #ffbebe;"
        }
        return computedStyle
      }
    },
    data() {
      return {
        loading_state: true
      }
    },
    computed: {
      self_store() {
        return store
      }
    },
    components: {
      CircleLoader
    },
    data() {
      return {
        tableObject: {
          title: 'Transactions',
          loading: true,
          emptyDataListMessage: 'You have not created any transactions yet.'
        }
      }
    },
    mounted() {
      var self = this;

      store.dispatch('user/fetchUserTransactions').then(() => {
      }).catch((e) => {
      }).finally(() => {
      });

    },

  }

</script>
