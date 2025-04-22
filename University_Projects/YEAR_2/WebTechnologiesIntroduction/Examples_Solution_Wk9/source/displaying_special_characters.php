

<?php
/**
	This code is part of Lecture 17 - Security in Web Technologies by Dr. Goskel Misirli.
	
	This code was written on Wed-3-April-2024, done from examples on this site: https://phppot.com/php/php-htmlentites/
	
	The goal of this code was to show the difference in how htmlspecialchars and htmlentities displays the special characters, ÷ and ×.
	But it turns out that PHP has no problem doing thi, even without these functions.
	
	The htmlentities() function converts a string with special characters to a form that can be interpreted by html.
	For example, unicode characters like ÷×
	But it turns out that PHP has no problem displaying these characters in the right HMTML format though, even without the special functions

 */

$input_string = "The multiplication and division symbols: ÷ ×" . "<br/><br/>";
echo "Not using anything to display the multiplication and division symbols. <br/>";
echo $input_string  . "<br/>";

echo "Using htmlspecialchars() to display the multiplication and division sign gives this: <br/>";
echo $output = htmlspecialchars($input_string) . "<br/><br/>";

echo "But using htmlentities() to display the multiplication and division sign gives this: <br/>";
echo $output = htmlentities($input_string)  . "<br/><br/>";

echo "<b>But it turns out that PHP has no problem displaying these characters in the right HMTML format though, even without the special functions.<br/>
Moreover it turns out that both htmlspecialchars() and htmlentities() functions act almost completely alike for these special characters.<b>";
?>