/**
 *  Code gotten from AWT_Project, like that of Briygnonem, but refined
 */

const Parser = new DOMParser();
// const Util = new Utility(true);
let Path = "./page_html/";



function LoadTopNavbarContent(htmlContent="")
{
    let htmlContentStr = JSON.parse(JSON.stringify(htmlContent.trim()));
    let targetElementHandle = document.getElementById("TopNavbarHTML");
    let newDoc = Parser.parseFromString(htmlContentStr, "text/html");

    targetElementHandle.appendChild(newDoc.querySelector("div"));

    /**
     *  Initialize theme button
     */
    const ThemeButtonHandle = document.getElementById("ThemeButton");
    ThemeControlMain(ThemeButtonHandle);

    /**
     *  Initialize TopNavbarControl
     */

    const topNavbarLinkItemsHandle = document.getElementById("TopNavbarLinkItems");
    const topNavbarResizeToggleButtonHandle = document.getElementById("TopNavbarToggleButton");

    TopNavbarControlMain(topNavbarLinkItemsHandle, topNavbarResizeToggleButtonHandle);
}


function FetchTopNavbarContent()
{
    let rc = new RequestConnector();
    let url = Path + "TopNavbar.html";
    rc.SendRequest(url, "get", "text", {}, LoadTopNavbarContent);
}

function LoadSideNavbarContent(htmlContent="")
{
    let htmlContentStr = htmlContent.trim();
    let targetElementHandle = document.getElementById("SideNavbarHTML");
    let newDoc = Parser.parseFromString(htmlContentStr, "text/html");
    targetElementHandle.appendChild(newDoc.querySelector("div"));
}

function FetchSideNavbarContent()
{
    let rc = new RequestConnector();
    let url = Path + "SideNavbar.html";
    rc.SendRequest(url, "get", "text", {}, LoadSideNavbarContent);
}

function LoadBottomNavbarContent(htmlContent="")
{
    let htmlContentStr = htmlContent.trim();
    let targetElementHandle = document.getElementById("BottomNavbarHTML");
    let newDoc = Parser.parseFromString(htmlContentStr, "text/html");
    targetElementHandle.appendChild(newDoc.querySelector("div"));
}

function FetchBottomNavbarContent()
{
    let rc = new RequestConnector();
    let url = Path + "BottomNavbar.html";
    rc.SendRequest(url, "get", "text", {}, LoadBottomNavbarContent);
}

function InitPageNavbars()
{
    let existingElements = {
        'TopNavbar': document.getElementById("TopNavbarHTML") != undefined ? true : false,
        'SideNavbar': document.getElementById("SideNavbarHTML") != undefined ? true : false,
        'BottomNavbar': document.getElementById("BottomNavbarHTML") != undefined ? true : false,
    };

    if (existingElements.TopNavbar)
    {
        FetchTopNavbarContent();
    }
    if (existingElements.SideNavbar)
    {
        FetchSideNavbarContent();
    }
    if (existingElements.BottomNavbar)
    {
        FetchBottomNavbarContent();
    }
}


function main()
{
    InitPageNavbars();
}

main();