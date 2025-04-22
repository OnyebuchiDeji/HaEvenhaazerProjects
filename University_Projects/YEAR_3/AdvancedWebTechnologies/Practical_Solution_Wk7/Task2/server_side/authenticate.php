<?php

include("connection.php");

$username = $_POST['username'];
$password = $_POST['password'];

$loggedin = false;

$username = htmlentities(strip_tags($username));
$password = htmlentities(strip_tags($password));

$query = "SELECT studentid, username, password, profileremark FROM LibDB WHERE username = ? LIMIT 1";

if($stmt = $conn->prepare($query)){
	$stmt->bind_param("s", $username);
	$stmt->execute();
	$stmt->bind_result($dbstudentid, $dbusername, $dbpassword, $dbprofileremark);
	while($stmt->fetch()){
		
		if(password_verify($password, $dbpassword)){
			$loggedin = true;
			// SUCCESS
			session_start();
			session_regenerate_id(); 
			$_SESSION['id'] = session_id();
			$_SESSION['studentid'] = $dbstudentid;
			$_SESSION['username'] = $dbusername;
			$_SESSION['profileremark'] = $dbprofileremark;
		}
	}
	$stmt->close();
}else{
	echo $conn->error;
	exit;
}

if($loggedin){
	$location = '../client_side/secure.php';
}else{
	// FAILURE
	$location = '../client_side/badauth.php';
}

header("Location: $location");
exit;
?>
