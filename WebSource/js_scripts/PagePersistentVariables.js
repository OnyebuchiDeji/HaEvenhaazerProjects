/**
 *  This initializes all the global persistenet variables
 *  and defines the functions used to modify them. 
 *  
*/
const g_CurrentThemeIsDarkID = "ThemeIsDarkId";

const SavePageVariable = (id, data) =>
{
    localStorage.setItem(String(id), data);
}

const GetPageVariable = (id) =>
{
    return localStorage.getItem(String(id));
}
