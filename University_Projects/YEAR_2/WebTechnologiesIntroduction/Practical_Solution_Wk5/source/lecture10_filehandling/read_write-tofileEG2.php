<!DOCTYPE html><html>
    <head>
        <title>File Reading and Writing <em>With</em> File Handle</title>
    </head>
    <body>
        <!--
            One can readfrom files on the server where the php scrupt is...
            and put their contents into variables
         -->
        <?php
            $fileName = "file1EG2.txt";
            if (file_exists($fileName))
            {
                $fileData = file_get_contents($fileName);
                echo $filedata;
            }
            else
            {
                //  Need to create a handle
                $writeHandle = fopen($fileName, "w");
                //  fgets returns a line!
                $text = "This file did not exist. Created it through php!";
                $result = fwrite($writeHandle, $text);
                fclose($handle);
                echo "$fileName" . " has been created!";
            }

            //  Using handles to read the file...
            $readHandle = fopen($fileName, "r");
            while (($buffer = fgets($readHandle, 4096)) !== false)
            {
                echo $buffer;
            }
            fclose($readHandle);
            echo "$fileName" . " has been read!";
        ?><br>
    </body>
</html>