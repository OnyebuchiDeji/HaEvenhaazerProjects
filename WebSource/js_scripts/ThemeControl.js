let thc_Path = "./page_html/";


// let themeButtonHandle = document.getElementById("ThemeButton");
// let IconsTemplateElement = document.getElementById("TopNavbarIconsTemplate").content;
    /**
        * The reason for the prefix is to differentiate this similar named
        * global variable, 'htmlContentCopy' from those in other scripts
        * In this case for the theme, because ProjectsSideNavbarContent
        * had a similar global variable, there were issues.
    */
// let tc_HtmlContentCopy = document.importNode(IconsTemplateElement, true);


function SwitchToDarkTheme(themeButtonHandleRef, htmlContentCopyRef)
{
    document.body.classList.replace("LightBG", "DarkBG");

    //  Change Icon
    var iconElement = htmlContentCopyRef.getElementById("ThemeIcon-Sun").outerHTML;
    
    themeButtonHandleRef.innerHTML = iconElement;
    SavePageVariable(g_CurrentThemeIsDarkID, true);
}

function SwitchToLightTheme(themeButtonHandleRef, htmlContentCopyRef)
{
    document.body.classList.replace("DarkBG","LightBG");

    //  Change Icon
    let iconElement = htmlContentCopyRef.getElementById("ThemeIcon-Moon").outerHTML;

    themeButtonHandleRef.innerHTML = iconElement;
    SavePageVariable(g_CurrentThemeIsDarkID, false);
}

//  Callback for Toggle Theme Button Hook
function ToggleThemeCallback(themeButtonHandleRef, htmlContentCopyRef)
{
    if (document.body.classList.contains("LightBG") && GetPageVariable(g_CurrentThemeIsDarkID) == "false"){
        SwitchToDarkTheme(themeButtonHandleRef, htmlContentCopyRef);
    }
    else
    {
        SwitchToLightTheme(themeButtonHandleRef, htmlContentCopyRef);
    }
}

function InitTheme(themeButtonHandleRef, htmlContentCopyRef)
{
    
    if (GetPageVariable(g_CurrentThemeIsDarkID) == "true") //  If true
    {
        SwitchToDarkTheme(themeButtonHandleRef, htmlContentCopyRef);
    }
    else if (GetPageVariable(g_CurrentThemeIsDarkID) == "false")
    {
        SwitchToLightTheme(themeButtonHandleRef, htmlContentCopyRef);
    }
    else    //  If variable not yet set.
    {    
        SwitchToLightTheme(themeButtonHandleRef, htmlContentCopyRef);
    }
}

function ThemeControlMain(themeButtonHandleRef)
{
    let rc = new RequestConnector();
    let url = thc_Path + "IconsTemplate.html";
    rc.SendRequest(url, "get", "text", {}, (htmlContent="")=>{
        let htmlContentStr = htmlContent.trim();
        var newDoc = Parser.parseFromString(htmlContentStr, "text/html");

        // document.body.appendChild(newDoc.querySelector("template"));

        let iconsTemplateElement = newDoc.getElementById("TopNavbarIconsTemplate").content;
        let htmlContentCopy = newDoc.importNode(iconsTemplateElement, true);

        InitTheme(themeButtonHandleRef, htmlContentCopy);
        
        //  Register Theme Button Callback
        themeButtonHandleRef.onclick = (event)=>{
            ToggleThemeCallback(themeButtonHandleRef, htmlContentCopy);
        }
    });
}
