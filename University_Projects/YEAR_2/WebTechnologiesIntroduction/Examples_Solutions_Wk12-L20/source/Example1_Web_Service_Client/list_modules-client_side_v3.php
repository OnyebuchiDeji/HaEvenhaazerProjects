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
                height: auto;
            }
        </style>
     </head>

     <body>
        <div id="content" class="col-md-8"></div>

        <script>
            /**
             * 
             */
            $(function()
                {
                    //  This gets the json returned by the server script
                    //  it creates a handle int the form of this anonymous function to
                    //  that manipulates the data obtained
                    $.getJSON("get_modules-server_side_v3.php", function(data)
                    {
                        /**
                         * For each first-level data item:
                         * since the get_modules-server_side_v3 sends the contents of entries3-list_type.json...
                         * the json received has a normal list of associative arrays, not an associative array of associative arrays...
                         * like the list_modules-client_side_v2.php.
                         * 
                         * So I search through each data in the normal list
                         * each item is an associative array.
                         * In this case it is index and value that I am given
                         * So it goes through each 
                         */
                        // $.each(data, function(index, entry)
                        $.each(data, function(index, value)
                        {
                            // console.log(entry);
                            $("#content").append("<h1>" + value.name.toUpperCase() + "'s" + " Data:\t"  + "</h1>");
                            $("#content").append("<p>List Number:" + index  + "</p>");
                            $("#content").append("<p>Age:" + value.age  + "</p>");
                            $("#content").append("<p>Who? " + value.description + "</p>");
                            $("#content").append("<p>Email: " + value.email + "</p>");
                            $("#content").append("<p>Module Type: " + value.moduleType + "</p>");
                            $("#content").append("<p>Year: " + value.year + "</p>");
                        });
                    });
                }
            );
        </script>
     </body>
</html>