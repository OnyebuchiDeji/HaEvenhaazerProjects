<!DOCTYPE HTML><hmtl>
    <head>
        <title>The Server Side EG2 Selection Details</title>
    </head>

    <body>
        Details

        ID:
        <?php
            if (isset($_POST["id"])) 
            {
                echo $_POST["id"];
            }
            else
            {
                echo "Did not receive an ID by POST";
            }
        ?><br>

        Year:
        <?php
            if (isset($_PoST["moduleYear"]))
            {
                echo $_POST["moduleYear"];
            }
            else
            {
                echo "Did not receive Modue Year by POST";
            }
        ?>

    </body>
</hmtl>