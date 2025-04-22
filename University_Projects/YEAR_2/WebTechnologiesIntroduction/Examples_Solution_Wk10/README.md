#	Date: Saturday 19th April, 2025


#	Brief

This examples solution explored client-side storage of data. Little but important data like
what theme the client selected, what page the client is currently in for Single-Page web applications,
etc. can be stored on the cliend side storage using localStorage and or sessionStorage APIs provided by the web engine
in JavaScript.
They are also used for caching a web page's information in case the client goes offline.

localStorage differs from sessionStorage in that the latter goes only exists for a limited time and is lost when that
browser window is closed. Whereas the former persisits in system memory for that page indefinitely, until deleted in page caches.

Client-side stored data are not sent to the server the web engine contacts;
they differ from cookies in this fact, despite cookies also being stored locally.


Lastly, it is seen that the data they store, whether bool or number, are stored in memory as strings.
Hence, when serializing objects in JavaScript, JSON.stringify is used, and when reading them, JSON.parse is used.