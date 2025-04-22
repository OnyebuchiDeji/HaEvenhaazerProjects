<!DOCTYPE HTML><html>
    <!--
        Done: Sun-25-Feb-2024
        I have test these

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

            .moduleName a {color: white;}
        </style>
    </head>

    <body>
        <?php
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

            foreach ($modules as $module)
            {
                echo "<a href=display_task2_get.php?name=$moduleItem[id]>". ": $moduleItem[id] </a>". "$moduleItem[name], Year $moduleItem[Year]". "\n";
            }


        ?>
    </body>
</html>
