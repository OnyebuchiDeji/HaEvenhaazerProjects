<!DOCTYPE html>
<?php
	include("connection.php");
	
	$username = $_POST['username'];
	$studentid = $_POST['studentid'];
	$password = $_POST['password'];
	$profile_remark = $_POST['profileremark'];

	$query = "INSERT INTO LibDB(studentid, username,password,profileremark) VALUES(?, ?, ?, ?)";
	//	htmlspecialchars and htmlentities() are extremely similar.
	//	But htmlentities() affects more special characters.
	$username = htmlentities(strip_tags($username));
	$studentid = htmlentities(strip_tags($studentid));
	$password = htmlentities(strip_tags($password));
	$profile_remark = htmlentities(strip_tags($profile_remark));

	$hashed_password = password_hash($password, PASSWORD_DEFAULT);
	if($stmt = $conn->prepare($query)){
		$stmt->bind_param("ssss", $studentid, $username, $hashed_password, $profile_remark);
		$stmt->execute();
		$stmt->close();
	}

?>
<html lang="en">
  <head>
    <title>Database Connection Example - Simple Address Book - PHP Output (UPDATE)</title>
  </head>
  <body>
    <h2>Registered user <em><?= $username; ?><em></h2>

    <p><a href="../client_side/login.php">Return to login page</a></p>

  </body>
</html>
