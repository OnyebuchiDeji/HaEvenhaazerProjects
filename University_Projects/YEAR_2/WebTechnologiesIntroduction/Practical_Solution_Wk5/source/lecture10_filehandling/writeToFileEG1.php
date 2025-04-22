<!DOCTYPE html><html>
    <head>
        <title>Writing To Files Using Handle</title>
    </head>
    <body>
        <?php
            //  Write Mode
            $handle = fopen("data_write.txt", "w");
            $text = "God is Father\n";
            $result = fwrite($handle, $text);
            fclose($handle);

            //  Append Mode
            $handle = fopen("data_write.txt", "a");
            $result = fwrite($handle, "My God!");
        ?>
    </body>
</html>