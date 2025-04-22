/**
 * Comment added: Thurs-15-Feb-2024
 * Task 1: Implement highlighting specific elements.
 * Task 2: Implement adding content in the currently highlighted element
 * In this version, some mistakes with highlighting were made.
 * I thought that highlighting indicates that the element has been selected, representing the currently selected element...
 * but it turns out that that is not the case. The highlighting is separate, and I should be able to sepcify which element...
 * to remove the highlighting from.
 * I implement this in the most up-to-date source being used currently, not this one.
 */
var inputElementList = document.getElementsByClassName("input");
var buttonsList = document.getElementsByTagName("button");    

var g_highlightCallCount = 0;
var g_selectedElementCount = 0;
var g_currentSelectedElement = null;
var g_previousElementTag = "";
var g_lightColorList = [ "lightred", "lightblue", "lemon", "lightgreen", "yellow", "gold", "cyan", "skyblue", "peach"];
var g_darkColorList = ["red", "darkred", "darkblue", "blue","green","darkgreen", "black", "purple", "indigo", "violet", "gray", "darkgray", "rebeccapurple"];

function random(min, max)
{
    var number = min + Math.floor(Math.random() * (max+1 - min));
    return number;
}

// To attach each btton to their corresponding event
function attachButtonToEvent()
{
    for (var i = 0; i < buttonsList.length; i++)
    {
        switch (buttonsList[i].id)
        {
            case "highlight-button":
                buttonsList[i].onclick = function()
                {
                    console.log("Highlight Button!");
                    highlight_v2();
                };
                break;
            case "add_content-button":
                buttonsList[i].onclick = function()
                {
                    console.log("Add Content Button");
                    addContent()
                };
                break;
            case "remove_highlighted-button":
                buttonsList[i].onclick = function()
                {
                    console.log("Remove Higlight Button");
                    deselectCurrentElement()
                };
                break;
        }
    }
}

function getInputElement(name)
{
    for (let i = 0; i < inputElementList.length; i++)
    {
        if (inputElementList[i].name == name)
        {
            return inputElementList[i]
        }
    }
}

function highlight_v1A()
{
    var elementTagInfo = getInputElement("highlight-input").value;
    var accessedElements = document.getElementsByTagName(elementTagInfo);
    
    for (let i=0; i <accessedElements.length; i++)
    {
        g_highlightCallCount += 1;
        //  Change to highlightCallCount % 2 == 1 to affect just odd numbers
        if (g_highlightCallCount % 2 == 0)
        {
            accessedElements[i].style.background = g_darkColorList[random(0, g_darkColorList.length)];
            accessedElements[i].style.color = g_lightColorList[random(0, g_lightColorList.length)];
        }
    }
    
}
function highlight_v1B()
{
    var elementTagInfo = getInputElement("highlight-input").value;
    var accessedElements = document.getElementsByTagName(elementTagInfo);
    
    for (let i=0; i <accessedElements.length; i++)
    {
        g_highlightCallCount += 1;
        if (g_highlightCallCount % 2 == 0)
        {
            accessedElements[i].style.background = g_darkColorList[random(0, g_darkColorList.length)];
            accessedElements[i].style.color = g_lightColorList[random(0, g_lightColorList.length)];
        }
        else
        {
            accessedElements[i].style.background = g_darkColorList[random(0, g_darkColorList.length)];
            accessedElements[i].style.color = g_lightColorList[random(0, g_lightColorList.length)];
        }
    }
    
}


function deselectPreviousElement(elementTagInfo)
{
    /*
        This unhighlights the previous element to show tha tit is no more selected
    */
    if (g_selectedElementCount >= 1)
    {
        var accessedElements = document.getElementsByTagName(elementTagInfo);
        accessedElements[g_selectedElementCount - 1].style.background = "";
        accessedElements[g_selectedElementCount - 1].style.color = "";
    }
}

function highlight_v2()
{
    /*
        Basically this version does something coolade.
        selectedElementCount keeps track of which element to be selected next.
        So, for example, where there are more than one elements, like the paragraphs with tag <p>...
        The first time I click highlight, it should select just the first paragraph. The second time should select the second...
        and so on as such.

    */
    deselectPreviousElement(g_previousElementTag);


    var elementTagInfo = getInputElement("highlight-input").value;
    var accessedElements = document.getElementsByTagName(elementTagInfo);


    if (g_selectedElementCount >= accessedElements.length)
    {
        g_selectedElementCount = 0;
    }
    
    g_currentSelectedElement = accessedElements[g_selectedElementCount];

    g_highlightCallCount += 1;
    if (g_highlightCallCount % 2 == 0)
    {
        g_currentSelectedElement.style.background = g_darkColorList[random(0, g_darkColorList.length)];
        g_currentSelectedElement.style.color = g_lightColorList[random(0, g_lightColorList.length)];
    }
    else
    {
        g_currentSelectedElement.style.background = g_darkColorList[random(0, g_darkColorList.length)];
        g_currentSelectedElement.style.color = g_lightColorList[random(0, g_lightColorList.length)];
    }

    g_selectedElementCount += 1
    g_previousElementTag = elementTagInfo;
}

function addContent()
{
    /**
     * Adds whatever is typed into its aassociated field into the currently selected html element.
     * 
    */

    var content = getInputElement("add_content-input").value;
    var savedPrevContent = g_currentSelectedElement.innerHTML;
    g_currentSelectedElement.innerHTML = String(content) + "\n" + savedPrevContent;

}

//  This is the name for the Remove Highlighted Button
function deselectCurrentElement()
{
    // var accessedElements = document.getElementsByTagName(elementTagInfo);
    g_currentSelectedElement.style.background = "";
    g_currentSelectedElement.style.color = "";
    g_currentSelectedElement = null;
}


attachButtonToEvent()