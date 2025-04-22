<?php
    session_start();

    //  Cehcks again if the current user is admin
    //  If not, redirect
    if (isset($_SESSION["loggedin"]) && $_SESSION["admin"] == FALSE)
    {
        header("refresh: 5; url=server_side-messagingservice_script.php");
        echo "You're not an admin! So... going back";
    }
    else
    {
        $userName = $_POST["username"];
        $userPassword = $_POST["password"];
        $userIsAdmin = 0;
        if ($_POST["radio-yes"])
        {
            $userIsAdmin = 1;
        }
        else if ($_POST["radio-no"])
        {
            $userIsAdmin = 0;
        }
        $userData = array($userName, $userPassword, $userIsAdmin);

        $fileWriteHandle = fopen($_SESSION["storeFileName"], "a");
        fputcsv($fileWriteHandle, $userData);
        fclose($fileWriteHandle);
    }

?>