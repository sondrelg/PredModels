// Source: https://codesandbox.io/s/github/rrag/react-stockcharts-examples2/tree/master/examples/CandleStickStockScaleChartWithVolumeBarV3

export function getData() {
	const url_string = window.location.href
	var url = new URL(url_string);
	var ticker = url.searchParams.get("name");
	if (ticker==null){
		ticker="NHY"
	}
	const promise = fetch("api/data/tsv/"+ticker)
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
