<template>

  <div :class="COMPUTED_class_object">
    <template v-for="item in menuItems">

      <a v-on:click="METHOD_emitMenuItemChange(item.id)" class="item">
        <i :class="item.class"></i>
        {{ item.title }}
      </a>

    </template>

    <a class="item" v-on:click="METHOD_logout_button">
      Logout
    </a>

  </div>

</template>

<style lang="scss">
  @import './CompanyMainMenuBoxComponent.css';
</style>

<script type="text/javascript">

import { store } from '../../../store/store'
import CompanyInfoBox from '../../CompanyInfo/CompanyInfoBox/CompanyInfoBox.vue'
import CompanyApplyForm from '../../CompanyApply/CompanyApplyForm/CompanyApplyForm.vue'
import VueRouter from 'vue-router'

export default {
  name: 'CompanyMainMenuBoxComponent',
  data () {
    return {
      windowWidth: window.innerWidth
    }
  },
  props: {
    menuItems: []
  },
  methods: {
    METHOD_logout_button() {
        let payload = {
          router: this.$router
        };
        store.dispatch('logoutUser', payload);
    },
    isEmpty: function (obj) {
      for (var key in obj) {
        if (obj.hasOwnProperty(key)) { return false }
      }
      return true
    },
    METHOD_change_path: function (nameOfThePath) {
      if (nameOfThePath == 'login') {
        store.commit('MUTATE_currentAction', 'login')
      }
      this.$router.push(nameOfThePath)
    },
    METHOD_emitMenuItemChange: function (id) {
      this.$emit('changedMenuItem', {id: id})
    }
  },
  mounted () {
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
      console.log(this.isMobile)
    })
  },
  computed: {
    COMPUTED_class_object() {
      if (this.windowWidth <= 1200  && this.windowWidth >= 600) {
        return 'ui horizontal labeled menu';
      }
      else {
        return 'ui vertical labeled menu';
      }
    },
    self_store () {
      return store
    }
  },
  watch: {
  },
  components: {
    CompanyInfoBox,
    CompanyApplyForm,
    VueRouter
  },
  watch: {
  },
  created () {
  }
}

</script>
