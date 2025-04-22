<html>
    <head>
        <title>Multimedia Upload Form - Uploading to MySQL DB</title>
    </head>

    <body>
        <!-- The `multipart/form-data` specifies that you want to send a file -->
        <form method="post" action="UploadScript.php" enctype="multipart/form-data">
            <label for="ImageData">Select an Image</label>
            <input type="file" name="ImageData"/><br>
            <label for="ImageName">Enter File Name</label>
            <input type="text" name="ImageName"/>
            <input type="submit"/>
        </form>
    </body>


</html>