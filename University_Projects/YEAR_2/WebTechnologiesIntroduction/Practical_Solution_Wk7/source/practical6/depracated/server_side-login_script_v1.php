<?php
    session_start();

    //  Check if session logged in is already set:
    //  If set, go straight to the message or actual service page.
    if (isset($_SESSION["loggedin"]))
        header("Location: server_side-messagingservice_script.php");
    if (!isset($_POST["username"]) || !isset($_POST["password"]))
        header("Location: client_side-login_form.php");

    $username = $_POST["username"];
    $password= $_POST["password"];


    //  If first admin
    if ($username=="deji" && $password=="secret1")
    {
        //  Set the session of key loggedin with boolean value TRUE
        $_SESSION["loggedin"] = TRUE;
        //  Set another session storing username data
        $_SESSION["username"] = "deji";
        //  Change page being displayed or script run
        header("Location: server_side-messagingservice_script.php");
    }
    elseif ($username== "evenhaazer" && $password== "secret1")
    {
        //  Set the session of key loggedin with boolean value TRUE
        $_SESSION["loggedin"] = TRUE;
        //  Set another session storing username data
        $_SESSION["username"] = "evenhaazer";
        //  Change page being displayed or script run
        header("Location: server_side-messagingservice_script.php");
    }
    else
    {
        //  O, generally, the username is not authorised to access the messagin services!
        header("Location: client_side-login_form.php");
    }
?>