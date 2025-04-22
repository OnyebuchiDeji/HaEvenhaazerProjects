<?php
    /**
     * This is getmodules.php -- This is a PHP Web service.
     * The php is used to get the data and provide it to the client side.
     */
    $file = file_get_contents("entries.json", true);
    echo $file;
    //  Unset destroyss the specified variable -- in this case to free resources.
    unset($file);
?>