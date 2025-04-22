<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Search Live on MySQL Database</title>
        <style type="text/css">
            body{
                font-family: Arial, sans-serif;
            }
            /* Formatting search box */
            .search-box{
                width: 350px;
                position: relative;
                display: inline-block;
                font-size: 14px;
            }
            .search-box input[type="text"]{
                height: 32px;
                padding: 5px 10px;
                border: 1px solid #CCCCCC;
                font-size: 14px;
            }
            .result{
                position: absolute;        
                z-index: 999;
                top: 25%;
                left: 0;
            }
            .search-box input[type="text"], .result{
                width: 100%;
                box-sizing: border-box;
            }
            /* Formatting result items */
            .result p{
                margin: 0;
                padding: 7px 10px;
                border: 1px solid #CCCCCC;
                border-top: none;
                cursor: pointer;
            }
            .result p:hover{
                background: #f2f2f2;
            }
        </style>
        <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
        <script type="text/javascript">
            $(document).ready(function(){
                $(".SearchBox input[type='text']").on("keyup input", function(){
                    //  Get input value on change
                    var inputVal = $(this).val();
                    var resultDropdown = $(this).siblings(".result");
                    if (inputVal.length){
                        //  term is the key of the key-val pair that will be sent
                        $.get("BackendSearch-Students.php", {term: inputVal}).done(function(data){
                            //  Display the returned data in browser
                            console.log(data);
                            resultDropdown.html(data);
                        });
                    }else{
                        resultDropdown.empty();
                    }
                });

                //  Set search input value on click of result item
                $(document).on("click", ".result p", function(){
                    $(this).parents(".SearchBox").find("input[type='text']").val($(this).text());
                    $(this).parent(".result").empty();
                });
            });
        </script>
    </head>
    <body>
        <div class="SearchBox">
            <h1>Search Students Live:</h1>
            <input type="text" autcomplete="off" placeholder="Search country..."/>
            <div class="result"></div>
        </div>
    </body>
</html>