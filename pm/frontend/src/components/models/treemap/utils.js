export function getData() {
	const promise = fetch("api/data/daily/")
		.then(response => {
			if (!response.ok) {
				throw Error(response.statusText);
        	}
			return response.json()
		})
		.then(data => {
		    console.log(data)
			return data
		})
	.catch(function() {

		window.location = "/incorrect_ticker";
		console.log(data)
	});
	return promise;
}
