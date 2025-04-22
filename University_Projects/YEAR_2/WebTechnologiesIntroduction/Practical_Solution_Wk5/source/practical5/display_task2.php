<?php
    $id = "CSC-20021";
    $name = "Web Technologies";
    $year = "2";
?>

<!DOCTYPE html><html>
    <head>
        <title>Replacing ID and NAME with the values of $id and $name vairiables</title>
        <link rel="stlesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">
    </head>

    <body class="container-fluid">
        <br>
        <div>
            <label>Id</label>: <?php echo "$id"; ?>
        </div>
        <div>
            <label>Name</label>: <?php echo "$name"; ?>
        </div>
        <div>
            <label>Year</label>: <?php echo "$year"; ?>
        </div>
    </body>
</html>