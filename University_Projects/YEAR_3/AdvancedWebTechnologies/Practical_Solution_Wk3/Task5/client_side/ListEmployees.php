
<!DOCTYPE html>
<html>
    <head>
        <title>Task 2: RESTful API Web Services</title>
    </head>

    <body>
        <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">

            <label for="employeeName">Employee Name:</label>
            <input type="text" name="employeeName"/><br>
        
            <label for="employeeSalary">Employee Salary</label>
            <input type="number" name="employeeSalary"/><br>
            
            <label for="employeeAge">Employee Age</label>
            <input type="number" name="employeeAge"/><br>

            <input type="submit"/>
        
        </form>

        <br><br>

        <?php
            include_once '../server_side/structures/Database.php';
            include_once '../server_side/structures/Employee.php';
                                        

            $action = isset($_GET['action']) ? $_GET['action'] :  "l";
            $out_array = array();
            switch ($action){
                case "v":
                    //  First is View Employee
                    header ("location: ./ViewEmployee.php?id=$targetId");
                    break;
                case "d":
                    //  Next is Delete Employee
                    $DB = new Database();
                    $targetId = isset($_GET['targetId']) ? $_GET['targetId'] : -1;
                    echo "Target ID: $targetId";
                    $out_array = $DB->DeleteRecord("employee", $targetId);
                    break;
                case "u":
                    //  Next is Update Employee
                    $DB = new Database();
                    $targetId = isset($_GET['targetId']) ? $_GET['targetId'] : -1;
                    $newName = isset($_GET['employeeName']) ? $_GET['employeeName'] : "";
                    $newSalary = isset($_GET['employeeSalary']) ? $_GET['employeeSalary'] : "";
                    $newAge = isset($_GET['employeeAge']) ? $_GET['employeeAge'] : "";
                    $newData = array(
                        "employeeName"=>$newName,
                        "employeeSalary"=>$newSalary,
                        "employeeAge"=>$newAge,
                    );
                    $out_array = $DB->UpdateRecord("employee", $targetId, $newData);
                    break;
                default:
                    //  Get Database Connection
                    $DB = new Database();
                    $dbConn = $DB->GetConnection();

                    //  Initialize Employee Object
                    $lengthCheck = 1;
                    $employeeObj = new Employee($dbConn, "employee");
                    $employeeObj->name = isset($_POST['employeeName']) ? $_POST['employeeName'] : "";
                    $employeeObj->salary = isset($_POST['employeeSalary']) ? $_POST['employeeSalary'] : "";
                    $employeeObj->age = isset($_POST['employeeAge']) ? $_POST['employeeAge'] : "";

                    $lengthCheck = strlen($employeeObj->name) * strlen($employeeObj->salary) * strlen($employeeObj->age);
                    if ($lengthCheck > 0){
                        if ($employeeObj->Register()){
                            $out_array=array(
                                "status" => true,
                                "message" => "Employee Registered Successfully!",
                                "id" => $employeeObj->id,
                                "employeeName" => $employeeObj->name,
                                "employeeSalary" => $employeeObj->salary,
                                "employeeAge" => $employeeObj->age,
                            );
                        }
                        else{
                            $out_array["status"] = false;
                            $out_array["message"] = "Employee already exists!";
                        }
                    }
                    else{
                        $out_array["status"] = false;
                        $out_array["message"] = "To add employees, enter details into form!";
                    }

                    break;
                }
        ?>

        <div id="messages" style='background-color:black;color:lightgreen;padding:0.5%;'>
            <b >Messages</b><br>
            <?php
                // echo '<pre>';
                print_r(json_encode($out_array));
                // echo '<pre>';
            ?>
        </div>

        <br><br>
        

        <div id="Employee Table">
            <table>
                <tr>
                    <th>ID</th>
                    <th>Employee Name</th>
                    <th>Employee Salary</th>
                    <th>Employee Age</th>
                    <th>Update</th>
                    <th>Delete</th>
                </tr>
                <?php
                    
                    // $DB = new Database();
                    // $dbConn = $DB->GetConnection();
                    
                    $stmnt = $DB->GetAllRecords("employee");
                    

                    if ($stmnt->rowCount() > 0){
                        while ($row=$stmnt->fetch(PDO::FETCH_ASSOC)){
                            echo "<tr>";
                            echo "<th>" . $row['id'] . "</th>";
                            echo "<th>" . $row['employee_name']. "</th>";
                            echo "<th>" . $row['employee_salary'] . "</th>";
                            echo "<th>" . $row['employee_age'] . "</th>";
                            echo "<th><a href='./UpdateForm.php?targetId=" . $row['id'] . "'>Update</a></th>";
                            echo "<th><a href='./ListEmployees.php?action=d&targetId=" . $row['id'] . "'>Delete</a></th>";
                            echo "</tr>";
                        }
                    }

                ?>
            </table>
        </div>
    </body>
</html>