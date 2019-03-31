import React, { Component } from 'react';
import ChartComponent from '../models/candlestick_chart/candlestick';

export class CandleStickChart extends Component {
    render() {
        return (
            <form>
                <label>
                    Ticker:&nbsp;&nbsp;
                    <input type="text" name="name" />
                </label>
                <input type="submit" value="Submit" />
            <ChartComponent/>
            <p><i>Press "d" for å tegne, del for å slette, esc for å manuvrere</i></p>
            </form>
        )
    }
}
export default CandleStickChart


