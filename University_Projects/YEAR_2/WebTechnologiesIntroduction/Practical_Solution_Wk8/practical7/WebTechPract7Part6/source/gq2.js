// NOTE that neither jQuery nor Ajax were used!
/**
 * Pre how this works!
 * It uses a form!
 * The method is get, so it appends the data to the link!
 * The form's id is quotenum
 * The value of the form is the bascically the data that is to be appended to the link...
 * that is specified as action: https://www.teach.scam.keele.ac.uk/extra_scripts/getquote.php
 * 
 * I was having a little problem with it working because I did not turn the random value...
 * generated into a string.
 * 
 * Now it works!
 * A similar thing is employed in example 3 that uses Ajax
 */
function getRandomQuote()
{
    quoteElement = document.getElementById("quotenum");
    var randVal = Math.floor(Math.random() * 151);
    quoteElement.value = String(randVal);

    // location.assign("https://www.teach.scam.keele.ac.uk/extra_scripts/getquote.php?quotenum="+String(ransVal));
}

formHandle = document.getElementById("f1");
formHandle.addEventListener("submit", getRandomQuote);