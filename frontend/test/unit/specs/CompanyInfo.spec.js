import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyInfoBox from '../../../src/components/CompanyInfo/CompanyInfoBox/CompanyInfoBox'
import SuiVue from "semantic-ui-vue";

Vue.use(SuiVue);


describe('CompanyInfoBox.vue', () => {
  it('renders the correct transaction button', () => {
  const wrapper = mount(CompanyInfoBox);
    expect(wrapper.html()).toContain('<button class="ui bottom attached label company-image-leading-button"');
    expect(wrapper.html()).toContain('Transfer money');
  });
});

