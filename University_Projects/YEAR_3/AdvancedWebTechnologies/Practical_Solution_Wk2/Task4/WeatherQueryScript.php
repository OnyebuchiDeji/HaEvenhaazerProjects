<!-- In this query script, the info is not displayed but rather stored inthe dataBase, `CityAndWeather` -->
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
            // echo "Request Response: <br>";
            // echo "$response<br><br>";
    
            $apiResult = json_decode($response, true);
    
            //  PHP_EOL --> PHP EndofLine
            // echo "Current temperature in $location is {$api_result['current']['temperature']} Degree Celcius<br><br>", PHP_EOL;
            echo "Displaying Weather information for <b>$cityQuery</b>: <br>";
    
            $currentWeatherData = $apiResult['current'];
    
            $city = ucwords($cityQuery);
            $time = $currentWeatherData['observation_time'];
            $temperature = $currentWeatherData['temperature'] . " degree(s) celcius";
           
            echo "City: $city<br>";
            echo "Time: $time<br>";
            echo "Temp: $temperature<br>";
            $serverName = "katara.scam.keele.ac.uk";
            $userName = "x7e30";
            $password = "x7e30x7e30";
            $dbName = "x7e30";
    
            $conn = mysqli_connect($serverName, $userName, $password, $dbName);
    
            //  Validate Connection
            if (!$conn){
                die("Error: Could not connect to database of user ". $userName . " " . mysqli_connect_error());
            }
            echo "<h4>Successfully Connected to Database <b>$dbName {Server: $serverName | User: $userName}</b><br><br></h4>";
    
            // The below didn't work
            //  one can't just add the variables to the sql command statement
            /**
             * 
             *  $insertQuery_v1 = "insert into `CityAndWeather` (`City`, `Time`, `Temperature`)
             *          values  (`$city`, `$time`, `$temperature`);
             *          ";
             *  //  Returns 1 if successful
             *  $insertResult = $conn->query($insertQuery);
             *  echo "InsertQueryResult: $insertResult<br>";
            *   
             *  if ($insertResult == 1){
             *      echo "<h3><b>Successfully Saved Information for $city : {Time: $time, Temperature: $temperature} into Database<br><br>";
             *  }
            */
            //  So do it this way
            $insertCommand = "insert into `CityAndWeather` (`City`, `Time`, `Temperature`)
                        values  (?, ?, ?);
                        ";
            if ($stmt = mysqli_prepare($conn, $insertCommand)){
                //  'sss' because of three strings being added
                mysqli_stmt_bind_param($stmt, "sss", $city, $time, $temperature);

                //  Execute Query
                mysqli_stmt_execute($stmt);
                mysqli_stmt_close($stmt);
                echo "<h4><b>Successfully Saved Information for $city : {Time: $time, Temperature: $temperature} into Database</h4><br><br>";
            }
            else{
                echo "City information could not be saved. MySQL Error: " . mysqli_error($conn) . "<br><br>";
            }


            echo "View The Cities and  Information <a href='WeatherInfoDisplay.php'>Here</a>";
            $conn->close();
        }

    ?>  
</body>
</html>