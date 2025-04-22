/**
 * Implementing JQuery
 * 
 * This continues from task 7 of Part 1 of the practical7
 * 
 */


/**
 * Here, tasks 2 and 3 are done, which required...
 * creating this file and adding the .ready code alonf with the....
 * 'document has loaded!'are tasks 2 and 3 respectively.
 * 
 * Task 7:
 * It involves not using the .ready() function, but a short-hand...
 * form of it:
 * $
 * (
 *      //  my code
 * );
 * 
*/
$(
    function()
    {
        alert("Document has loaded!");
        Task4();
        Task6();
        Task8();
        Task9();
        Task10();
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

//  This task shows the two ways in which jQuery can be used...
//  to select elementd from the DOM:
//  first using a combination of CSS and XPath selectors passed as strings...
//  to the jQuery constructor: $("div a").
//  And the second using methods of the jQuery object.
function Task8()
{
    $("#caveat").css("background", "red");
}

//  This is task 9
//  Basically accessing another element in DOM via id
function Task9()
{
    //  The '>' sign indicates selecting all children of the element with id 'ulist'
    $("#ulist > li").css("background", "blue");
}

//  This task's goal is to add classes to DOM elements that did not...
//  previously have those classes.
//  The addition of the class is triggered by mouseover event...
//  then the class is removed bt mouseouts event 
function Task10()
{
    /**
     * Basically .hover is equivalent to .mouseover() of normal JS
     * For every onxxx event in normal JS there is a jQuery equivalent.
     * The .hover takes to arguments:
     * the first is the function it runs when the mouse hovers over the element.
     * the second is the function to run when mouse leaves the elements area
    */
    $("#ulist li:last").hover
    (
        function()
        {
            $(this).addClass("green");
        },
        function()
        {
            $(this).removeClass("green");
        }
    );
}

/**
 * This shows the implementation of chaining by jQuery -- possible because the retuned...
 * jQuery object of each function starting from the first can allow further functions to be...
 * called on it.
 * 
 * Here .find() is used which allows one search the descendants of an already selected elements
 * $("#ulist").find("li") is same as $("#ulis li")
 * 
 * .each() iterates over every element and allows a function to be applied to each element selected.
 * .append() is used to append some text to the contents of each element.
 */
function Task11()
{
    $("#ulist").find("li").each(
        //  I is the individual child element within the element with id 'ulist'
        function(i)
        {
            //  This is a variable that refers to the currently selected element's css selector symbol
            $(this).append(" is a fruit." + i);
        }
    );
}


/**
 * To select certain elements within a larger group of elements...
 * apart from ready selectors that select elements by position, presence, the value of attributes, etc.
 * jQuert provides the filter() and not() funcitons for further selection criteria.
 * filter() reduces a selection to elements matching the filter argument...
 * and not() does the opposite.
 */
//  In this task, all li elements that have no ul children are selected from a ul element
function Task12()
{
    //  Every li element with no ul children are given a border
    $(li).not(":has(ul)").css("border", "1px solid black");
}

/**
 * This task shows the implementation of the [expression] syntax from XPath
 * It can be used to filter by attributes. For example, to select all input elements with a name attribute:
 */
function Task13()
{
    $("input[name]").css("background", "#cccccc");
}

/**
 * The code aims to find every definition description element to hide them.
 * This code, $("#dict").find("dd").hide() selects the element with id 'dict'...
 * and finds its children that are definition descriptions 'dd' and hides them
 * 
 * The .end() jQuery function reverts to the previously matched set.
 * 
 * The first .find () is thus undone and the distionary itself is now being searched through again.
 * So the second .fund() is called to select all child dt elements and attach a click handler.
 * 
 * In the click handlet $(this).next finds te next sibling from the current dt. The next sibling is the corresponding...
 * dd from that dt. It then calls .slideToggle() on that dd element
 * 
 * The actual program for this is written separately
 */
function Task14()
{
    $("#dict").find("dd").hide().end().find("dt").click
    (
        function()
        {
            $(this).next().slideToggle();
        }
    );
}