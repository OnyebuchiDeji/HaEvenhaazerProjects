<?php
    $hostname = "katara.scam.keele.ac.uk";
    $username = "x7e30";
    $password = "x7e30x7e30";
    $dbname = "x7e30";

    try{
        $g_dbConn = new PDO("mysql:host=".$hostname.";dbname=".$dbname, $username, $password);
    }catch (PDOException $e){
        print "Error!: " . $e->getMessage() . "<br>";
        die();
    }
?>