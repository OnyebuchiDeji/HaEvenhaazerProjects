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

            .moduleName a {color: white;}
        </style>
    </head>

    <body>
        <?php
            $modules = array("CSC-20021", "CSC-30012");

            foreach ($modules as $module)
            {
                echo "$module" . "\n";
            }
        ?>

    </body>
</html>