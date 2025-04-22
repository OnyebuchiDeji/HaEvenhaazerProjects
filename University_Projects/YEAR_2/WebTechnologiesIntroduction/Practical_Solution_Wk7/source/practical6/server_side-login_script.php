<?php
/**
 * Comment: Sun-3-March-2024
 * Notice that the login_script was changed.
 * In version 2, writing the data to files was implmeneted according to task 1
 * In this version, reading was implemented.
 * The read data was checked against the entered data for any match.
 * When a match is found, login is successful.
 * If no match ws found login is not successful: the option to login with new details...
 * or to sign in by making a new account are implemented (these were implemented in version2).
 * 
 * In version 2, redirecting delay was implemented 
 * 
 * Note that the session keys, admin1 and admin2 are needed to uniquely identify whether they have...
 * been set.
 * But the session key "admin" identifies whether the currently logged in user is an admin
 * 
 */
    $_SESSION["storeFileName"] = "UserDataStore.csv";
    session_start();

    //  Check if session logged in is already set:
    //  If set, go straight to the message or actual service page.
    if (isset($_SESSION["loggedin"]))
        header("Location: server_side-messagingservice_script.php");
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
        $_SESSION["admin"] = TRUE;
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
        header("Location: server_side-messagingservice_script.php");
    }
    elseif ($username== "evenhaazer" && $password== "secret2")
    {
        $_SESSION["admin"] = TRUE;
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
        header("Location: server_side-messagingservice_script.php");
    }
    else
    {
        $_SESSION["admin"] = FALSE;
        $users = array();
        //  First read from databse for non-admin user details -- the admin user details are done above.
        if (($readFileHandle = fopen($_SESSION["storeFileName"], "r")) !== FALSE)
        {
            while (($lineData = fgetcsv($readFileHandle, 1000, ",")) !== FALSE)
            {
                //  Make an associative array that uses the username to be the key to identify...
                //  its corresponding data, its password and admin bool data.
                $users[$lineData[0]] = array("password"=>$lineData[1], "admin"=>$lineData[2]);
            }
            fclose($readFileHandle);
        }
        //  Now use the gotten posted data and compare with every read userdata from database for whether it is the same.
        if (isset($users[$username]) and $users[$username]['password'] == $password)
        {
            $_SESSION["loggedin"] = TRUE;
            $_SESSION["username"] = $username;
            header("Location: server_side-messagingservice_script.php");
        }
        else
        {
            //  Else if the entered details don't match any, give permission to...
            //  login with other account or make a new account
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

    }
?>