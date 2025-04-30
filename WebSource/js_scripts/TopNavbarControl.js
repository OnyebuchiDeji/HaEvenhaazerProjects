/**
 *  Date: Monday 19th April, 2025
 * 
 *  Gotten from `TopNavbarResizeSemantics-CSS`
 *  This controls resizing responsiveness.
 */

let tnc_Path = "./WebSource/page_html/";


// const topNavbarResizeToggleButtonHandle = document.getElementById("TopNavbarToggleButton");
// const topNavbarLinkItemsHandle = document.getElementById("TopNavbarLinkItems");


function ToggleTopNavbarLinkItemsResize(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef)
{
    if (topNavbarLinkItemsHandleRef.classList.contains("Resized")){
        topNavbarLinkItemsHandleRef.classList.toggle("Resized");
        topNavbarResizeToggleButtonHandleRef.classList.toggle("Closed");
    }
}

function RegisterBodyResizeEvent(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef)
{
    // console.log(topNavbarLinkItemsHandleRef);
    // console.log(topNavbarResizeToggleButtonHandleRef);
    window.addEventListener("resize", ()=>{
        let windowWidth = document.body.offsetWidth;

        if (windowWidth > 768)
        {
            ToggleTopNavbarLinkItemsResize(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef);
        }
    });
}

function RegisterButtonHandleEvent(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef)
{
    topNavbarResizeToggleButtonHandleRef.addEventListener("click",()=>{
        topNavbarLinkItemsHandleRef.classList.toggle("Resized");
        topNavbarResizeToggleButtonHandleRef.classList.toggle("Closed");
    });
}

function ChangeTopNavbarToggleButtonIcon(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef)
{
    let rc = new RequestConnector();
    let url = tnc_Path + "IconsTemplate.html";
    
    rc.SendRequest(url, "get", "text", {}, (htmlContent="")=>{

        let htmlContentStr = htmlContent.trim();
        var newDoc = Parser.parseFromString(htmlContentStr, "text/html");

        var iconsTemplateElement = newDoc.getElementById("TopNavbarIconsTemplate").content;
        var htmlContentCopy = newDoc.importNode(iconsTemplateElement, true);
    
        isClosed = topNavbarResizeToggleButtonHandleRef.classList.contains("Closed") ? true : false;
        
        //  If isOpen, select the Close Icon, If !isOpen, select the Open Icon
        var iconElement = isClosed ? htmlContentCopy.getElementById("TopNavbarIcon-Close").outerHTML :
            htmlContentCopy.getElementById("TopNavbarIcon-Open").outerHTML;
    
        topNavbarResizeToggleButtonHandleRef.innerHTML = iconElement;
    });
}

function TopNavbarControlMain(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef)
{
    RegisterBodyResizeEvent(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef);
    RegisterButtonHandleEvent(topNavbarLinkItemsHandleRef, topNavbarResizeToggleButtonHandleRef);
}
