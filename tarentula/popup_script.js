////////////////
// Variables //
//////////////

var queryInfo = {"active" : true};
var textURLID = "url";
var textTitleID = "title";
var canvThumbID = "thumb";
var buttonShotID = "shot";
var buttonSendID = "send";

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
	sendButton = document.getElementById(buttonSendID);

	// Request info from content script
	chrome.tabs.query( queryInfo, function(tabs) {
		
		chrome.tabs.sendMessage(
        	tabs[0].id,
        	{from: 'popup', subject: 'GetInfo'},
        	printInfo);
	
	
	});

	// Add a listener to the 'Shot !' button
	shotButton.addEventListener('click', function(ce) {

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


	// Add a listener to the 'Send' button
	sendButton.addEventListener('click', function(ce) {

			var data = {
				"url" : document.getElementById(textURLID).value,
				"title": document.getElementById(textTitleID).value,
				"img" : document.getElementById(canvThumbID).toDataURL()
			};
			
			// Need  <all_urls> permission here
			var x = new XMLHttpRequest();
			x.open('POST', 'http://localhost:5000/post');
			x.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
			
			x.onload = function() {
        		alert(x.responseText);
    		};

    		x.send(JSON.stringify(data));

	});

});



