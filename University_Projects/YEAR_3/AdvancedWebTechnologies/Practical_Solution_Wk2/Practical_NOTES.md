#   Date: Tuesday 11th February 2025


##  Things Learnt

### Tuesday 11th February 2025
+   Those `.sql` files with the names of the tables, like the 'StudentsCSC30025_V1.sql' here are imported into phpAdmin and ran.

+   Consider the `MultiMediaSQL` Folder PHP Scripts.
    -   When a file with the same input fileName is entered
    the script appends the date and time to make sure
    there are no duplicates stored in the database.

    -   Note how in `ViewFilesScript.php`, the way the image files' ids, names, and paths are gotten is an alternative way
    to how it's done in the `DBControl` practice scripts.

+   Variables:
    +   Local Variables: those defined in a function and method, existing only within that function's scope.

    +   Global Variables: When not stored in the superglobal `$_SESSION` or in cookies, these are variables declared outside functions or methods. But they are not explicitely stored in the session and hence will not persist across requests.

    +   $_POST, $_GET, and $_REQUEST:   These are **superglobals**. They store form data and URL parameters respectively. They persist only during the current request; they are not carried ober to subsequent requests unless they are manually stored in a cookie or session.

    +   Temporary Variables in a Loop or Process: these are variables used in loops or as part of a single request's processing cycle.  They have neither a session or global scope so they're cleared once the scrip finishes execution.

    +   Session-Scoped Variables: These only last for a session and **are not stored in $_SESSION**. They require a session, database or cookies for them to persist between sessions.

    +   $_SESSION:
        -   Superglobal associative array.
        -   It stores varaibes that persist across multiple page requests within a session -- as long as the session remains active.
        -   This means the variables they store are session-scoped --- they exist during the lifetime of the session, but are not stored permanently. When the user closes the browser or the session timesout, the session expires and the data is discarded.
        -  Session data is stored on the server device, unlike cookies which are stored on the user's browser. 
        -   The Session Identifier is the only session data stored in the user's browser as a cookie, `PHPSESSID`.

+   