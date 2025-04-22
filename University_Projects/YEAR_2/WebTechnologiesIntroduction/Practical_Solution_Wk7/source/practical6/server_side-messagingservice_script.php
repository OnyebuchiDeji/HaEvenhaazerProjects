<?php
    session_start();

    if (!isset($_SESSION["loggedin"]) && $_SESSION["loggedin"]===FALSE)
        header("Location: server_side-login-form.php");
?>

<!DOCTYPE HTML><html>
    <head>
        <title>Message Service Page (Secret Page)</title>
    </head>

    <body>
        <a href="server_side-admin_form.php">Admin Control</a><br><br>
        Welcome! To the Deji Messaging Web App Services
        <?php echo $_SESSION["username"] ?><br><br>

        <h2>Messages</h2>
        <?php
            //  Add Code for messaging
        ?>
        <form action="client_side-login_form.php" method="POST">
            <input type="Submit" name="logout" value="Log Out">
        </form>
        &copy; Private Message Limited</p>
    </body>
</html>