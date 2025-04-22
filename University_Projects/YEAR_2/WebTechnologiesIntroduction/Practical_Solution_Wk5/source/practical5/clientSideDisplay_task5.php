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
            $id = "CSC-10025";
            $name = "Cybercrime";
            $year = 1;

            echo "<a href=display_task2_get.php?id=$id&name=$name&year=$year</a>" . "\n";
        ?>

    </body>
</html>