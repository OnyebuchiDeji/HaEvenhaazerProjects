
<html>
<head>
    <title>Form to Query PHP Script to Get a Student from Database StudentsCSC30025_V1</title>
</head>

<body>
    <h1>Check for the existence of this student's first and last name</h1>
    <form name="form" action="" method="get">
        <!--
            Don't forget that it is the name property that PHP uses
            to access them in the $_GET global variable
        -->
        <label for="FName">First Name: </label>
        <input type="text" name="FName" id="FName" value="">

        <label for="LName">Last Name: </label>
        <input type="text" name="LName" id="LName" value="">

        <input type="submit" value="Search"/>
    </form>

    <?php
        $fNameSearchQuery = "";
        $lNameSearchQuery = "";
        if (empty($_GET['FName']) || empty($_GET['LName'])){
            echo "<b>Waiting for Client to Enter Search First Name and Last Name.</b><br><br>";
        }else{
            $fNameSearchQuery = $_GET['FName'];
            $lNameSearchQuery = $_GET['LName'];

            if ($fNameSearchQuery){
                $fNameSearchQuery = trim($fNameSearchQuery); 
            }
            if ($lNameSearchQuery){
                $lNameSearchQuery = trim($lNameSearchQuery); 
            }
            echo "Client Searching for: $fNameSearchQuery $lNameSearchQuery<br>";
        }


        //  Connect to database
        $serverName = "katara.scam.keele.ac.uk";
        $userName = "x7e30";
        $password = "x7e30x7e30";
        $dbName = "x7e30";

        //  Connect
        $conn = mysqli_connect($serverName, $userName, $password, $dbName);

        //  Validate Connection
        if (!$conn){
            //  Kill Script
            die("Error: Could not connect to database of user ". $userName . " " . mysqli_error($conn));
        }

        echo "<h3>Successfully Connected to Database <b>{Server Name: $serverName, User: $userName}</b></h3><br><br>";

        //  Inquire
        $sqlSelectquery = "select StudentID, FName, LName from StudentsCSC30025_V1";
        $res1 = mysqli_query($conn, $sqlSelectquery);

        $PresentFlag = 0;
        $debugFlag = false;
        $studentID = "";
        //  If res1 is valid, loop through, searching for the name value like the `formNameSearchQuery`
        if ($res1->num_rows > 0)
        {
            while ($row = mysqli_fetch_assoc($res1))
            {
                //  Compare the input names and the names gotten from the database
                $dbFName = $row['FName']; 
                $dbLName = $row['LName'];
                $studentID = $row['StudentID'];
 
                //  strcmp returns 0 when the strings are exactly thr same
                $fNamePresent = strcmp($fNameSearchQuery, $dbFName);
                $lNamePresent = strcmp($lNameSearchQuery, $dbLName);

                if ($debugFlag){

                    echo "FName Present: $fNamePresent<br>";
                    echo "LName Present: $lNamePresent<br>";
    
                    echo "searhFName: $fNameSearchQuery<br>";
                    echo "searchLName: $lNameSearchQuery<br>";
                    echo "dbFName: $dbFName<br>";
                    echo "dbLName: $dbLName<br>";
    
                    echo "<br>";
    
                    //  Can't do this. strlen won't be evaluated
                    // echo "searhFName Length: strlen($fNameSearchQuery)<br>";
                    // echo "searchLName Length: strlen($lNameSearchQuery)<br>";
                    // echo "dbFName Length: strlen($dbFName)<br>";
                    // echo "dbLName Length: strlen($dbLName)<br>";
                    $fNameLength = strlen($fNameSearchQuery);
                    $lNameLength = strlen($lNameSearchQuery);
                    $dbFNameLength = strlen($dbFName);
                    $dbLNameLength = strlen($dbLName);
                    echo "searhFName Length: $fNameLength <br>";
                    echo "searchLName Length: $lNameLength <br>";
                    echo "dbFName Length: $dbFNameLength <br>";
                    echo "dbLName Length: $dbLNameLength <br>";
                    echo "<br>";    
                }

                if (!$fNamePresent && !$lNamePresent){
                    $PresentFlag = 1;
                }
            }

            if ($PresentFlag){
                echo "<h4><b>Indeed $fNameSearchQuery $lNameSearchQuery is present in the Students Database</b></h4><br>";
                echo "Full Name: <b>$fNameSearchQuery $lNameSearchQuery</b>, StudentID: <b>$studentID</b><br>";
            }
            else{
                echo "<h4><b>Student $fNameSearchQuery $lNameSearchQuery not present in the Students Database</b></h4><br><br>";
            }
        }
        else{
            mysqli_close($conn);
        }
    ?>
</body>
</html>