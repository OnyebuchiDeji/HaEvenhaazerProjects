<?php
    /**
     * This is getmodules.php -- This is a PHP Web service.
     * The php is used to get the data and provide it to the client side.
     * This version gets the contents of a list-like form of json
     */
    $file = file_get_contents("entries3-list_type.json", true);
    echo $file;
    //  Unset destroyss the specified variable -- in this case to free resources.
    unset($file);
?>