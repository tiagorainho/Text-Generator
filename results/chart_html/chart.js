
function perc2color(perc) {
	var r, g, b = 0;
	if(perc < 50) {
		r = 255;
		g = Math.round(5.1 * perc);
	}
	else {
		g = 255;
		r = Math.round(510 - 5.10 * perc);
	}
	var h = r * 0x10000 + g * 0x100 + b * 0x1;
	return '#' + ('000000' + h.toString(16)).slice(-6);
}

function calculateColorFromEntropy(entropy) {
    return perc2color((entropy * 100)/6)
}

let x = 100
let y = 500
htmldata = ''
points.forEach((point) => {
    htmldata += '<circle ' + 
        ' cx="' + (+x + +point.alpha*+1000) + 
        '" cy="' + (+y - +point.k* +20) + 
        '" data-value="' + point.entropy + 
        '" r="' + (point.entropy+1) + 
        '" fill="' + calculateColorFromEntropy(point.entropy) + 
        '"></circle>'
});

document.querySelector('.data').innerHTML = htmldata