<?php
require_once('../server_side/authorise.php');

//The rest of this script will not execute if the session check in authorise.php fails and 
//the user will have been redirected to a different page
?>

<html>
 <head>
  <title>Secure page</title>
 </head>
 <body>
  <h2>Secure page after login</h2>
  
  <p>
  Welcome to the protected area, <?php echo($_SESSION['username']) ?>!
  </p>
  <h3>Your Information</h3>
  <ul>
    <li>
        StudentID: <?php echo $_SESSION['studentid'];?>
    </li>
    <li>
        Username: <?php echo $_SESSION['username'];?>
    </li>
    <li>
        Profile Remark:<br>
        <div style="margin:0% 0% 0% 5%">
            <?php echo $_SESSION['profileremark'];?>
        </div>
    </li>
  </ul>

  <a href="../server_side/logout.php">Logout</a>

 </body>
</html>
