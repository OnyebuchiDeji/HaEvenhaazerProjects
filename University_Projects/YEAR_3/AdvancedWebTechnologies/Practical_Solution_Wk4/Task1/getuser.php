<!DOCTYPE HTML><html>
    <head>
        <style>
            table{
                width: 100%;
                border-collapse: collapse;
            }           

            table, td, th {
                border: 1px solid black;
                padding: 5px;
            }

            th {text-align: left;}
        </style>
    </head>

    <body>
        <?php
            $inputQueryVal = intval($_GET['q']);
            $method = $_GET['choice'];
    
            //  The server and database details
            $servername = "katara.scam.keele.ac.uk";
            $username = "x7e30";
            $password = "x7e30x7e30";
            $dbname = "x7e30";

            $conn = mysqli_connect($servername, $username, $password, $dbname);
            if (!$conn){
                die("Could not Connect to Database {$dbname}: " . mysqli_error($conn));
            }

            mysqli_select_db($conn, "ajax_example");
            //  Prepare the SQL query
            $query = "select * from student where sunumber = '".$inputQueryVal."'";
            $result = mysqli_query($conn, $query);  //  Execute SQL Statement

            if (strlen($method) <= 1){
                echo "<table>
                <tr>
                <th>StudentID</th>
                <th>Name</th>
                <th>Address</th>
                <th>Email</th>
                </tr>
                ";
                while ($row = mysqli_fetch_array($result)){
                    echo "<tr>";
                    echo "<td>" . $row['StudentID'] . "</td>";
                    echo "<td>" . $row['Name'] . "</td>";
                    echo "<td>" . $row['Address'] . "</td>";
                    echo "<td>" . $row['email'] . "</td>";
                    echo "</tr>";
                }
                echo "</table>";
            }else{
                echo "<table>
                <tr>
                <th>StudentID</th>
                <th>Name</th>
                <th>Email</th>
                </tr>
                ";
                while ($row = mysqli_fetch_array($result)){
                    echo "<tr>";
                    echo "<td>" . $row['StudentID'] . "</td>";
                    echo "<td>" . $row['Name'] . "</td>";
                    echo "<td>" . $row['email'] . "</td>";
                    echo "</tr>";
                }
                echo "</table>";

            }
            mysqli_close($conn);
        ?>
    </body>
</html>