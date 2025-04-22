<html>
<body>
    <h1>Weather API Control CSC-30025</h1>
    <?php
        $cityQuery = "";
        if (empty($_POST['city']) || $_POST['city'] == "" || strlen($_POST['city']) == 0){
            echo "Nothing Entered. Redirecting in 2 seconds...";
            header("refresh:3;URL=WeatherFormScript.php");
        }
        else{
            $cityQuery = trim($_POST['city']);
            echo "Client Entered: <b>$cityQuery</b><br><br>";

            $queryString = http_build_query([
                'access_key' => '4f5e169d993a927e8e6e3b6805615be2',
                'query' => $cityQuery,
            ]);
    
            $requestUrl = sprintf('%s?%s', 'http://api.weatherstack.com/current', $queryString);
            // echo "Request URL: $request_url<br><br>";
    
            //  Usin `curl` to get the data from the API web service's endpoint
            $json = curl_init($requestUrl);
            curl_setopt($json, CURLOPT_RETURNTRANSFER, true);
    
            $response = curl_exec($json);
            echo "Request Response: <br>";
            echo "$response<br><br>";
    
            $apiResult = json_decode($response, true);
    
            //  PHP_EOL --> PHP EndofLine
            // echo "Current temperature in $location is {$api_result['current']['temperature']} Degree Celcius<br><br>", PHP_EOL;
            echo "Displaying Weather information for <b>$cityQuery</b>: <br>";
    
            $currentWeatherData = $apiResult['current'];
            $displayString = "";
            echo "<ul>";
            foreach ($currentWeatherData as $key=>$val){
                $keyCopy = str_replace("_", " ", $key);
                $keyCopy = ucwords($keyCopy);
                if (!is_array($val)){
                    $displayString = "$keyCopy: $val<br>";
                }
                if (strcmp($key, "temperature") == 0){
                    $displayString =  "$keyCopy: $val degree(s) celcius<br>";
                }
                if (strcmp($key, "weather_icons") == 0){
                    continue;
                }
                if (strcmp($key, "weather_descriptions") == 0){
                    $size = count($val);
                    echo "Weather Descriptions: <br><ul>";
                    foreach ($val as $valItem){
                        echo "<li>$valItem</li>";
                    }
                    echo "</ul><br></li>";
                    continue;
                }
    
                echo "<li>$displayString</li>";
            }
            echo "</ul>";
        }
    ?>
</body>
</html>