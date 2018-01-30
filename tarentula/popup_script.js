// Variables
var queryInfo = {"active" : true};
var textURLID = "url";


// print Tab Url
function printURL(textURL)
{
	chrome.tabs.query( queryInfo, function(tabs) {
			textURL.value = tabs[0].url;
		}
	);
}

// Listener
document.addEventListener('DOMContentLoaded', function(dcle) {

		textURL = document.getElementById(textURLID);

		printURL(textURL);
	}
);