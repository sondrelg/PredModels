import React, {Component, Fragment} from 'react';

import ReactDOM from 'react-dom';

import Header from './layout/Header';
import CandleStickChart from './layout/candlestick_chart';
import TreeMapChart from './layout/treemap';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header/>
                <div className="container body">
                    {/*<CandleStickChart/>*/}
                    <TreeMapChart/>
                </div>
            </Fragment>
        )
    }
}
ReactDOM.render(<App/>, document.getElementById('app'));