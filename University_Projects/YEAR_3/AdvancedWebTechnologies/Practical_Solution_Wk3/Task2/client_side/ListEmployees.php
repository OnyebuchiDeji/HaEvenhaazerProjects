
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

        <div id="messages" style='background-color:black;color:lightgreen;padding:0.5%;'>
            <b >Messages</b>
            <?php

                include_once '../server_side/structures/Database.php';
                include_once '../server_side/structures/Employee.php';

                //  Get Database Connection
                $DB = new Database();
                $dbConn = $DB->GetConnection();

                //  Initialize Employee Object
                $employeeObj = new Employee($dbConn, "employee");
                $employeeObj->name = isset($_POST['employeeName']) ? $_POST['employeeName'] : die("<b style=color:red>Please Submit Employee Info Through Form.</b>");
                $employeeObj->salary = isset($_POST['employeeSalary']) ? $_POST['employeeSalary'] : die("<b style=color:red>Please Submit Employee Info Through Form.</b>");
                $employeeObj->age = isset($_POST['employeeAge']) ? $_POST['employeeAge'] : die("<b style=color:red>Please Submit Employee Info Through Form.</b>");

                if ($employeeObj->Register()){
                    $emp_arr=array(
                        "status" => true,
                        "message" => "Employee Registered Successfully!",
                        "id" => $employeeObj->id,
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
        </div>

        <br><br>
        
        <div id="Employee Table">
            <table>
                <tr>
                    <th>ID</th>
                    <th>Employee Name</th>
                    <th>Employee Salary</th>
                    <th>Employee Age</th>
                </tr>
                <?php
                    include_once '../server_side/structures/Database.php';
                    include_once '../server_side/structures/Employee.php';
                    $DB = new Database();
                    // $dbConn = $DB->GetConnection();
                    
                    $stmnt = $DB->GetAllRecords("employee");
                    

                    if ($stmnt->rowCount() > 0){
                        while ($row=$stmnt->fetch(PDO::FETCH_ASSOC)){
                            echo "<tr>";
                            echo "<th>" . $row['id'] . "</th>";
                            echo "<th>" . $row['employee_name']. "</th>";
                            echo "<th>" . $row['employee_salary'] . "</th>";
                            echo "<th>" . $row['employee_age'] . "</th>";
                            echo "</tr>";
                        }
                    }

                ?>
            </table>
        </div>
    </body>
</html>