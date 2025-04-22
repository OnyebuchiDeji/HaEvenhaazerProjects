<!DOCTYPE HTML><html>
    <head>
        <!-- 
            This version uses the GET method instead of POST...
            to send data from client to server
         -->
        <title>This is the welcome_get.php</title>
    </head>

    <body>
        The name that was submitted:
        <?php
            if (isset($_GET["name"]))
            {
                echo $_GET["name"]; 
            }
            else
            {
                echo "No name sent by GET!";
            }
        ?><br>

        The phone number submitted:
        <?php
            if (isset($_GET["phone"]))
            {
                echo $_GET["phone"];
            }
            else
            {
                echo "No phone number sent by GET!";
            }
        ?><br>
    </body>
</html>