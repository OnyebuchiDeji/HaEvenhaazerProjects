<?php
    /**
     *  Note the design.
     *  By either using `print_r` or `echo`
     *  the data is output.
     * 
     *  When this script is called as a web service using `curl`
     *  or any other similar app, this output is the response to
     *  that curl request, making the data available.
     */
    //  Get Database Class
    include_once '../structures/Database.php';

    //  Get User Class
    include_once '../structures/User.php';

    //  instantiate DB object
    $dbObj = new Database();
    $DBConn = $dbObj->GetConnection();

    $userObj = new User($DBConn, "Practical3");

    //  Set User Property Values
    if (!empty($_GET['username']) && !empty($_GET['password']))
    {
        $userObj->username = $_GET['username'];
        $userObj->password = $_GET['password'];
        $userObj->created = date('Y-m-d H:i:s');
    }else{
       echo "<b style=color:red>You've yet to enter any data!</b><br>";
       die("Error: Have not entered any details in GET request url.");
    }
    echo $userObj->username . "<br>";
    echo $userObj->password . "<br>";
    echo $userObj->created . "<br>";

    // echo strlen($userObj->username) . "<br>";
    // echo strlen($userObj->password) . "<br>";
    // echo strlen($userObj->created) . "<br>";

    // Signup the user
    if ($userObj->SignUp()){
        $user_arr = array(
            "status"=>true,
            "message"=>"Signup Successful!",
            "id"=>$userObj->id,
            "username"=>$userObj->username
        );
    }
    else{
        $user_arr = array(
            "status"=>false,
            "message"=>"User already exists!"
        );
    }
    print_r(json_encode($user_arr));
    

?>