<!DOCTYPE HTML><html>
    <head>
        <title>Write To File Using File_Put_Contents</title>
    </head>

    <body>
        <?php
            //  Open the file to get existing content
            $file = "data_write.txt";

            //  Append a new person to the data
            $current = file_get_contents($file);
            $current .= "Glory!\n";
        
            //  Write the contents back to the file
            file_put_contents($file, $current);

            if (empty($result))
            {
                echo "Could not write to the file!";
            }
            else
            {
                echo "Done! Number of Bytes: " . $result;
            }
        ?>
    </body>
</html>