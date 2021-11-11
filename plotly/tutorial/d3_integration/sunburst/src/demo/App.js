/* eslint no-magic-numbers: 0 */
import React, { Component } from 'react';

import { Sunburst } from '../lib';


class App extends Component {
    constructor() {
        super();
        this.state = {
            // width: 500,
            // height: 500,
            // padding: 10,
            // innerRadius: 20,
            transitionDuration: 1000,
            selectedPath: ['living room'],
            dataVersion: 1,
            data: {name: 'house',
                   children: [{name: 'living room',
                               children: [{name: 'couch', size: 5},
                                          {name: 'tv', size: 3},
                                          {name: 'desk', size: 4},
                                          {name: 'chair', size: 1},
                                          {name: 'table', size: 4},
                                          {name: 'piano', sie: 2}]},
                              {name: 'kitchen',
                               color: '#006',
                               children: [
                                   {name: 'fridge', size: 3, color: '#060'},
                                   {name: 'dishwasher', size: 2, color: '#600'},
                                   {name: 'sink', size: 1},
                                   {name: 'cabinets', size: 7},
                                   {name: 'oven', size: 2}]},
                              {name: 'coat closet', size: 4},
                              {name: 'storage closet', size: 10},

            }
        }
    }
}
