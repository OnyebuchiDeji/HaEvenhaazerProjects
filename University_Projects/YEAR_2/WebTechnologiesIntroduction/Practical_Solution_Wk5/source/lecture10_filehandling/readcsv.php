<!DOCTYPE HTML><html>
    <head>
        <title>Reading Comma Separated Values</title>
    </head>
    <body>
        <!--
            fgetcsv delivers an array per line of CSV data
        -->
        <?php
            $row = 1;
            if (($handle=fopen("test.csv", "r")) !== FALSE)
            {
                while (($data=fgetcsv($handle, 1000, ",")) !== FALSE)
                {
                    $num = count($data);
                    echo "<p>$num fields in line $row: <br/>";
                    $row++;
                    for ($c = 0; $c < $num; $c++)
                    {
                        echo "*" . $data[$c] . "<br/>"; 
                    }
                    echo "</p>";
                }
                fclose($handle);
            }
        ?>
    </body>
</html>