<!DOCTYPE HTML><html>
    <!--
        Done: Sun-25-Feb-2024
        I have test these

        In this version List.php also saves to and reads from a file stored locally on the server.

     -->
    <head>
        <style>
            .moduleName
            {
                font-family: Arial;
                color: white;
                background-color: rgb(192, 80, 77);
            }

            .moduleDetails
            {
                font-family: Arial;
            }

            .moduleName a {
                color: black;
                text-decoration: solid;
            }

            .moduleName a:hover
            {
                color: gray;
                text-decoration: overline;
            }
        </style>
    </head>

    <body>
        <?php
            $fileStoreName = "ModuleStoreCSV.csv";
            
            $writeableArray = array();
            $modules = array(
                "CSC-20021" => array(
                    "id" => "CSC-20021",
                    "name" => "Web Technologies",
                    "year" => 2
                ),
                "CSC-30012" => array(
                    "id" => "CSC-30012",
                    "name" => "Communications and Networks",
                    "year" => 3
                ),
                "CSC-10024" => array(
                    "id" => "CSC-10024",
                    "name" => "Programming I - Programming Fundamentals",
                    "year" => 1
                ),
            );

            //  Populate This Modules Array if file exists and is not empty
            $row = 1;
            
            //  If file is open and exists
            if (($csvReadHandle=fopen($fileStoreName, "r")) !== FALSE)
            {
                //  For every line
                while (($data=fgetcsv($handle, 1000, ",")) !== FALSE)
                {
                    //  Number of fields in that line
                    $num = count($data);
                    $row++;
                    $rowCell = 0;
                    $modules[$data[$rowCell]] = array(
                        "id"=> $data[$rowCell],
                        "name"=> $data[$rowCell + 1],
                        "year"=> $data[$rowCell + 2],
                    );
                }
            }
            else
            {
                //  Create the csv file and close it
                echo "File did not exist! Now creating. Whatever you add to form is added to the file!";
                $csvReadHandle=fopen($fileStoreName, "w");
                fclose($csvReadHandle);
            }


            //  Get and check if the entered information already exists...
            //  If it does't add it to modules module.
            //  If it doesn't skip it!
            if (isset($_POST["id"]))
            {
                $exists = false;
                $idPost = $_POST["id"];
                $namePost = $_POST["name"];
                $yearPost = $_POST["year"];
                foreach ($modules as $module)
                {
                    if ($idPost === $module["id"])
                    {
                        $exists = true;
                        break;
                    }
                }
                if ($exists !== true)
                {
                    $modules[$module["id"]] = array(
                        "id"=> $module["id"],
                        "name"=> $module["name"],
                        "year"=> $yearPost
                    );
                }
            }


            //  Write Each Module To File So that when Starting Anew, it would be loaded
            foreach ($modules as $module)
            {
                $writeableArray[] = array($module["id"], $module["name"], $module["year"]);
            }
            $csvFileHandle = fopen($fileStoreName, "a");
            foreach ($writeableArray as $fields)
            {
                fputcsv($csvFileHandle, $fields);
            }
            fclose($csvFileHandle);


            //  Display All as HTML Links
            foreach ($modules as $module)
            {
                echo "<a href=display_task2_get.php?name=$moduleItem[id]>". ": $moduleItem[id] </a>". "$moduleItem[name], Year $moduleItem[Year]". "\n";
            }


        ?>
    </body>
</html>
