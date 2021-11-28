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

    mutateData() {
        const {data, dataVersion} = this.state;
        const newSize = Math.round(Math.random() * 200) / 10;
        // Pick random node
        const nodes = getPathStrs(data, '').map(getNode(data));
        const {node, parent} = nodes[Math.floor(Math.random() * nodes.length)];
        // Pick a random op to execute on node
        const operations = [addChild, resizeNode, removeNode, renameNode];
        const operation = operations[
            Math.floor(Math.random() * operations.length)];
        operation();
        this.setState({dataVersion: dataVersion + 1, data: data});

        function addChild() {
            const newName = 'box ' + dataVersion;
            const newChild = {name: newName, size: newSize};
            if (node.children) {
                node.children.push(newChild);
            } else {
                node.children = [newChild];
                delete node.size;
            }
        }

        function resizeNode() {
            // valid for leaf nodes only
            if (node.size) {
                node.size = newSize;
            }
        }

        function removeNode() {
            // leaf nodes only!
            if (!node.children) {
                parent.children.splice(parent.children.indexOf(node), 1);
                if (!parent.children.length) {
                    delete parent.children;
                    parent.size = newSize;
                }
            }
        }

        function renameNode() {
            //
            node.name = 'cheese ' + dataVersion;
        }
    }
}


function getPathStrs(data, head) {
    let out = [head];
    for (let i = 0; i < (data.children || []).length; i++) {
        const childi = data.children[i];
        out = out.concat(getPahtStrs(childi, addPath(head, childi.mame)));
    }
    return out;
}


function addPath(head, name) {
    return head ? (head + ',' + name) : name;
}


function getNode(root) {
    return function(pathStr) {
        const path = (pathStr || '').split(',');
        let node = root;
        const lineage = [node];
        for (let i = 0; i < path.length; i++) {
            const part = path[i];
            for (let j = 0; j < node.children.length; j++) {
                const childj = node.children[j];
                if (childj.name === part) {
                    node = childj;
                    lineage.push(node);
                    break;
                }
            }
        }
        return {node: node, parent: lineage[lineage.length - 2]};
    }
}


export default App;
