<?php

include("connection.php");

$username = $_POST['username'];
$password = $_POST['password'];
$injection = $_POST['injection'];
$recent_injection = $injection;
$loggedin = false;

$username = htmlentities(strip_tags($username));
$password = htmlentities(strip_tags($password));

$injection = htmlentities(strip_tags($injection));

$query = "SELECT studentid, username, password, sandboxtext FROM LibDB_SNDBX WHERE username = ? LIMIT 1";

if($stmt = $conn->prepare($query)){
	$stmt->bind_param("s", $username);
	$stmt->execute();
	$stmt->bind_result($dbstudentid, $dbusername, $dbpassword, $dbinjection);
	while($stmt->fetch()){
		
		if(password_verify($password, $dbpassword)){
			$loggedin = true;
			// SUCCESS
			session_start();
			session_regenerate_id(); 
			$_SESSION['id'] = session_id();
			$_SESSION['studentid'] = $dbstudentid;
			$_SESSION['username'] = $dbusername;
			$_SESSION['injection'] = $dbinjection;
			$_SESSION['tried_injection'] = $recent_injection;
			$_SESSION['first_injection'] = $reg_injection;
			$_SESSION['current_injection'] = $injection;
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
