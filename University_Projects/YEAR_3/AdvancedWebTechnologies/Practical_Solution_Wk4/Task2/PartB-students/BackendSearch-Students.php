<?php
    //  Attempt MySQL Server Connection
    $conn = mysqli_connect("katara.scam.keele.ac.uk", "x7e30", "x7e30x7e30", "x7e30");

    //  Check Connection
    if ($conn === false){
        die("ERROR: could not connect. " . mysqli_connect_error());
    }

    if (isset($_REQUEST['term'])){
        //  Prepare a select statement
        //  '?' will be replaced later
        $query = "select * from student where Name like ?";

        if ($stmnt = mysqli_prepare($conn, $query)){
            //  Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmnt, "s", $param_term);

            //   Set parameters 
            $param_term = $_REQUEST['term'] . '%';

            //  Attempt to execute the prepared statement
            if (mysqli_stmt_execute($stmnt)){
                $result = mysqli_stmt_get_result($stmnt);

                //  Check the no. of rows in the returned results
                if (mysqli_num_rows($result) > 0){
                    //  Fetch each consecutive result rows as an associated array
                    while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)){
                        echo "<p>" . $row['Name'] . "</p>";
                    }
                }else{
                    echo "<p>No matches found</p>";
                }
            }else{
                echo "ERROR: Couldn't execute $query. " . mysqli_error($conn);
            }
        }

        //  Close Statement
        mysqli_stmt_close($stmnt);
    }

    //  Close Connection
    mysqli_close($conn);
?>