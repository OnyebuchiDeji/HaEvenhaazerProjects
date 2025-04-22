import * as fs from "fs";
/*
    Created: Fri-23-Feb-2024
    Things to cosider:

        1. Simply shows the use of Funciton Objects and how to accesss their members, as well as...
    creating methods in them

        2.  Converted one of the function objects into JSON string form using JSON.stringify()...
        making it ready to be written to a file. Though no file writing was done here.

        3.  Having made the JSON string of the SchoolObj object, one can immediately use the...
        JSON.parse() to convert that stringified JSON object back into the original object. 

    Added: Sun-25-Feb-2024
    Used "fs" library to write the JSONIFIED-to-string object to an actual file.
    Then read the file and use it instead of using the return of the readFromServer() funciton.
    The "fs" library is built up
*/


const fileHandler = require("fs");
const JSON_FILE_NAME = "schoolobj.json"

function SchoolObj(name, code)
{
    this.name = name;
    this.code = code;
    this.modules = new Array()
    this.addModule = function(module)
    {
        this.modules.push(module);
    }
}

function ModuleObj(id, name, year)
{
    this.id = id; this.name = name; this.year = year;
}

// Function to imitate reading from a server
function readFromServer()
{
    var scm = new SchoolObj("School of Computing and Mathematics", "SCM");
    scm.addModule(new ModuleObj("CSC-20021", "Web Technologies", 2));
    scm.addModule(new ModuleObj("CSC-20001", "Database Systems", 2));
    scm.addModule(new ModuleObj("CSC-20021", "Communications and Networks", 3));

    //  This converts the string to a JavaScript Object Notation (JSON) string format
    //  From here it can be stored in a file.
    var jsonSchool = JSON.stringify(scm);
    console.log(jsonSchool);
    return jsonSchool;
}

function writeJSON()
{
    try
    {
        //  Writing File Synchronously
        fileHandler.writeFileSync(JSON_FILE_NAME, readFromServer());
    }
    catch(error)
    {
        //  Loggin any error
        console.error(error);
        throw error;
    }

    console.log(JSON_FILE_NAME + " written to correctly");
}

function readJSON()
{
    try
    {
        //  Reading the JSON File
        const jsonData = fs.readFileSync(JSON_FILE_NAME);
        return jsonData;
    }
    catch (error)
    {
        //  Logging any error
        console.error(error);

        throw error;
    }
}

function addNewFieldToJSON()
{
    try
    {
        //  Read the contents of the JSOn file
        const currentJsonData = fs.readFileSync(JSON_FILE_NAME);

        //  Parsing the JSON content
        //  Turning from JSON form to the form of the object!
        const schoolObj = JSON.parse(currentJsonData);
        const jsonifiedSchoolObj = JSON.stringify(schoolObj);
        jsonifiedSchoolObj["newItem"] = "${schoolObj.name} ${schoolObj.code}";

        fs.writeFileSync(JSON_FILE_NAME, jsonifiedSchoolObj);
    }
    catch(error)
    {
        //  Logging the error
        console.error(error);

        throw error;
    }
}

function updateJSON(newName, newCode)
{
    try
    {
        //  Read the contents of the JSOn file
        const currentJsonData = fs.readFileSync(JSON_FILE_NAME);

        //  Parsing the JSON content
        //  Turning from JSON form to the form of the object!
        const schoolObj = JSON.parse(currentJsonData);
        schoolObj.name = newName;
        schoolObj.code = newCode;
        const jsonifiedSchoolObj = JSON.stringify(schoolObj);

        fs.writeFileSync(JSON_FILE_NAME, jsonifiedSchoolObj);
    }
    catch(error)
    {
        //  Logging the error
        console.error(error);

        throw error;
    }
}
//  Now parsing the JSON string object that has been created to store the information from scm in readFromServer()
//  It gives me back the origninal SchoolObj type with the information in it accurately.
writeJSON();
updateJSON("School of Life Sciences", "SLS")
addNewFieldToJSON();
var school = JSON.parse(readFromServer());

modulesEntity = document.getElementById("modules");

modulesEntity.innerHTML += '<h2>' + school.name + ' (' + school.code + ')' + '</h2>';

for (i = 0; i < school.modules.length; i++)
{
    module = school.modules[i];
    modulesEntity.innerHTML += '<p>' + module.id + ': ' + module.name + ', Year ' + module.year + '</p>';
}