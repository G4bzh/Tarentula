////////////////
// Variables //
//////////////

var queryInfo = {"active" : true};
var textURLID = "url";
var textTitleID = "title";
var textSelectionID = "selection";


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

function printInfo(info)
{
	document.getElementById(textTitleID).value = info.title;
	document.getElementById(textSelectionID).value = info.selection;
	document.getElementById(textURLID).value = info.title;
}




////////////////////////
// Listeners (Logic) //
//////////////////////

// Page loaded listener
document.addEventListener('DOMContentLoaded', function(dcle) {

	chrome.tabs.query( queryInfo, function(tabs) {
		document.getElementById(textURLID).value = tabs[0].url;
		chrome.tabs.sendMessage(
        tabs[0].id,
        {from: 'popup', subject: 'DOMInfo'},
        printInfo);
	
	});
});


