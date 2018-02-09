////////////////
// Variables //
//////////////

var queryInfo = {"active" : true};
var textURLID = "url";
var textTitleID = "title";
var canvThumbID = "thumb";
var buttonShotID = "shot";
var buttonSendID = "send";

		
var img = new Image();
var X = 0;
var Y = 0;
var dX = 0;
var dY = 0;
var drag = false;

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
	canv = document.getElementById(canvThumbID);
	ctx=canv.getContext('2d');


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
    
			img.onload = function() {
				ctx.drawImage(img,X,Y);
			};

			dX = canv.width;
			dY = canv.height;
			img.src = dataURL;
	
    	});

	});


	canv.addEventListener("mousedown", function(e){
		drag=true;
		dX =e.x;
		dY=e.y;
	});

	canv.addEventListener("mouseup",  function(){
		drag=false;
	});

	canv.addEventListener("mousemove", function(e) {

		if (drag)
		{
			X -= dX - e.x;
			Y -= dY - e.y;
			dX = e.x;
			dY = e.y;
			
			ctx.drawImage(img,X,Y);
		}

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



