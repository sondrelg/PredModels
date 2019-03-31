import React, {Component, Fragment} from 'react';

import ReactDOM from 'react-dom';

import Header from './layout/Header';
import CandleStickChart from './layout/candlestick_chart';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header/>
                <div className="container">
                    <CandleStickChart/>
                </div>
            </Fragment>
        )
    }
}
ReactDOM.render(<App/>, document.getElementById('app'));