// Source: https://codesandbox.io/s/github/rrag/react-stockcharts-examples2/tree/master/examples/CandleStickStockScaleChartWithVolumeBarV3
// https://github.com/rrag/react-stockcharts-examples2

export function getData() {
	const url_string = window.location.href
	var url = new URL(url_string);
	var ticker = url.searchParams.get("name");
	if (ticker==null){
		ticker="Nano"
	}
	const promise = fetch("api/data/tsv/"+ticker)
		.then(response => {
			if (!response.ok) {
				throw Error(response.statusText);
        	}
			return response.json()
		})
		.then(data => {

			var i = 0
			for (i=0;i<data.length;i++){
				data[i]['date'] = new Date(data[i]['date'])
			}

			return data
		})
	.catch(function() {
		window.location = "/incorrect_ticker";
	});
	return promise;
}
