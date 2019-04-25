import React from 'react'
import { Line } from 'react-chartjs-2';

const LineChart = (props) => {
    const pretty_ts = props.data.ts.map((ts) => (new Date(ts*1000)).toLocaleTimeString());
    console.log(props.data.ts);
    const chartData = {
        labels: pretty_ts,
        datasets: [{
            label: 'Bytes to Server',
            backgroundColor: '#75DDDD',
            borderColor: '#17BEBB',
            fill: false,
            data: props.data.bytes_ts
        }, {
            label: 'Bytes from Server',
            backgroundColor: '#84C7D0',
            borderColor: '#1F5673',
            fill: false,
            data: props.data.bytes_fs
        }]
    };
    const chartOptions = {
        scales: {
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Number of bytes'
                }
            }],
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Date and Time'
                }
            }]
        },
        title: {
            display: true,
            text: 'Byte Traffic Data'
        }
    };
    return (
        <Line data={chartData} options={chartOptions} redraw />
    )
};
    export default LineChart;
