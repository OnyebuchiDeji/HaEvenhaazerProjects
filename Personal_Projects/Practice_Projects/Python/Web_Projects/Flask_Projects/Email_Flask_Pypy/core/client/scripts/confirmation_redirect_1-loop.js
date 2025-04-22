


function sleep(milliseconds){

    var start = new Date().getTime();
    // console.log(start);
    
    while ((new Date().getTime() - start) < milliseconds){
        // console.log(new Date().getTime() - start);
        continue;
    }
}

function redirect(){
    window.location.href = "/home";
}

async function is_verified_v1()
{
    while (true){

        var {flag} = await fetch("/serve-verify-flag").then(r=>r.json());
        console.log(flag);
        if (flag){
            break;
        }
        sleep(5000);    //  Sleep for 5 seconds.
    }
    redirect();
}

async function is_verified_v2()
{
    var id = setInterval(async(id)=>{
        var {flag} = await fetch("/serve-verify-flag").then(r=>r.json());
        console.log(flag);
        if (flag){
            clearInterval(id);
            redirect();
        }
    }, 5000, id);

}

addEventListener("pageshow", async ()=>{
    await is_verified_v2();
});



