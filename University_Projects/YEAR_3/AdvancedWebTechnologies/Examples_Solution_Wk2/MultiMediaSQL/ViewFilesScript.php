<!DOCTYPE html><html>

<head>
    <title>View Images</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
        img{
            width: 25%;
        }
    </style>
</head>

<body>

    <?php

        include_once("ConnectionScript.php");
        
        echo "<h2>View of All Uploaded Files</h2><br>";

        //  Checks if statement is valid
        if ($stmnt = mysqli_prepare($conn, "select * from P2Imgs")){
            
            //  Exectutes and gets all the records of the table
            mysqli_stmt_execute($stmnt);

            //  binds each record's field data to the following variables
            //  so that the variables refer to each subsequent record
            mysqli_stmt_bind_result($stmnt, $fileId, $filename, $filepath);

            //  For each record in the returned associated-list formatted table data
            while (mysqli_stmt_fetch($stmnt)){
                echo "<h4>Picture $fileId: $filename. '$filepath'</h4>";
                echo "<img src='./resources/imageUploadStoreDir/$filepath' />";
                echo "<hr>";
            }

            echo "<br>";

            //  Shutdown statement execution

            mysqli_stmt_close($stmnt);
            echo "Go to <a href='UploadForm.php'>Upload Page</a><br>";
            
        }
        
    ?>
</body>

</html>