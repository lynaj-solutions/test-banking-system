import { mount } from '@vue/test-utils'
import Vue from 'vue'
import Company from '../../../src/components/Company/Company/Company'
import SuiVue from "semantic-ui-vue";

Vue.use(SuiVue);


describe('Company.vue', () => {

  it('renders the correct transaction button', () => {
  const wrapper = mount(Company);
    expect(wrapper.html()).toContain('<button class="ui bottom attached label company-image-leading-button"');
    expect(wrapper.html()).toContain('Transfer money');
  })

  it('renders the correct transaction table', () => {
  const wrapper = mount(Company);
    expect(wrapper.html()).toContain('<tr><th>Recipient</th> <th>Sender</th> <th>From Currency</th> <th>To Currency</th> <th>Value</th> <th>Exchange Rate</th> <th>Created At</th> <th>Status</th></tr>');
  })

  it('transaction button click should render the login view', () => {
    const wrapper = mount(Company);
    expect(wrapper.html()).not.toContain('<input type="password" placeholder="Password" class="input ui-input-box-div ui-input-box-div-text" style="width: 80%;">');
    const button = wrapper.find('button');
    button.trigger('click');
    expect(wrapper.html()).toContain('<input type="password" placeholder="Password" class="input ui-input-box-div ui-input-box-div-text" style="width: 80%;">');
  })

  it('registration button click should render the registration view', () => {
    const wrapper = mount(Company);
    expect(wrapper.html()).not.toContain('<input type="text" placeholder="Last Name" class="input ui-input-box-div ui-input-box-div-text" style="width: 80%;">');
    const img_button = wrapper.find('img');
    img_button .trigger('click');
    expect(wrapper.html()).toContain('<input type="text" placeholder="Last Name" class="input ui-input-box-div ui-input-box-div-text" style="width: 80%;">');
  })
})