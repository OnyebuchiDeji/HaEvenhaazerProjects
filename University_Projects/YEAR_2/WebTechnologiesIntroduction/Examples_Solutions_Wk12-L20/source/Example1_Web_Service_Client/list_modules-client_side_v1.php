<!DOCTYPE html><html>
    <!-- 
        This is the Web Service CLient -- this gets the data from the server side and presents it.
     -->
     <head>
        <title>The Client Side</title>
        <script src="http://code.jquery.com/jquery-3.7.1.min.js"></script>
        <style>
            #content
            {
                border: 5px solid black;
                width: auto;
                height: 500px;
            }
        </style>
     </head>

     <body>
        <div id="content" class="col-md-8"></div>

        <script>
            /**
             * This version parses json information that contained a single associative array list
             */
            /*
                For each first-level data item:
                index is the key, entry is the value.
                In entries2.json, the key is 'deji'
                "deji" has the value an associative array of different key-value pairs as it's value.
                Note how the value of "deji", which is an associative array, is used to get the actual values represented by the inner keys
                E.g, value.id
                Basically, jQuery forms an associative array object from json associative arrays.
                That's why the keys, index, name,year, are treated like properties of the object (associative array), which itself is the value...
                represented by the key, "deji"
                */
            // $.each(data, function(index, entry)
            $(function()
                {
                    $.getJSON("get_modules-server_side_v1.php", function(data)
                    {
                        // $.each(data, function(index, entry)
                        $.each(data, function(key, value)
                        {
                            // console.log(entry);
                            $("#content").append("<h1>" + String(key) + ": " + String(value)  + "</h1>");
                            // $("content").append("<strong>" + entry.name + "</strong>");
                            // $("content").append("<p>" + entry.description + "</p>");
                            // $("content").append("<p>Co-ordinator: " + entry.email + "</p>");
                            // $("content").append("<p>Modulet Type: " + entry.moduleType + "</p>");
                            // $("content").append("<p>Year: " + entry.year + "</p>");
                        });
                    });
                }
            );
        </script>
     </body>
</html>