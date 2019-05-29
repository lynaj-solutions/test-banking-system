import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyMainBalanceTable from '../../../src/components/CompanyMainPanelComponent/CompanyMainBalanceTable/CompanyMainBalanceTable'
import SuiVue from "semantic-ui-vue";

Vue.use(SuiVue);


describe('CompanyMainBalanceTable.vue', () => {
  it('renders the correct balance table', () => {
    const wrapper = mount(CompanyMainBalanceTable);
    expect(wrapper.html()).toContain('<th>Balance</th>');
    expect(wrapper.html()).toContain('<th>Currency</th>');

  });
});

