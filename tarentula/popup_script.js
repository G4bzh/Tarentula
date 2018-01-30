////////////////
// Variables //
//////////////

var queryInfo = {"active" : true};
var textURLID = "url";



////////////////
// Functions //
//////////////


// print Tab Url into textURL element
function printURL(textURL)
{
	chrome.tabs.query( queryInfo, function(tabs) {
			textURL.value = tabs[0].url;
		}
	);
}


////////////////////////
// Listeners (Logic) //
//////////////////////

// Page loaded listener
document.addEventListener('DOMContentLoaded', function(dcle) {

		textURL = document.getElementById(textURLID);

		printURL(textURL);
	}
);