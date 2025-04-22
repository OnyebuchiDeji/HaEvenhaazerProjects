<?php
/*
    Files with only php do not need the <?php ?>
*/
    $modules = array("CSC-20021", "CSC-30012");
    echo "<html><body>";
    foreach ($modules as $module)
    {
        echo "<span style='color: red'>$module</span><br>";
    } 
    echo "</html></body>";
?>