<template>
  <div style="justify-content: center;display: flex;">

      <sui-segments horizontal style="display: flex;flex-direction: column;justify-content: center;">

        <sui-segment style="margin-top: 2em !important; margin-bottom: 2em !important;"  >
          <company-info-box />
        </sui-segment>


        <sui-segment style="width: 100%;display: flex;justify-content: center;">
          <company-table-with-transactions id="top" style="display: flex;justify-content: center;"/>
        </sui-segment>


      </sui-segments>
  </div>
</template>

<style lang="scss">
  @import './Company.css';
</style>

<script type="text/javascript">

  import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
  import CompanyTableWithTransactions
    from '../../CompanyMainPanelComponent/CompanyTableWithTransactions/CompanyTableWithTransactions'
  import VueRouter from 'vue-router'

  export default {
  name: 'Company',
  data () {
    return {
    }
  },
  props: {

  },
  methods: {
  },
  mounted () {
  },
  computed: {
  },
  watch: {
  },
  components: {
    CompanyInfoBox,
    CompanyTableWithTransactions,
    VueRouter
  },
  watch: {
  },
  created () {
  }
}

</script>
