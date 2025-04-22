<!DOCTYPE HTML><html>
    <head>
        <title>
            Using PHP HTML CSS JavaSCript
        </title>
        <style>
            .moduleName
            {
                    font-family: Arial;
                    color: white;
                    background-color: rgb(192, 80, 77);
            }
            .moduleName2
            {
                font-family: Arial;
                color: rgb(192, 80, 77);
                background-color: white;
            }
        </style>
    </head>

    <body>
        <?php
            $modules = array("CSC-20021", "CSC-30012");
            foreach ($modules as $module)
            {
        ?>
            <span class='moduleName' onmouseover="highlight(this)"
            onmouseout="unhighlight(this)"><?= $module ?></span><br>
        <?php
            }
        ?>

        <script>
            function unhighlight(entity)
            {
                entity.className = "moduleName";
            }
            function highlight(entity)
            {
                entitiy.className = "moduleName2";
            }
        </script>
    </body>
</html>