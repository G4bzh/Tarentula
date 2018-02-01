////////////////
// Variables //
//////////////

var queryInfo = {"active" : true};
var textURLID = "url";
var textTitleID = "title";
var canvThumbID = "thumb";
var buttonShotID = "shot";


////////////////
// Functions //
//////////////


function printInfo(info)
{
	document.getElementById(textURLID).value = info.url;
	document.getElementById(textTitleID).value = info.title;
   
}




////////////////////////
// Listeners (Logic) //
//////////////////////

// Page loaded listener
document.addEventListener('DOMContentLoaded', function(dcle) {


	shotButton = document.getElementById(buttonShotID);

	// Request info from content script
	chrome.tabs.query( queryInfo, function(tabs) {
		
		chrome.tabs.sendMessage(
        	tabs[0].id,
        	{from: 'popup', subject: 'GetInfo'},
        	printInfo);
	
	
	});

	// Add a listener to the button
	shotButton.addEventListener('click', function(ce){

		// Need  <all_urls> permission here
		chrome.tabs.captureVisibleTab(null, {}, function (dataURL) {
    		
    		var img = new Image();
	
			img.onload = function() {

				var canv=document.getElementById(canvThumbID);
    			var ctx=canv.getContext('2d');
				ctx.drawImage(img,400,100,750,450,0,0,750,450);
			};

			img.src = dataURL;
	
    	});

	});

});



