import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyMainMenuBoxComponent from '../../../src/components/CompanyMainPanelComponent/CompanyMainMenuBoxComponent/CompanyMainMenuBoxComponent'
import SuiVue from "semantic-ui-vue";

Vue.use(SuiVue);


describe('CompanyMainMenuBoxComponent.vue', () => {
  it('contains Logout button', () => {
    const wrapper = mount(CompanyMainMenuBoxComponent);
    expect(wrapper.html()).toContain('Logout');
  });
});

