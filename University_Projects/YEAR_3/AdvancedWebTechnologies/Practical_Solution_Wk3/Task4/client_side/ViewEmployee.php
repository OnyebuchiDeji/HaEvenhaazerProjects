
<!DOCTYPE html>
<html>
    <head>
        <title>Task 2: RESTful API Web Services</title>
    </head>

    <body>
        <form method="get" action="<?php echo $_SERVER['PHP_SELF']; ?>">
            <h4>Choose an Employee based on their ID</h4>
            <label for="employeeId">Employee ID:</label>
            <select name="employeeId">
                <?php
                     include_once '../server_side/structures/Database.php';
                     include_once '../server_side/structures/Employee.php';
                     $DB = new Database();
                     // $dbConn = $DB->GetConnection();
                     
                     $stmnt = $DB->GetAllRecords("employee");
 
                     if ($stmnt->rowCount() > 0){
                         while ($row=$stmnt->fetch(PDO::FETCH_ASSOC)){
                             echo "<option value='" . $row['id'] . "'>" . $row['id'] . "</option>";
                         }
                     }
                ?>
            </select>

            <br>
            <input type="submit"/>
        
        </form>

        <div style='color:lightgreen; background-color:black; margin:1.5%; padding:1.5%;align-self:center;' id="Employee_Details">
            <?php
                include_once '../server_side/structures/Database.php';
                include_once '../server_side/structures/Employee.php';
                $DB = new Database();

                $requestedId = isset($_GET['employeeId']) ? $_GET['employeeId'] : die("<b style=color:blue>Please Choose an ID.</b>");
                
                $stmnt = $DB->GetAllRecords("employee");
 
                if ($stmnt->rowCount() > 0){
                    while ($row=$stmnt->fetch(PDO::FETCH_ASSOC)){
                        if ($row['id'] == $requestedId){
                            echo "<div style='font-size:1.5rem;padding:auto;margin:auto;text-align:left;'>";
                            echo "Here is the information for employee <b>ID: $requestedId</b><br>";
                            echo "Name:     " . $row['employee_name'] . "<br>";
                            echo "Salary:   " . $row['employee_salary'] . "<br>";
                            echo "Age:      " . $row['employee_age'] . "<br>";
                            echo "</div>";
                        }
                    }
                }
            
            ?>
        </div>
    </body>
</html>