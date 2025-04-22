<?php
/**
	This code is part of Lecture 17 - Security in Web Technologies by Dr. Goskel Misirli.
	
	This code was written on Wed-3-April-2024, done from examples on this site: https://phppot.com/php/php-htmlentites/
	
	The htmlentities() function converts a string with special characters to a form that can be interpreted by html.
	For example, unicode characters like 
		
	The goal of this code is to show the use of htmlentities() function in validating some input.
	In this example, the difference between using htmlentities() vs htmlspecialchars() is shown.
	htmlspecialchars() is limited to doing what htmlentities() does only with this limited types of characters:
	ampersand, double quotes, single quotes, greater than, and less than characters, to convert them to their appropriate html representation...
	that is, a form that html is able to interprete and display properly.
 */

$input_string = "HTML © symbol";
echo "Using htmlspecialchars() gives this: <br/><br/>";
echo $output = htmlspecialchars($input_string) . "<br/><br/>";

echo "But using htmlentities() was meant to give a better result:<br/><br/>";
echo $output = htmlentities($input_string);

echo "<br/><br/>Though from running this code, it turns out that htmlspecialchars() and htmlentities() work very well.<br> It could be a PHP update."
?>