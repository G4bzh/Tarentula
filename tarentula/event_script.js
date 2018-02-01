/////////////
// Broker //
///////////


chrome.runtime.onMessage.addListener(function (msg, sender) {
 	
 	if ((msg.from === 'content') && (msg.subject === 'ShowAction')) 
 	{
     	chrome.pageAction.show(sender.tab.id);
    }

});
