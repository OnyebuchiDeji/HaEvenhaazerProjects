/**
 * Implementing JQuery
 * 
 * This version shows all tasks for the Part 1 of the practical...
 * till the task 7 of this part.
 * Because at task 7 the .ready() funciton was removed...
 * I implemented and continued from this part in another version of the project file.
 * 
 */

//  Here, tasks 2 and 3 are done, which required...
//  creating this file and adding the .ready code alonf with the....
//  'document has loaded!'are tasks 2 and 3 respectively.


$(document).ready(
    function()
    {
        alert("Document has loaded!");
        Task4();
        Task6();
    }
);




//  This is task 4
//  Adding an event listener for a click to every link...
//  in the html file
function Task4()
{
    $("a").click(
        //  This event argument is provided by event funcitons...
        //  they represent a handle to the DOM element that triggered the event
        function(event)
        {
            alert("Thanks for visiting!");
        }
    );
}

/**
 * This taks involves calling the event.preventDefault()...
 * method to prevent the event's default behaviour
 */
function Task6()
{
    $("a").click(
        function(eventOwner)
        {
            alert("The following statement prevents the default behaviour.");
            eventOwner.preventDefault();
        }
    );
}