/**
 * This is the JS that runs in the confirmation page loaded by the link clicked by the
 * recepient of the email, to show that login was successful; it redirects to the home page directly.
 */


function redirect(){
    window.location.href = "/home";
}

function sleep(milliseconds){

    var start = new Date().getTime();
    // console.log(start);
    
    while ((new Date().getTime() - start) < milliseconds){
        // console.log(new Date().getTime() - start);
        continue;
    }
}

g_count = 5;

function main(){
    var msg = document.getElementById("message");
    msg.innerText = "You will be redirected in 5 seconds";

    // sleep(5000);
    sleep(1000);


    redirect();

    // var id = setInterval((g_count)=>{
    //     g_count -= 1;
    //     console.log(g_count);
    // }, 1000, g_count);
}

main();


function test2(){
    // while (count > 0){
    //     var id = setTimeout(function(count){
    //         msg.innerText = "Will redirect to Home Page in " + count + "...";
    //     }, 1000, count);
    //     count -= 1;

    //     setTimeout(function(){
    //         clearInterval(id);
    //     }, 2000)
    // }

}


function test1(){
        /*
        The below didn't work.
        setTimeout works asynchronously...
        meaning it is not created more than once.
        So the while loop does nothing but decrement the count variable
        setTimeout just waits for the specified second, and then runs the function
        and since it takes the argument, it just console.logs everything without
        waiting a second for each before printing.

        Solution: Use setTimeout, then clear the timeout every next loop
    while (count > 0){
        // msg.innerText = "Will redirect to Home Page in " + count + "...";
        setTimeout(function(count){
            // console.log("Pree");
            console.log(count);
        }, 1000, count);   //  1000 in milliseconds.
        count -= 1;
    }
    */
}