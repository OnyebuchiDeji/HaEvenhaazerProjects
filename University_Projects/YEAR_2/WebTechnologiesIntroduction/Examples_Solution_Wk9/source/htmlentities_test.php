<?php
/**
	This code is part of Lecture 17 - Security in Web Technologies by Dr. Goskel Misirli.
	
	This code was written on Wed-3-April-2024, done from examples on this site: https://phppot.com/php/php-htmlentites/
	
		
	The goal of this code is to show the use of htmlentities() function in validating some input.
	In this example, it removes the double quoted from the input_string below, affecting the html displayed
	Later, another funciton: html_entitiy_decode() converts the output string given by hmtlentities()...
	back to its original form, and displays this.
 */
$input_string = "PHP 'character string conversion' functions <i>htmlentities()</i>";
$output = htmlentities($input_string);
echo "<b>Original Character String before running HTMLENTITIES(string)</b><br/>";
echo $input_string . "<br/><br/>";

echo "<b>After Conversion, after running HTMLENTITIES(string)</b><br/>";
echo $output ."<br/><br/>";

$decoded_output = html_entity_decode($output);
echo "<b>After running HTML_ENTITY_DECODE(output) to decode the previously encoded html entity</b><br/>";
echo $decoded_output;
?>