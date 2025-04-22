<?php

    $serverName = "katara.scam.keele.ac.uk";
    $userName = "x7e30";
    $password = "x7e30x7e30";
    $dbName = "x7e30";

    //  Create a Connection
    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    //  Check Connection
    if (!$conn){
        die("Connection Failed: " . mysqli_connect_error());
    }

    echo "<h4>Successfully Connected to Database <b>$dbName</b>, <b>{Server Name: $serverName | User Name: $userName}</b></h4><br>";

?>