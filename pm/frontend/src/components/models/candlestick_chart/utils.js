// Source: https://codesandbox.io/s/github/rrag/react-stockcharts-examples2/tree/master/examples/CandleStickStockScaleChartWithVolumeBarV3

export function getData() {
	const promise = fetch("api/data/tsv/nano")
		.then(response => response.json())
		.then(data => {

			var i = 0
			for (i=0;i<data.length;i++){
				data[i]['date'] = new Date(data[i]['date'])
			}

			return data
		})
	return promise;
}
