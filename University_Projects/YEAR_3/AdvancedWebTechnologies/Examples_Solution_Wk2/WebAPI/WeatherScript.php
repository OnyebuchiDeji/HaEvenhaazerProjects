<html>
<body>
    <h1>Weather API Control CSC-30025</h1>
    <?php
        $location = 'Newcastle-Under-Lyme';

        $queryString = http_build_query([
            'access_key' => '4f5e169d993a927e8e6e3b6805615be2',
            'query' => $location,
        ]);

        $request_url = sprintf('%s?%s', 'http://api.weatherstack.com/current', $queryString);
        echo "Request URL: $request_url<br><br>";

        //  Usin `curl` to get the data from the API web service's endpoint
        $json = curl_init($request_url);
        curl_setopt($json, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($json);
        echo "Request Response: <br>";
        echo "$response<br><br>";

        $api_result = json_decode($response, true);

        //  PHP_EOL --> PHP EndofLine
        echo "Current temperature in $location is {$api_result['current']['temperature']} Degree Celcius<br><br>", PHP_EOL;
    ?>
</body>
</html>