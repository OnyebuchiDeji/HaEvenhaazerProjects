<!-- 
    Modified to Display Captcha Form randomly
    by getting name from database and based on the choice,
    that name and the user's try at writting what the CAPTCHA shows
    are sent along with the other form data.

    Then `createreg` does the other processing.
 -->


<html>
 <head>
  <title>Register</title>
 </head>

 
 <body>
  <h2>Register</h2>

  Please enter your username and password below to register:

  <form action="../server_side/createreg.php" method="POST">
        Enter Student Id:<br>
        <input type="text" name="studentid" maxlength="5"/>
        <br />

        Enter Username:<br />
        <input type="text" name="username" maxlength="30"/>
        <br />

        Enter Password:<br />
        <input type="password" name="password" maxlength="100"/>
        <br />

        Enter Profile Remark:<br />
        <textarea type="text" name="profileremark" maxlength="400"
            placeholder="Give a Short Description of Yourself"></textarea>
        <br /><br/>

        Consider this Captcha:<br />
        <?php
            include "../server_side/connection.php";

            #   Use $conn to connect to the Captcha Table
            #   and obtain an array of these captcha images.
            $query = "SELECT captcha_image_filename from FormCaptchaDB_P8";
            $res = $conn->query($query);
            $arr = array();
            if ($res->num_rows >0)
            {
                while ($row = $res->fetch_assoc()){
                    $arr[] = $row['captcha_image_filename'];
                }
            }else{ echo "Couldn't Load Captcha! Table Empty.<br>";}

            // $conn->close();
            
            #   this rand generates random values between
            #   v1 and v2, with v2 included. So index incase of v2
            #   given count gives size, should be - 1
            $captcha_choice = $arr[rand(0, count($arr) - 1)];
            // echo "Choice: " . $captcha_choice . "<br/>";
            
            echo "<br/>";
            echo "<input type='hidden' name='captcha_filename' value='$captcha_choice'><br>";

            echo "<img src='../CaptchaImages/" . "$captcha_choice" . "'/><br/>";
        ?>
        
        Enter the Captcha's Text:<br/>
        <input type="text" name="captcha_input" maxlength="50"/>
        <br/><br/>

        <input type="submit" value="Register" />
  </form>

 </body>
</html>
