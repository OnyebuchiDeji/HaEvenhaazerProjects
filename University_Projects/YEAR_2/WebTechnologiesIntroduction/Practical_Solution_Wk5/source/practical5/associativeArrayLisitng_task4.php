<!DOCTYPE HTML><html>
    <!--
        Done: Sat-25-Feb-2024
        I have test these
     -->
    <head>
        <style>
            .moduleName
            {
                font-family: Arial;
                color: white;
                background-color: rgb(192, 80,72);
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
                    "name" => "Communications and Networks!",
                    "year" => 3
                ),
                "CSC-10024" => array(
                    "id" => "CSC-10024",
                    "name" => "Programming I - Programming Fundamentals",
                    "year" => 1
                ),
            );

            foreach ($modules as $moduleItem)
            {
                echo "<a href=display_task2_get.php?name=$moduleItem[id]>". ": $moduleItem[id] </a>". "$moduleItem[name], Year $moduleItem[Year]". "\n";
            }
        ?>

    </body>
</html>