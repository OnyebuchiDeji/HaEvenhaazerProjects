<?php
    session_start();
    if (isset($_SESSION["loggedin"]) && $_SESSION["admin"] == FALSE)
    {
        header("refresh: 5; url=server_side-login_form.php");
        echo "You're not an admin! So... going back";
    }
?>

<!DOCTYPE html><html>
    <head>
        <title>
            Admin User Control Form
        </title>
    </head>

    <body>
        <h2>Enter Details for a New User</h2>
        <form action="server_side-adduser_script.php" method="post">
            User Name:<br>
            <input type="text" name="username"><br>
            Password:<br>
            <input type="text" name="password"><br>
            Admin:<br>
            <input type="radio" name="radio-yes">
            <input type="radio" name="radio-no"><br><br>

            <input type="submit">
        </form>
    </body>
</html>