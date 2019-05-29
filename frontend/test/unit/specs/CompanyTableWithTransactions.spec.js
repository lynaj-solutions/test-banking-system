import { mount } from '@vue/test-utils'
import Vue from 'vue'
import CompanyTableWithTransactions from '../../../src/components/CompanyMainPanelComponent/CompanyTableWithTransactions/CompanyTableWithTransactions'
import SuiVue from "semantic-ui-vue";


Vue.use(SuiVue);


describe('CompanyTableWithTransactions.vue', () => {
  it('contains basic table\'s header', () => {
    const wrapper = mount(CompanyTableWithTransactions);

    expect(wrapper.html()).toContain('<th>To Currency</th>');
    expect(wrapper.html()).toContain('<th>Recipient</th>');
    expect(wrapper.html()).toContain('<th>Sender</th>');
    expect(wrapper.html()).toContain('<th>Status</th>');
    expect(wrapper.html()).toContain('<th>Created At</th>');
    expect(wrapper.html()).toContain('<th>From Currency</th>');
    expect(wrapper.html()).toContain('<th>Exchange Rate</th>');
    expect(wrapper.html()).toContain('<th>Value</th>');

  });
});

