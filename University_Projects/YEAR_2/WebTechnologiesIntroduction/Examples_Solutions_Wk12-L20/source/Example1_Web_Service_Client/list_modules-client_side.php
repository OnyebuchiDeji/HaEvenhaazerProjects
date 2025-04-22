<!DOCTYPE html><html>
    <!-- 
        This is the Web Service CLient -- this gets the data from the server side and presents it.
     -->
     <head>
        <title>The Client Side</title>
     </head>

     <body>
        <div id="content" class="col-md-8"></div>

        <script>
            $.getJSON("get_modules-server_side.php", function(data)
            {
                $.each(data, function(index, entry)
                {
                    console.log(entry);
                    $("content").append("<h1>" + entry.data.id + "</h1>");
                    $("content").append("<strong>" + entry.name + "</strong>");
                    $("content").append("<p>" + entry.description + "</p>");
                    $("content").append("<p>Co-ordinator: " + entry.email + "</p>");
                    $("content").append("<p>Modulet Type: " + entry.moduleType + "</p>");
                    $("content").append("<p>Year: " + entry.year + "</p>");
                });
            });
        </script>
     </body>
</html>