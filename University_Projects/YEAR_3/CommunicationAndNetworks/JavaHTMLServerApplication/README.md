#	Date: Saturday 19th April, 2025

#	Brief

This is a small example showing implementation of a HTML server written in the 
Java programming language.

While it runs on a certain port on the system's localhost, any requests to an HTML, text,
json, image, or gif file on the server will cause the application to respond with the requested file
if it does exist; else the response gives the File Not Found error.

A request to this app can be made using your device's search engine, or any app able to make HTTP requests.

To be able to detect and respond appropriately to HTTP requests, the app builds an HTTP packet, containing the header,
the COntent-Type, other parameters, and finally the data.

The app was expanded to handle client requests in parallel by running the request h

All the logiv was done by me, the student; the lecturer only explained the concepts and added some placeholder code.