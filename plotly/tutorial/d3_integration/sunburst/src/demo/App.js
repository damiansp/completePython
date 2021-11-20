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
                              {name: 'bathroom', size: 6},
                              {name: 'master bedroom',
                               children: [{name: 'bed', size: 8},
                                          {name: 'recliner', size: 3},
                                          {name: 'dresser', size: 4},
                                          {name: 'master bath', size: 6},
                                          {name: 'closet', size: 5}]},
                              {name: 'bedroom',
                               children: [{name: 'bed', size: 5},
                                          {name: 'desk', size: 3},
                                          {name: 'dresser', size: 4},
                                          {name: 'closet', size: 5}]},
                              {name: 'hall', size: 10}]}}
        this.setProps = this.setProps.bind(this);
        this.mutateData = this.mutateData.bind(this);
        this.period = 3;
        this.updateInterval = setInterval(this.mutateData, 1000 * this.period);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        const {data, selectedPath} = this.state;
        const selectedPathStr = selectedPath.join(',');
        const paths = getPathStrs(data, '');
        const options = paths.map(path => (
            <option value={path} key={path}>
                {path.split(',').join('->') || 'root'}
            </option>));
        const selectChange = e => {
            this.setstate({selectedPath: e.target.value.split(',')});
        }
        return (
            <div>
                <h2>Sunburst Demo</h2>
                <p>
                    Click a node or select it in the dropdown to select a
                    subtree.
                </p>
                <p>
                    Every {this.period} seconds a node will be added, removed,
                    resized, or renamed.
                </p>
                <Sunburst setProps={this.setProps} {...this.state} />
                <select valu={selectedPathStr} onChange={selectChange}>
                    {options}
                </select>
            </div>);
    }

    mutateData() {}
}
