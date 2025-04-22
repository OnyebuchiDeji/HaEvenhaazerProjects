<!DOCTYPE HTML><html>
    <!-- Embedding PHP -->
    <head>
        <style>
            .moduleName
            {
                font-family: Arial;
                color: white;
                background-color: rgb(192, 80, 77);
            }
        </style>
    </head>
    <body>
        <?php
            $modules = array("CSC-20021", "CSC-30012");
            foreach ($modules as $module)
            {
                echo "<span class='moduleName'>
                $module</span><br>";
            }
        ?>
    </body>
</html>