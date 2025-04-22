
<!DOCTYPE html>
<html>
    <head>
        <title>Task 2: RESTful API Web Services</title>
    </head>

    <body>
        <form method="get" action="<?php echo $_SERVER['PHP_SELF']; ?>">
            <h4>View The Salary Report for all employees from the start id to the end id.</h4>
            <br>
            <label for="startId">Start ID:</label>
            <select name="startId">
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
            </select><br>
        
            <label for="endId"> Salary</label>
            <select name="endId">
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
            </select><br>
            
            <input type="submit"/>
        
        </form>

        <br><br>

        <div id="Employee Table">
            <h2><b>Employee Salary Summary Table</b></h2>

            <table style='border:5px solid blue;'>
                <tr style='padding:1.5%;'>
                    <th>ID</th>
                    <th>Employee Name</th>
                    <th>Employee Salary</th>
                </tr>
                <?php
                    include_once '../server_side/structures/Database.php';
                    include_once '../server_side/structures/Employee.php';
                    $DB = new Database();

                    $startId = isset($_GET['startId']) ? $_GET['startId'] : die("<b style=color:blue>Please Choose a Start ID.</b>");
                    $endId = isset($_GET['endId']) ? $_GET['endId'] : die("<b style=color:blue>Please Choose an End ID.</b>");
                    // echo "StartId: $startId <br>";
                    // echo "EndId: $endId <br>";
                    
                    $stmnt = $DB->GetAllRecords("employee");
                    $totalSalary = 0;

                    if ($stmnt->rowCount() > 0){
                        while ($row=$stmnt->fetch(PDO::FETCH_ASSOC)){
                            if ($row['id'] < $startId){continue;}
                            elseif ($row['id'] > $endId){continue;}
                            echo "<tr>";
                            echo "<th>" . $row['id'] . "</th>";
                            echo "<th>" . $row['employee_name']. "</th>";
                            echo "<th>" . $row['employee_salary'] . "</th>";
                            echo "</tr>";

                            $totalSalary += (int)$row['employee_salary'];
                        }
                    }
                ?>
            </table>
            <h4>Total Salary: <b><?php echo"$totalSalary"; ?></b></h4>
        </div>
    </body>
</html>