<!DOCTYPE html>
<?php
	include("connection.php");
	
	$username = $_POST['username'];
	$studentid = $_POST['studentid'];
	$password = $_POST['password'];
	$profile_remark = $_POST['profileremark'];
	$captcha_input = trim($_POST['captcha_input']);
	$captcha_filename = $_POST['captcha_filename'];

	$query2 = "SELECT captcha_image_characters FROM FormCaptchaDB_P8 WHERE captcha_image_filename = ? LIMIT 1";

	$captcha_input = htmlentities(strip_tags($captcha_input));
	$captcha_filename = htmlentities(strip_tags($captcha_filename));

	#First test captcha
	$capture_success = true;
	if ($stmt = $conn->prepare($query2))
	{
		$stmt->bind_param("s", $captcha_filename);
		$stmt->execute();
		$stmt->bind_result($captcha_characters);
		$stmt->fetch();

		if (strcmp($captcha_characters, $captcha_input) != 0){
			echo "<h2><b>Captcha Failed! Try Again</b></h2><br>";
			echo "<p>Redirecting in 3</p>";
			$capture_success = false;
			header("refresh:3; url=../client_side/register.php");
		}
		$stmt->close();
	}else{
		echo $conn->error;
		exit;
	}

	if ($capture_success)
	{
		$query1 = "INSERT INTO FormDB_P8(studentid, username,password,profileremark) VALUES(?, ?, ?, ?)";
		//	htmlspecialchars and htmlentities() are extremely similar.
		//	But htmlentities() affects more special characters.
		$username = htmlentities(strip_tags($username));
		$studentid = htmlentities(strip_tags($studentid));
		$password = htmlentities(strip_tags($password));
		$profile_remark = htmlentities(strip_tags($profile_remark));

		$hashed_password = password_hash($password, PASSWORD_DEFAULT);
		if($stmt = $conn->prepare($query1)){
			$stmt->bind_param("ssss", $studentid, $username, $hashed_password, $profile_remark);
			$stmt->execute();
			$stmt->close();
		}
	}


?>
<html lang="en">
  <head>
    <title>Database Connection Example - Simple Address Book - PHP Output (UPDATE)</title>
  </head>
  <body>
    <?php
	if ($capture_success){
		echo "<h2>Sucessfully Registered User <em>$username</em></h2>";
	}
	?>
		

    <p><a href="../client_side/login.php">Return to login page</a></p>
  </body>
</html>
