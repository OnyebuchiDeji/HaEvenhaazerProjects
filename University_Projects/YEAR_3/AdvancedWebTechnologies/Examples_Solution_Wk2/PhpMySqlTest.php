<!DOCTYPE html><html>

    <head>
        <title>Database Connectivity with PHP
    </head>

    
    <body>
        <h1>SQL Database Interface with PHP</h1>

        <?php

            //  Connect
            $serverName = "https://www.teach.scam.keele.ac.uk/phpmyadmin/";
            $userName = "x7e30";
            $password = "x7e30x7e30";
            $dbname = "x7e30";

            $conn = mysqli_connect($serverName, $userName, $password, $dbname);

            //  validate Connection
            if (!$conn){
                die("Connection Failed: ".mysqli_connect_error());
            }
            else{
                echo "Connection Successful..."."<br>";
                $sql = "SELECT StudentID, FirstName, FROM student";
                $result = $conn->query($sql);
                if ($result->num_rows > 0){
                    while ($row = $result->fetch_assoc()){
                        echo "StudentID: " . $row["StudentID"] . ", " . "First Name: " . $row["FirstName"] . "<br>"; 
                    }
                }
                else{
                    echo "Nothing found from the Database. It's empty!";
                }
                $conn->close();
            }
            //  Create Database Table


            //  Add information into table


            //  Retrieve all records and display
        ?>
    </body>

</html>