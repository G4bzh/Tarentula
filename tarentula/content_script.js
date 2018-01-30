// Copyright (c) 2009 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var additionalInfo = {
	"url" : location.href,
	"title": document.title,
	"body": document.characterSet
};


// Inform event_script we need pageaction
chrome.runtime.sendMessage({
   from:    'content',
   subject: 'showPageAction'
});


// Listen for message from popup
chrome.runtime.onMessage.addListener(function (msg, sender, response) {
 	 
 	 if ((msg.from === 'popup') && (msg.subject === 'DOMInfo')) {
	     // Directly respond to the sender (popup), 
	     // through the specified callback */
 	     response(additionalInfo);
 	}

});
