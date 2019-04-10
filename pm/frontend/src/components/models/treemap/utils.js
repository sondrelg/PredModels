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
	});
	return promise;
}
{/*export function getData() {
    const data = [
            { ticker:'Apple', name:'Apple', change:0.05, value:5000 },
            { ticker:'Mango', name:'Mango', change:-0.05, value:3000 },
            { ticker:'Orange', name:'Orange', change:0.02, value:2300 },
            { ticker:'Banana', name:'Banana', change:-0.02, value:500 },
            { ticker:'Grape', name:'Grape', change:0.01, value:4300 },
            { ticker:'Papaya', name:'Papaya', change:-0.01, value:1200 },
            { ticker:'Melon', name:'Melon', change:0, value:4500 }
        ]
    return data
}*/}