import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyRegisterComponent from '../../../src/components/CompanyRegisterComponent/CompanyRegisterComponent/CompanyRegisterComponent'
import SuiVue from "semantic-ui-vue";

Vue.use(SuiVue);


describe('CompanyRegisterComponent.vue', () => {
  it('contains basic div class', () => {
    const wrapper = mount(CompanyRegisterComponent);
    expect(wrapper.html()).toContain('<div class="ui input div-email-class">');
  });
});

