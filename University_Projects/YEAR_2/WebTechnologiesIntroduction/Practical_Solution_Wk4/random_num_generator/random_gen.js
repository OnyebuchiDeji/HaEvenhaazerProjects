
/*
    Code to generate a random number between 0 and 9, when the page is loaded.
    The result willbe displayed in the "result" label entity.    
*/

document.getElementById("result").innerHTML = random(1, 10);

/*
    Write JS code to display a random number when the user clicks on the submit button.
    The minimum and maximum numbers will be taken from the min and max input entities.
*/

function random(min, max)
{
    var number=min + Math.floor (Math.random() * (max+1-min));
    return number;
}

function showRandom()
{
    // parseInt converts String to Int
    var min=parseInt(document.getElementById("min").value);
    var max=parseInt(document.getElementById("max").value);
    document.getElementById("result").innerHTML=random(min, max);
}