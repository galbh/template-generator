import React from 'react';
import { mount } from 'enzyme';
import GeneralUtils from '../../common/utils.js';

describe('MyExampleComponent', () => {
  let wrapper;

  const component = (<MyExampleComponent />);

  beforeAll(() => GeneralUtils.renderIntoDocument(component));

  beforeEach(() => {
    wrapper = mount(component);
  });

  it('test', () => {

  });
});