/*
    Calculator Task Done on Sat-9th-December-2023
*/

var operatorHandle = document.getElementById("operator");
var resultHandle = document.getElementById("result");
var buttonsHandle = document.getElementsByTagName("button");

var equalsHandle = document.getElementById("equals_sign");
equalsHandle.onclick = solve;   //  This works
// equalsHandle.onclick = function(){solve()};

function setButtonsOnclickM1()
{
    for (i=0; i < buttonsHandle.length; i++)
    {
        /*
            I had to make an anonymous function to call the original function...
            to be able to pass in the calling element's id as a parameter.
        */
        buttonsHandle[i].onclick = function()
        {
            changeOperatorA(this.id);
        };
    }
}

function setButtonsOnclickM2()
{
    for (i=0; i < buttonsHandle.length; i++)
    {
        /*
            This uses a different way and passes the whole element into the function...
            changeOperatorB that has been linked. Apart from this, every other function remains the same.
            Though it is similar to the prior given that it uses an anonymous function so that it can be passed...
            into the main function.
        */
        buttonsHandle[i].onclick = function()
            {
                changeOperatorB(this)
            };
    }
}

setButtonsOnclickM2();


function changeOperatorA(buttonid)
{

    switch (buttonid)
    {
        case "plus":
            operatorHandle.value = "+";
            operatorHandle.innerHTML = "+"; break;
        case "minus":
            operatorHandle.value = '-';
            operatorHandle.innerHTML = "-"; break;
        case "multiply":
            operatorHandle.value = "&times";
            operatorHandle.innerHTML = "&times";break
        case "divide":
            operatorHandle.value = "&divide";
            operatorHandle.innerHTML = "&divide"; break;
    }

}
function changeOperatorB(element)
{
    var callerElementId = element.id;
    switch (callerElementId)
    {
        case "plus":
            operatorHandle.value = "+";
            operatorHandle.innerHTML = "+"; break;
        case "minus":
            operatorHandle.value = '-';
            operatorHandle.innerHTML = "-"; break;
        case "multiply":
            operatorHandle.value = "&times";
            operatorHandle.innerHTML = "&times";break
        case "divide":
            operatorHandle.value = "&divide";
            operatorHandle.innerHTML = "&divide"; break;
    }

}

// ÷×

function solve()
{

    var value1 = parseFloat(document.getElementById("val1").value);
    var value2 = parseFloat(document.getElementById("val2").value);
    
    var sign = operatorHandle.value;
    

    switch(sign)
    {
        case "+":
            result = value1 + value2;
            resultHandle.innerHTML = String(result);
            break;
        case "-":
            result = value1 - value2;
            resultHandle.innerText = String(result);
            break;
        case "&times":
            result = value1 * value2;
            resultHandle.innerText = String(result);
            break;
        case "&divide":
            result = value1 / value2;
            resultHandle.innerText = String(result);
            break;
    }
}