<!DOCTYPE html><html>
    <head>
        <title>File Reading With No File Handle</title>
    </head>
    <body>
        <!--
            One can readfrom files on the server where the php scrupt is...
            and put their contents into variables
         -->
        <?php
            $fileData = file_get_contents('file1EG1.txt');
            echo $fileData
        ?>
    </body>
</html>