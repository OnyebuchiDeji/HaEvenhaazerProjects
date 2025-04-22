#	Date: Saturday 19th April, 2025


#	Brief

The first example shows several different versions of two php scripts: `get_modules-server_side.php` and `get_modules-client_side.php`.

THe general working is that the server side scripts parse the information in the json files when the client side
scripts send get requests to the corresponding server side script.
After getting the response from their contacted server side script, the client side one will perform operations like looping through 
the information and displaying it on the DOM.


The second example consists of two files.
The first file, `list_doi-client_side.php` sends a get request to the second file
`using_doi_service.php`. This second file sends as a response the data from the doi page it requests from.
This first file then processes the string to noly display the text. The algorithm for processing the string
was custom by me. I also had to explore other syntax semantics like switch-case in PHP to ensure cleanness and speed.
