// Copyright (c) 2009 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.


// Inform event_script we need pageaction
chrome.runtime.sendMessage({
   from:    'content',
   subject: 'ShowAction'
});


// Listen for message from popup
chrome.runtime.onMessage.addListener(function (msg, sender, response) {

 	if ((msg.from === 'popup') && (msg.subject === 'GetInfo')) {
	     // Directly respond to the sender (popup), 
	     // through the specified callback */

	    var additionalInfo = {
			"url" : document.getElementById('tabShareAndEmbed').getElementsByClassName('form-control')[0].value,
			"title": document.getElementsByTagName('h2')[2].innerText,
			"code" : 1
		};

 	    response(additionalInfo);
 	}


});



