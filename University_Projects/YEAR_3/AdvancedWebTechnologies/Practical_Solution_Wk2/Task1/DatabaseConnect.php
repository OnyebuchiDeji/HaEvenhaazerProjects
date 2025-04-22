<!-- 
    Consider the alternatives that exist
 -->
<html>

<body>
    <h1>StudentsCSC30025_V1 Database Script</h1>

    <?php
        $servername = "katara.scam.keele.ac.uk";
        $username = "x7e30";
        $password = "x7e30x7e30";
        $dbname = "x7e30";

        $conn = mysqli_connect($servername, $username,
                $password, $dbname);
        
        //  Validate Connection
        if (!$conn){
            //  Die terminates the script. So no need for else block
            //  Aloso could do: `mysqli_error($conn)`
            die("Connection Failed: " . mysqli_connect_error());
        }
        
        echo "<h3>Connected to Database Server User <b>$username</b> Successfully<br><br></h3>";

        echo "<b><i>Note How the data printed from the associated array using foreach is not in order.</i></b><br><br>";

        $getAllFieldsSqlQuery = "select * from StudentsCSC30025_V1";
        
        //mysqli_query($conn, $getAllFieldsSqlQuery);
        $res1 = $conn->query($getAllFieldsSqlQuery);

        if ($res1 ->num_rows > 0){

            //  Also: mysqli_fetch_assoc($result);
            while ($row = $res1->fetch_assoc()){
                foreach($row as $colName=>$value){
                    echo "<b>$colName: $value </b><br>"; 
                }
                echo "<br>";
            }
        }
        else{
            echo "Table is empty!<br>";
        }

        //  also: mysqli_close($conn);
        $conn->close();
    ?>
</body>

</html>