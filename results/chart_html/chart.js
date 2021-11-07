
function perc2color(value){
    //value from 0 to 1
	green_hsl = 120
    var hue=((1-value)*green_hsl).toString(10);
    return ["hsl(",hue,",100%,50%)"].join("");
}

function calculateColorFromEntropy(entropy) {
    return perc2color(entropy/highest_entropy)
}

let x = 100
let y = 500
let htmldata = ''
let highest_entropy = 0
points.forEach((point) => {
    if(highest_entropy < point.entropy) {
		highest_entropy = point.entropy;
	}
});
points.forEach((point) => {
    htmldata += '<circle ' + 
        ' cx="' + (+x + +point.alpha*+1000) + 
        '" cy="' + (+y - +point.k* +20) + 
        '" data-value="' + point.entropy + 
        '" r="' + (point.entropy+2) + 
        '" fill="' + calculateColorFromEntropy(point.entropy) + 
        '"></circle>'
});

document.querySelector('.data').innerHTML = htmldata