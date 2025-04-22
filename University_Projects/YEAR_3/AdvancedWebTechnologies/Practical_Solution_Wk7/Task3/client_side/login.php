<html>
 <head>
  <title>Login</title>
 </head>
 <body>
  <h2>Login</h2>

  Please enter your username and password below. Also, try an Injection in any field.
  PS: the username will be used with WHERE in the stmnt. All will be used alongside SELECT.

  <form action="../server_side/authenticate.php" method="POST">
   Enter Username:<br />
   <input type="text" name="username" />
   <br />
   Enter Password:<br />
   <input type="password" name="password" />
   <br />
   <input type="submit" value="Login" />
    <br />
    Enter Some Injection Code:<br />
    <textarea type="text" name="injection" maxlength="400"
        placeholder="Try anything... I dear you, but it won't work"></textarea>
    <br />

  </form>

  <p>
    Or register <a href="register.php">here</a>
  </p>

 </body>
</html>
