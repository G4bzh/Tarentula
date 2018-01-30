////////////////
// Variables //
//////////////

var queryInfo = {"active" : true};
var textURLID = "url";
var textTitleID = "title";
var textBodyID = "body";


////////////////
// Functions //
//////////////


function printInfo(info)
{
	document.getElementById(textURLID).value = info.url;
	document.getElementById(textTitleID).value = info.title;
	document.getElementById(textBodyID).value = info.body;
}




////////////////////////
// Listeners (Logic) //
//////////////////////

// Page loaded listener
document.addEventListener('DOMContentLoaded', function(dcle) {

	// Request info from content script
	chrome.tabs.query( queryInfo, function(tabs) {
		
		chrome.tabs.sendMessage(
        	tabs[0].id,
        	{from: 'popup', subject: 'DOMInfo'},
        	printInfo);
	
	
	});

});


