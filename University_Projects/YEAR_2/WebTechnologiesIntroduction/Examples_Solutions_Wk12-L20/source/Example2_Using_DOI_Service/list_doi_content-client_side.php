<!DOCTYPE html><html>
    <!-- 
        This is the Web Service CLient -- this gets the data from the server side and presents it.

        It turns out that the file gotten from the "using_doi_service" server script...
        Does not give a JSON file. I was trying to get a JSON file using $.getJSON but this didn't work.
        So I use normal $.get() and process the string to print what I want
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
            function switch_case_test()
            {
                for (var i = 0; i < 10; i++)
                {
                    switch (i)
                    {
                        case 1:
                            console.log("one");
                            break;
                        case 3:
                            console.log("three");
                            break;
                        case 5:
                            console.log("five");
                            break;
                        case 7:
                            console.log("seven");
                            break;
                        case 9:
                            console.log("nine");
                            break;
                        default:
                            continue;
                            console.log("even");
                    }
                }
            }

            // var g_arr = new Array;

            function associative_array()
            {
                var name1 = "book";
                var name2 = "book2";
                var name3 = "book3";
                var arr = new Array();
                arr[name1] = "Edos";
                arr[name2] = "Liam";
                arr[name3] = "Ven";
                // console.log(arr[name1]);

                // $.each(arr, function(val){
                //     console.log(arr[val]);

                // });
    
                // for (const val in arr)
                // {
                //     console.log(arr[val]);
                // }   
            }
            
            $(function()
                {
                    $.get("using_doi_service.php", function(data)
                    {
                        var server_output = ""; 
                        var content_dict = new Array();
                        /**
                         * It is not possible to store this "data" variable in another object...
                         * outside this $.get() global function.
                         * When I tried to access server_output, even after I had done this:  server_output += String(data);
                         * anytime I printed it out to the console it will show *undefined*
                         */
                        server_output += String(data);
                        // console.log(server_output.substring(0, 4));
                        // $("#content").append("<h1>" + server_output + "</h1>");

                        var whole_string = "";
                        var key_word = "";
                        var value_word = "";
                        var key_flag = false;
                        var value_flag = false;
                        var letter = "";

                        for (var i = 0; i < server_output.length; i++)
                        {
                            // whole_string += server_output[i];
                            letter =server_output[i];

                            switch (letter)
                            {
                                case "{":
                                    if (value_flag == false)
                                    {
                                        key_flag = true;
                                    }
                                    else key_flag = false;

                                    continue;

                                case "}":
                                    value_flag = false;
                                    key_flag = true;
                                    if (key_word != "" && key_word != " ")
                                        content_dict[key_word] = value_word;
                                    value_word = "";
                                    key_word = "";
                                    
                                    continue;

                                case ",":
                                    //  This is so that the values which have commas are consifered
                                    //  so that it does not flush the values which have comma-separated content
                                    if (value_flag == false)
                                    {
                                        //  Flush
                                        key_flag = true;
                                        if (key_word != "" && key_word != " ")
                                            content_dict[key_word] = value_word;
                                        key_word = "";
                                        value_word = "";
                                    }
                                    else
                                    {
                                        key_flag = false;
                                    }
                                    continue;

                                case "=":
                                    value_flag = true;
                                    key_flag = false;
                                    // content_dict[key_word] = value_word;
                                    //  Reset
                                    // value_word = "";
                                    continue;

                                
                            }

                            if (key_flag == true)
                            {
                                key_word += letter;
                                // value_word = "";
                            }

                            if (value_flag == true)
                            {
                                value_word += letter;
                                // key_word = "";
                            }
    
                            // if (i >= 40)
                            // { 
                            //     break;
                            // }
                            
                            // console.log(key_word, value_word);

                        }

                        for (const key in content_dict)
                        {
                            // console.log(count);
                            console.log(key + ", " + content_dict[key]);
                            $("#content").append("<b>" + key + ", " + content_dict[key] + "</b><br><br>");
                        }
                    });


                }

            );

        </script>
     </body>
</html>