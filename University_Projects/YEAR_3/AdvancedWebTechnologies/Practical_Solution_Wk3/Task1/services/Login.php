<?php
    //  Include Database and USer Classes
    include_once '../structures/Database.php';
    include_once '../structures/User.php';

    //  Get Database Connection
    $dbObj = new Database();
    $dbConn = $dbObj->GetConnection();

    //  Initialize User Object
    $userObj = new User($dbConn, "Practical3");
    //  Set ID Property of User Object
    $userObj->username = isset($_GET['username']) ? $_GET['username'] : die("<b style=color:orange>Username or Password not entered!</b>");
    $userObj->password = isset($_GET['password']) ? $_GET['password'] : die("<b style=color:orange>Username or Password not entered!</b>");
    //  Read the details of the user to be edited
    $stmnt = $userObj->Login();

    /**
     *  NOTE!   Also consider the varaible, 'user_arr' 
     *  that though it is defined in the if block, its scope still extends
     *  to outside the block, hence why it's printed.
     *  Though this may be because it's an associative array object
     */

    if ($stmnt->rowCount() > 0){
        //  Get Row
        $row = $stmnt->fetch(PDO::FETCH_ASSOC);
        //  Create Array to Output
        $user_arr = array(
            "status"=>true,
            "message"=>"Login Successful!",
            "id"=>$row['id'],
            "username"=>$row['username']
        );
    }else{
        $user_arr=array(
            "status"=>false,
            "message"=>"Invalid Username or Password!",
        );
    }
    //  Make it in JSON format and output
    print_r(json_encode($user_arr));
?>