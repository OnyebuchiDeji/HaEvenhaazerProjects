<!DOCTYPE HTML><html>
    <!-- Using PHP only where needed! -->
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
        ?>
                <!-- Using PHP only where needed! -->
                <span class='moduleName'><?php echo $module ?></span><br>
        <?php
            }
        ?>
    </body>
</html>