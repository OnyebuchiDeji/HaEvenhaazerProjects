<?php
    /**
     * This is getmodules.php -- This is a PHP Web service.
     * The php is used to get the data and provide it to the client side.
     * This also uses the json files that store data in an associative array form
     */
    $file = file_get_contents("entries2-associative_type.json", true);
    echo $file;
    //  Unset destroyss the specified variable -- in this case to free resources.
    unset($file);
?>