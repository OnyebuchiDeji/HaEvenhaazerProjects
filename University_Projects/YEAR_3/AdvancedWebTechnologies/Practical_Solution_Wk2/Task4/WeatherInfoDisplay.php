

<html>
    <head>
        <title>List all database Weather Info</title>
    </head>

    <body>
        <?php
            $serverName = "katara.scam.keele.ac.uk";
            $userName = "x7e30";
            $password = "x7e30x7e30";
            $dbName = "x7e30";
    
            $conn = mysqli_connect($serverName, $userName, $password, $dbName);
        
            $cityInfoQuery = "select * from CityAndWeather";
            $res1 = $conn->query($cityInfoQuery);

            if ($res1->num_rows > 0){
                echo "<ul>";
                while ($record=mysqli_fetch_assoc($res1))
                {
                    $l_city = $record['City'];
                    $l_time = $record['Time'];
                    $l_temp = $record['Temperature'];
                    echo "
                        <li>$l_city</li>
                        <ul>
                        <li>Time: $l_time</li>
                        <li>Temperature: $l_temp</li>
                        </ul></li>
                    ";
                }
                echo "</ul>";
            }
            else{
                echo "<h4><b>No city information has been added as of now.</b></h4><br>";
            }
            echo "<a href='WeatherFormScript.php'>Add City Info</a>";
        ?>
    </body>
</html>