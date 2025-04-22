<html>

    
<body>
    <h1>SQL Database Interface with PHP</h1>

    <?php

        //  Connect
        $serverName = "katara.scam.keele.ac.uk";
        $userName = "x7e30";
        $password = "x7e30x7e30";
        $dbname = "x7e30";

        $conn = mysqli_connect($serverName, $userName, $password, $dbname);

        //  Validate Connection
        if (!$conn){
            die("Error: Connection Failed: ".mysqli_connect_error());
        }
        else{
            echo "Connection Successful..."."<br>";
            $sqlQuery = "SELECT CustomerID, CustomerName, ContactName FROM Test";

            $result = $conn->query($sqlQuery);
            // echo "$result";
            if ($result->num_rows > 0){
                /**
                 *  Basically, `fetch_assoc()` acts like an iterator.
                 *  Subsquent calls to it return the subsequent rows of the table.
                 *  
                 *  and the returned value of fetch_assoc() is an associated array of the
                 *  column names and the values for each consecutive row.
                 */
                while ($row = $result->fetch_assoc()){
                    echo "StudentID: " . $row["CustomerID"] . ", " . "Name: " . $row["CustomerName"] . "<br>"; 
                }
                echo "Num Rows Attribute: " . $result->num_rows . "<br>";
            }
            else{
                echo "Nothing found from the Database. It's empty!";
            }
            //  Edit Database Table, `Test`
            $insertQuery = "
            insert into `Test`(`CustomerID`, `CustomerName`, `ContactName`, `Address`, `City`, `PostalCode`, `Country`)
            values
            (90, 'Wilman Kala',	'Matti Karttunen', 'Keskuskatu 45',	'Helsinki',	21240,	'Finland');
            ";

            /**
             *  This insert query does not result in an object that has the property `num_rows`
             *  Rather it results in either 1 or none, to possibly indicate successful insertion
             *  of values into the table -- a boolean.
             */
            $insertRes = $conn->query($insertQuery);
            echo "insertQuery: " . $insertQuery . "<br>";
            echo "insertRes Value: " . $insertRes . "<br>";
            // echo "insertRes Num Rows: " . $insertRes->num_rows . "<br>"; <-- results in nothing
            //  Since 
            // if ($insertRes){
            //     $row = $insertRes->fetch_assoc();
            //     foreach ($row as $key => $val){
            //         echo "Key: ". $key . ", Value: " . $val . "<br>";
            //     }
            // }
            $getQuery = "SELECT CustomerID, CustomerName, ContactName FROM Test";
            $result2 = $conn->query($getQuery);
            $rows = $result2->fetch_assoc();

            if ($result2->num_rows > 0){
                foreach ($rows as $key => $val){
                    echo "Key: " . $key . ", Value: " . $val . "<br>";
                }
            }
            $conn->close();
        }


    ?>
</body>

</html>