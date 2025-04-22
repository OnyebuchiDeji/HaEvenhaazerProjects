<!DOCTYPE HTML><html>
    <head>
        <title></title>
        <meta name="Description" content="">
        <meta name="Keywords" content="">
        <script type="text/javascript">
            function ajaxFunction(choice){
                var httpxml;
                try{
                    //  Firefox, Chrome, Opera 8.0+, Safari
                    httpxml = new XMLHttpRequest();
                }
                catch(e) {
                    //  Internet Explorer
                    try{
                        httpxml = new ActiveXObject("Msxml2.XMLHTTP");
                    }
                    catch(e){
                        try{
                            httpxml = new ActiveXObject("Microsoft.XMLHTTP");
                        }
                        catch (e) {
                            alert ("Your browser does not support AJAX!");
                            return false;
                        }
                    }
                }

                function stateChanged(){
                    /*An Ajax http request has 5 states as your reference documents:
                    0   = UNSENT  open() has not been called yet.
                    1   = OPENED  send() has been called.
                    2   = HEADERS_RECEIVED    send() has been called, and headers and status are available.
                    3   = LOADING Downloading; responseText holds partial data.
                    4   = DONE    The operation is complete. State 4 means that the request had been sent, 
                        the server had finished returning the response and the browser had finished downloading 
                        the response content. So, it is right to say that the AJAX call has completed.*/
                    if (httpxml.readyState==4){ //  Successfull
                        //  alert(httpxml.responseText)
                        //  Get the response from the PHP server
                        // console.log(httpxml.responseText);
                        var myObject = JSON.parse(httpxml.responseText);

                        console.log(document.myForm);
                        /**
                         *  Get the form and remove the old options list for the form for states
                         */
                        // for (j = document.myForm.state.options.length - 1; j >= 0; j--){
                        //     document.myForm.state.remove(j);
                        // }

                        // var state1 = myObject.value.state1;

                        // var option = document.createElement("OPTION");
                        // option.text = "Select State";
                        // option.value = "";
                        // document.myForm.state.options.add(option);
                        // for (i=0; i<myObject.state.length;i++){
                        //     var option = document.createElement("OPTION");
                        //     option.text = myObject.state[i];
                        //     option.value = myObject.state[i];
                        //     document.myForm.state.options.add(option);

                        //     if (option.value == state1){
                        //         var k = i + 1;
                        //         document.myForm.state.options[k].selected = true;
                        //     }
                        // }
                        //  Remove old countries form options list
                        for (j=document.myForm.city.options.length - 1; j>=0; j--){
                            document.myForm.city.remove(j);
                        }
                        var city1 = myObject.value.city1;
                        for (i=0;i<myObject.city.length;i++){
                            var optn = document.createElement("OPTION");
                            optn.text = myObject.city[i];
                            optn.value = myObject.city[i];
                            document.myForm.city.options.add(optn);
                            if(optn.value==city1){
                                document.myForm.city.options[i].selected=true;
                            }
                        }
                        document.getElementById("txtHint").style.background='#00f040';
			            document.getElementById("txtHint").innerHTML='done';
                    }
                }

                var url="ajaxCheck.php";
                var country=myForm.country.value;
                if(choice != 's1'){
                    var state=myForm.state.value;
                    var city=myForm.city.value;
                }else{
                    var state='';
                    var city='';
                }
                url=url+"?country="+country;
                url=url+"&state="+state;
                url=url+"&city="+city;
                url=url+"&id="+Math.random();
                myForm.st.value=state;
                //alert(url);
                //document.getElementById("txtHint2").innerHTML=url;
                httpxml.onreadystatechange=stateChanged;
                httpxml.open("GET",url,true);
                httpxml.send(null);
                document.getElementById("txtHint").innerHTML="Please Wait....";
                document.getElementById("txtHint").style.background='#f1f1f1';
            }
        </script>
    </head>
    <body>
        <div id="txtHint" style="width : 100px; background-color: #cccc33;">Message Area</div>
        <br><br>
        <form name="myForm" action="ajaxMSG.php" method="post">
            <input type="hidden" name="st" value=0/>
            <table width=500>
                <tr>
                    <td>Select Country
                        <select name='country' id='s1' onchange="ajaxFunction('s1')">
                            <option value=''>Select One</option>
                            <?php
                                require "Config.php";
                                $sql="select distinct country from CountriesAJAX";
                                foreach ($g_dbConn->query($sql) as $row) {
                                    echo "<option value=$row[country]>$row[country]</option>";
                                }
                            ?>
                        </select>
                    </td>

                    <!-- <td>
                        <select name='state' onchange="ajaxFunction('s2')">
                          <option value=''>Select One</option></select>
                        </select>
                    </td> -->
                    <td>
                        <select name='city' onchange="ajaxFunction('s3')">
                          <option value=''>Select One</option></select>
                        </select>
                    </td>

                </tr>

                <tr>
                    <td colspan=2><input type=submit value='Submit'></td>
                </tr>
            </table>
        </form>

        <br><br>
        
        <div id="txtHint2"></div>
    </body>
</html>