//  This uses Ajax and JS only!

/**
 * Note that unlike example 2 this does not use a form.
 * The getquote uses an enum that maps to a unique quote.
 * The highest enum value should be 151 as indicated by example 2.
 * So the random generated value will have to be appended to the link passed to the...
 * makeRequest method
 */
function makeRequest(url)
{
    http_request = new XMLHttpRequest();
    http_request.onreadystatechange = function()
    {
        progress(http_request);
    }
    //  It's asynchronous because of the 'true'!
    http_request.open("GET", url, true);
    http_request.send(null);
    return http_request;
}

function progress(http_request)
{
    //  If request sent successfully and response is available
    if (http_request.readyState==4)
    {
        //  If request was successful because there was a response
        if (http_request.status == 200)
        {
            var quoteElement = document.getElementById("myquote");
            quoteElement.innerHTML = http_request.responseText;
        }
        else
        {
            alert("There was a problem with the request!");
        }
    }
}

function getRandomNumberString()
{
    var randVal = Math.floor(Math.random() * 151);
    return String(randVal);
}

var btnHandle = document.getElementById("clickme");

btnHandle.onclick = function()
{
    makeRequest("https://www.teach.scam.keele.ac.uk/extra_scripts/getquote.php?quotenum=" + getRandomNumberString());
}