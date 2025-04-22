
<?php

function printArray($array)
{
    foreach ($array as $person => $color)
    {
        //  Prints the value with the key
        echo "$person likes $color" . "<br/>";
    }
}

$fav_cols = array("Joe"=>"purple",
            "Elena" => "green",
            "Mark" => "brown",
            "Adrian" => "black",
            "Charles" => "red"
            );

printArray($fav_cols);
//  Add an element
$fav_cols["Bob"] = "orange";
printArray($fav_cols);

//  Remove
unset($fav_cols["Mark"]);
printArray($fav_cols);

//  change
$fav_cols["Joe"] = "blue";
printArray($fav_cols);

?>