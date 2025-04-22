<?php
    $_SESSION["storeFileName"] = "UserDataStore.csv";
    session_start();

    //  Check if session logged in is already set:
    //  If set, go straight to the message or actual service page.
    if (isset($_SESSION["loggedin"]))
        header("Location: messaging_service_script.php");
    if (!isset($_POST["username"]) || !isset($_POST["password"]))
        header("Location: client_side-login_form.php");

    $username = $_POST["username"];
    $password= $_POST["password"];

    // //  Writing to CSV file stored locally
    $fileWriteHandle = fopen($_SESSION["storeFileName"],"a");

    //  Set First Admin

    //  If first admin
    if ($username=="deji" && $password=="secret1")
    {
        //  Set the session of key loggedin with boolean value TRUE
        $_SESSION["loggedin"] = TRUE;
        //  Set another session storing username data
        $_SESSION["username"] = "deji";
        if (!isset($_SESSION["admin1"]))
        {
            $tempArray = array("deji", "secret1", 1);
            fputcsv($fileWriteHandle, $tempArray);
            $_SESSION["admin1"] = TRUE;
        }
        //  Change page being displayed or script run
        header("Location: messaging_service_script.php");
    }
    elseif ($username== "evenhaazer" && $password== "secret2")
    {
        //  Set the session of key loggedin with boolean value TRUE
        $_SESSION["loggedin"] = TRUE;
        //  Set another session storing username data
        $_SESSION["username"] = "evenhaazer";
        if (!isset($_SESSION["admin2"]))
        {
            $tempArray = array("evenhaazer", "secret2", 1);
            fputcsv($fileWriteHandle, $tempArray);
            $_SESSION["admin2"] = TRUE;
        }
        //  Change page being displayed or script run
        header("Location: messaging_service_script.php");
    }
    else
    {
        $_SESSION["loggedin"] = FALSE;
        //  Make a link and go to the signing page
        echo "Account not found.\n
         You want to make a new account with these details? Click sign in!\n";
        echo '<a href="server_side-signin_script.php?username=$username&password=$password$admin=0">' . "Sign In". "</a>";
        echo "Or log in with another account!";
        //  O, generally, the username is not authorised to access the messagin services!
        echo "Log in with another account? \n";
        echo 'Go to <a href="client_side-login_form.php">Login Page</a>'. "\n";
        // header("Location: client_side-login_form.php");
    }
?>