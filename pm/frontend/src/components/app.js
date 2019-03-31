import React, {Component, Fragment} from 'react';

import ReactDOM from 'react-dom';

import Header from './layout/Header';
import ChartComponent from './models/candlestick_chart/candlestick';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header/>
                <div className="container">
                    <form>
                      <label>
                        Ticker:
                        <input type="text" name="name" />
                      </label>
                      <input type="submit" value="Submit" />
                    </form>
                    <ChartComponent/>
                    <p><i>Press "d" for å tegne, del for å slette, esc for å kunne manuvrere</i></p>
                </div>
            </Fragment>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));