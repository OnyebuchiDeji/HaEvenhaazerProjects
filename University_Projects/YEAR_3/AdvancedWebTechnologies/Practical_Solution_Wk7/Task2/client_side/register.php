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
        <br />

        <input type="submit" value="Register" />
  </form>

 </body>
</html>
