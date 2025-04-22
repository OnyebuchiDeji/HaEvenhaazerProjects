<?php

    include_once '../structures/Database.php';
    include_once '../structures/Employee.php';

    //  Get Database Connection
    $DB = new Database();
    $dbConn = $DB->GetConnection();

    //  Initialize Emplyee Object
    $employeeObj = new Employee($dbConn, "employee");
    $employeeObj->name = isset($_POST['employeeName']) ? $_POST['employeeName'] : die("<b style=color:red>Please Submit Employee Info Through Form.</b>");
    $employeeObj->salary = isset($_POST['employeeSalary']) ? $_POST['employeeSalary'] : die("<b style=color:red>Please Submit Employee Info Through Form.</b>");
    $employeeObj->age = isset($_POST['employeeAge']) ? $_POST['employeeAge'] : die("<b style=color:red>Please Submit Employee Info Through Form.</b>");

    if ($employeeObj->Register()){
        $emp_arr=array(
            "status" => true,
            "message" => "Registered Successfully!",
            "id" => $user->id,
            "employeeName" => $employeeObj->name,
            "employeeSalary" => $employeeObj->salary,
            "employeeAge" => $employeeObj->age,
        );
    }
    else{
        $emp_arr=array(
            "status" => false,
            "message" => "Employee already exists!"
        );
    }
    print_r(json_encode($emp_arr));
?>