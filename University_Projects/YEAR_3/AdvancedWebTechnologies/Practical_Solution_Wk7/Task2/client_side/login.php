<html>
 <head>
  <title>Login</title>
 </head>
 <body>
  <h2>Login</h2>

  Please enter your username and password below:

  <form action="../server_side/authenticate.php" method="POST">
   Enter Username:<br />
   <input type="text" name="username" />
   <br />
   Enter Password:<br />
   <input type="password" name="password" />
   <br />
   <input type="submit" value="Login" />
  </form>

  <p>
    Or register <a href="register.php">here</a>
  </p>

 </body>
</html>
