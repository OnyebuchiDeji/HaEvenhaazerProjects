<?php

  // IMPORTANT: Change the connection parameters to reflect our MySQL setup...
  //            Server name: dalek.scam.keele.ac.uk
  //            Username: your username (eg. v0x00)
  //            Password: same as your username (NOT your usual login password)

  $servername = "katara.scam.keele.ac.uk";
  $username = "x7e30";
  $password = "x7e30x7e30";
  $dbname = "x7e30";

  // Create connection
  $conn = mysqli_connect($servername, $username, $password, $dbname);

  // Check connection
  if (!$conn) {
  	die("Connection failed: " . mysqli_connect_error());
  }
?>
