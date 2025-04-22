<?php
    /**
     *  Here redirecting delay was implemented 
     */
    session_start();
    //  Save new account by  sign-in
    if ($_SESSION["loggedin"]===FALSE && isset($_GET["username"]) && isset($_GET["password"]))
    {
        $userData = array($_GET["username"], $_GET["password"], 0);
        $fileWriteHandle = fopen($_SESSION["storeFileName"], "a");
        fputcsv($fileWriteHandle, $userData);
        fclose($fileWriteHandle);

        echo "Your new account has been created!";
        
        /*
            Comment added: Sat-2-March-2024
            Added function to delay refreshing the page using the refresh header...
            as done below.
            The Refresh Heaser Syntax:
            refresh: [TIME]; url=[URL]

        */

        
        header("refresh: 5;url=client_side-login_form.php");
        echo 'You will be redirected to the login page to log ing with new account in about 5 seconds.\n
        If not, please click <a href="client_side-login_form.php">login</a>.';
    }
?>