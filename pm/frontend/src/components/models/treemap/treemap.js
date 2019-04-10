import * as React from "react";
import * as ReactDOM from "react-dom";
import { TreeMapComponent, Inject, TreeMapTooltip, TreeMapLegend } from '@syncfusion/ej2-react-treemap';
import { getData } from "./utils"

export class ChartComponent extends React.Component {
	componentDidMount() {
		getData().then(data => {
			this.setState({ data })
		})
	}

    render() {
        if (this.state == null) {
            return <div>Loading...</div>
        }
        return ( <TreeMapComponent id='treemap'
            dataSource={this.state.data}
            weightValuePath='value'
            rangeColorValuePath='change'

            legendSettings= {{
                visible: true,
                position: 'Top',
                valuePath: 'level'
            }}
            leafItemSettings={{
                labelPath: 'ticker',
                colorMapping:[
                    { from:-3, to:-2, minOpacity:0.5, legendLabel: '-2%', maxOpacity:0.8, color:'#bf4045' },
                    { from:-2, to:-1, minOpacity:0.5, legendLabel: '-1%', maxOpacity:0.8, color:'#8b444e' },
                    { from:-1, to:1, minOpacity:0.5, legendLabel: '0%', maxOpacity:0.8, color:'#414554' },
                    { from:1, to:2, minOpacity:0.5, legendLabel: '1%', maxOpacity:0.8, color:'#35764e' },
                    { from:2, to:3, minOpacity:0.5, legendLabel: '2%', maxOpacity:0.8, color:'#2f9e4f' },
                    { from:3, to:1000, legendLabel: '3%', color:'#30cc5a' }
                ]
            }}
            tooltipSettings= {{ visible: true, template:'<div><p>Company: ${name}</p><p>Change: ${change}</p><p>Value: ${value}</p></div>' }}>
            <Inject services={[TreeMapTooltip, TreeMapLegend ]} />
        </TreeMapComponent> );
    }
}
export default ChartComponent
