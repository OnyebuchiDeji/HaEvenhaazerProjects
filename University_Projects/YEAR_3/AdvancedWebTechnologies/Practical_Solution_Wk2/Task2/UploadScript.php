<?php

    include_once("ConnectionScript.php");
    $imageName = $_POST["ImageName"];

    //  Get File Data from Client Device's dir
    if ($_FILES["ImageData"]["size"] < 20000000){
        //  Check for errors
        if ($_FILES["ImageData"]["error"] > 0){
            echo "Error: " . $_FILES["ImageData"]["error"] . "<br>";
        }
        else{
            //  Get the file's actual name, not the the name input by user
            $fileName = $_FILES["ImageData"]["name"];
            $fileType = $_FILES["ImageData"]["type"];   //  Get type

            //  Specify the directory to store the uploaded file in within the Server Device
            $fileUploadStoreDir = "./resources/imageUploadStoreDir/";

            /**
             * Search Server-Side Upload Store Directory for whether that file name exists
             *  If the same file is uploaded, it appends the date and time to the file path
             */
            $i = 0;
            $renamed = 0;

            while (file_exists($fileUploadStoreDir . $fileName)){
                $fileNameArray = explode(".", $fileName);
                $fileName = "";

                for ( ; $i<count($fileNameArray) - 1; $i++){
                    //  This gets the fileName without the extension e.g. (.png)
                    $fileName .= $fileNameArray[$i].".";
                    // echo "$fileNameArray[$i]";
                }
                //  So that it can append date and time to the file name
                //  because the same file was uploaded again.
                $fileName .= date("Y-m-d-H-i-s").".";
                //  finally append the extension, which is the last or end value of the fileNamArray
                $fileName .= end($fileNameArray);
                $renamed = true;
            }

            //  Move the file to the resource/imageUploadStoreDir folder on the server script
            move_uploaded_file($_FILES["ImageData"]["tmp_name"], $fileUploadStoreDir . $fileName);

            if ($renamed){
                echo "File Already Exists. Renaming uploaded file to $fileName<br>";
            }

            //  The '?' is a placeholder for values
            //  that will be added afterwards
            $statement = "insert into P2Imgs(filename, filepath) VALUES(?, ?)";
            if ($stmnt = mysqli_prepare($conn, $statement)){
                //  This statement bind is what appends uses the imageName and fileName
                //  to replace the two '?' in VALUES(?, ?)
                mysqli_stmt_bind_param($stmnt, "ss", $imageName, $fileName);

                // Execute Query
                mysqli_stmt_execute($stmnt);
                mysqli_stmt_close($stmnt);
                echo "File Uploaded. <a href='ViewFilesScript.php'>View All Files</a><br>";
            }
            else{
                echo "MySQL Error: " . mysqli_error($conn) . "\n<br>";
            }
        }
    }
    else{
        echo "File is Too Large<br>";
    }

?>