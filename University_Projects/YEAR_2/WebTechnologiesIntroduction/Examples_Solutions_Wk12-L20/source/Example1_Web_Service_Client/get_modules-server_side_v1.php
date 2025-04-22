<?php
    /**
     * This is getmodules.php -- This is a PHP Web service.
     * The php is used to get the data and provide it to the client side
     * Basically, this use the form of json files that has associative array-like data.
     */
    $file = file_get_contents("entries-associative_type.json", true);
    echo $file;
    //  Unset destroyss the specified variable -- in this case to free resources.
    unset($file);
?>