<?php
    session_start();
    //  If already logged previously in, go immediately to the messageing page
    if (isset($_SESSION["loggedin"]))
        header("Location: server_side-messagingservice_script.php");
    
?>

<!DOCTYPE HTML><html>
    <head>
        <title>Log-in Page</title>
    </head>

    <body>
        Welcome to Deji's Private Messaging Web App Service.<br>
        <form action="server_side-login_script.php" method="POST">
            Login Name:<br>
            <input type="text" name="username"><br>
            Password:<br>
            <input type="text" name="password"><br>
            <input type="submit">
        </form>
    </body>
</html>