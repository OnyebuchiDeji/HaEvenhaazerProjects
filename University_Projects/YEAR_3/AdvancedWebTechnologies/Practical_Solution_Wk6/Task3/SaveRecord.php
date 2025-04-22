<?php
    $conn = mysqli_connect("katara.scam.keele.ac.uk", "x7e30", "x7e30x7e30", "x7e30");
    //  Check Connection
    if ($conn === false){
        die("ERROR: could not connect. " . mysqli_connect_error());
    }
    $tableName = 'ReactUsers';

    $username = $_GET['username'];
    $phone = $_GET['phone'];
    $email = $_GET['email'];
    $comment = $_GET['message'];

    //  Sanitize Input
    $username=htmlspecialchars(strip_tags($username));
    $phone=htmlspecialchars(strip_tags($phone));
    $email=htmlspecialchars(strip_tags($email));
    $comment=htmlspecialchars(strip_tags($comment));

    $query = "INSERT INTO " . $tableName . " SET
    username='". $username . "', phone='" . $phone .
    "', email='" . $email . "', comment='".$comment. "'";

    //  Execute Query
    if (mysqli_query($conn, $query)){
        echo json_encode(array('MSG'=> "Success"));
    }else{
        echo json_encode(array('MSG'=> "Failed"));
    }
?>