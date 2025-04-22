
<!DOCTYPE html>
<html>
    <head>
        <title>Task 2: RESTful API Web Services</title>
    </head>

    <body>
        <form method="get" action="./ListEmployees.php">

            <label for="employeeName">Employee Name:</label>
            <input type="text" name="employeeName"/><br>
        
            <label for="employeeSalary">Employee Salary</label>
            <input type="number" name="employeeSalary"/><br>
            
            <label for="employeeAge">Employee Age</label>
            <input type="number" name="employeeAge"/><br>

            <input style='display:none;' type="text" name="action" value="u"/>
            <input style='display:none;' type="number" name="targetId" value="<?php echo $_GET['targetId'];?>"/>

            <input type="submit"/>
        
        </form>
    </body>
</html>