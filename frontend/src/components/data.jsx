import React, { Component } from 'react'
import LineCharts from './Charts'

export default class Data extends Component {
    constructor() {
        super();
        this.state = {
            ts: [],
            bytes_ts: [],
            bytes_fs: []
        };
    };

    componentDidMount() {
        fetch('http://localhost:5000/cf4844bc-a107-4e0a-84e1-fa04d76d388c/1524835943/60/10', {mode: 'cors'})
        .then((response) => response.json())
        .then( (results) => {
            const data = results.result;

            this.setState({
                ts: data.map((res) => res.ts),
                bytes_ts: data.map((res) => res.bytes_fs),
                bytes_fs: data.map((res) => res.bytes_ts),
            });
        })
    }

    render() {
        return (
            <LineCharts data={this.state}/>
        )
    }

}



