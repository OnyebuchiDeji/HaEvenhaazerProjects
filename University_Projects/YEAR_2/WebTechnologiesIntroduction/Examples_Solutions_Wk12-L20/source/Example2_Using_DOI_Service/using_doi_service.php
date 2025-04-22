<?php

    $opts = array(
            'http'=>array(
                "method"=>"GET",
                "header"=>"Accept:application/x-bibtex"
            )
        );
    
    //  Creates and returns a stream context with any options given.
    //  The stream enables data to be taken from whatever url is associated with it.
    //  THe stream context itself specifies the way that data is taken from the url
    $context = stream_context_create($opts);
    $file = file_get_contents("http://dx.doi.org/10.1016/j.algal.2015.04.001", false, $context);
    echo($file);
?>