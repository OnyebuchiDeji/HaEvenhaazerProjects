<!DOCTYPE html><html>
    <head>
        <title>Writing CSV Data</title>
    </head>
    <body>
        <!--

        -->
        <?php
            $list = array
            (
                array("ESV", "KDF", "MSN", "DFR"),
                array("487", "950", "125"),
                array('"TOE"', '"SHA"')
            );

            $fp = fopen("writecsv.csv", "w");

            foreach ($list as $fields)
            {
                fputcsv($fp, $fields);
            }
            fclose($fp);

            echo "Done!";
        ?>
    </body>
</html>