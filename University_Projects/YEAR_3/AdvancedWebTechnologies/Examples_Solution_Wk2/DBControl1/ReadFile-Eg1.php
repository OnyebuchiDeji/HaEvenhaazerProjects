

<?php
    $xmlData = fopen("cd_catalog.xml", "r") or
        die("Unable to open file!");
    echo "XML File Read Successfully:<br>";
    echo fread($xmlData, filesize("cd_catalog.xml"));
    fclose($xmlData);

    $xmlCDread = simplexml_load_file("cd_catalog.xml");
    echo "$xmlCDread";
?>
