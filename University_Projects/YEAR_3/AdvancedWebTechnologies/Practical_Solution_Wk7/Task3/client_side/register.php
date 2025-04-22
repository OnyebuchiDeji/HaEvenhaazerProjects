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

        Enter Some Injection Code (This one is INSERTed last):<br />
        <textarea type="text" name="injection" maxlength="400"
            placeholder="Try anything... I dear you, but it won't work"></textarea>
        <br />

        <input type="submit" value="Register" />
  </form>

 </body>
</html>
