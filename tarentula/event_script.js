// ////////////////
// // Variables //
// //////////////

// var ruleHosts = {
	
// 	"conditions" : [

// 		// Match Youtube
// 		new chrome.declarativeContent.PageStateMatcher({
// 			"pageUrl" : {
// 				"hostEquals" : "www.youtube.com",
// 				"schemes" : ["http", "https"]
// 			}
// 		}),

// 		// Match Dailymotion
// 		new chrome.declarativeContent.PageStateMatcher({
// 			"pageUrl" : {
// 				"hostEquals" : "www.dailymotion.com",
// 				"schemes" : ["http", "https"]
// 			}
// 		})
// 	],

// 	// Show the extension
// 	"actions" : [new chrome.declarativeContent.ShowPageAction()]
// };


// ////////////////////////
// // Listeners (Logic) //
// //////////////////////


// // Rules are added through onInstalled event
// chrome.runtime.onInstalled.addListener(function(details) {

// 	// Replace all previous rules
// 	chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {

// 		// With our new rule
// 		chrome.declarativeContent.onPageChanged.addRules([ruleHosts]);

// 	});
// });


chrome.runtime.onMessage.addListener(function (msg, sender) {
	if ((msg.from === 'content') && (msg.subject === 'showPageAction')) {
    	chrome.pageAction.show(sender.tab.id);
    }
});