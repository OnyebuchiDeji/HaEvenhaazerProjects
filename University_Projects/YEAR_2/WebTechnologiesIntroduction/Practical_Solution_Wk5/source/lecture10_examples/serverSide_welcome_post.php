<!DOCTYPE html><html>
    <head>
        <!--
            This is server-side processing.
            It just displays what information was entered into the form

         -->
        <title>This is the Welcome.php</title>
    </head>
    <body>
        The name that was submitted was:
        <?php 
            if (isset($_POST["name"]))
            {
                echo $_POST['name'];
            }
            else
            {
                echo "nothing was sent!";
            }
        ?><br>
        The phone number that was submitted was:
        <?php
            if (isset($_POST["phone"]))
            {
                echo $_POST['phone'];
            } 
            else
            {
                echo "nothing was sent!"; 
            }
        ?><br>
    </body>
</html>