<!DOCTYPE HTML><html>
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
            <!--
                 This: '<'?= $module '?>' for '<'? php echo $module '?>'
            -->
            <span class='moduleName'><?= $module ?></span><br>
        <?php    
            }
        ?>
    </body>
</html>