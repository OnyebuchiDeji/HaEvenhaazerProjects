<?php
    require "Config.php";

    error_reporting(0);
    $country = $_GET['country'];
    $state1 = $_GET['state'];
    $city1 = $_GET['city'];

    /**
     *  ctype_alpha(str) checks whether string, str, contains only alphabets or not.
     *  Below, an error occurs if any of the country names entered have a numeric character
     */

    if ((strlen($country)) > 0 && (!ctype_alpha($country))){
        echo "Data Error: countries do not have numbers in their names.<br>";
        exit;
    }
    /**
     *  This also esnures that the entered state does not have a numeric character
     */
    if ((strlen($state1)) > 0 && ctype_alpha(str_replace(' ', '', $state1)) === false){
        echo "Data Error: states do not have numbers in their names.<br:";
        exit;
    }

    if (strlen($country) > 0){
        $q_country = "select distinct(state) from CountriesAJAX where country = '$country'";
    }else{
        $q_country = "select distinct(state) from CountriesAJAX";
    }

    //  echo $q_country;
    $stmnt = $g_dbConn->prepare($q_country);
    $stmnt->execute();
    $state = $stmnt->fetchAll(PDO::FETCH_COLUMN);

    $q_state = "select distinct(city) from CountriesAJAX where ";
    if (strlen($country) > 0){
        $q_state = $q_state . " country = '$country' ";
    }
    if (strlen($state1) > 0) {
        $q_state = $q_state . " and state='$state1'";
    }
    $stmnt = $g_dbConn->prepare($q_state);
    $stmnt->execute();
    $city = $stmnt->fetchAll(PDO::FETCH_COLUMN);

    $main = array('state'=>$state, 'city'=>$city, 'value'=>array("state1"=>"$state1", "city1"=>"$city1"));
    echo json_encode($main);
?>