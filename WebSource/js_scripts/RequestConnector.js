
/**
 *  This uses the Fetch API. It is faster and more efficient.
 */
class RequestConnector
{
    constructor(){
        this.callback = null;
    }

    SendRequest(url="", requestType="", responseType="json", params=Object, callback)
    {
        let requestUrl = url.trim();
        requestType = requestType.toLowerCase();
        responseType = responseType.toLowerCase();

        switch(requestType){
            case "get":
                requestUrl += Object.entries(params).length > 0 ? "?": "";
                let getParams = new URLSearchParams();
                Object.entries(params).forEach(([k, v]) =>{
                    getParams.append(k, v);
                });

                fetch(requestUrl + getParams)
                    .then(responseType=="json" ? response=>response.json() : response=>response.text())
                    .then(content=>{
                        if (responseType=="json" && (content['Error'])){
                            console.log("Error: ", content['Error']);
                        }
                        callback(content);
                    });

                break;
                
            case "post":
                fetch(requestUrl, {
                    method: "POST",
                    headers:{
                        'Content-Type': "application/json",
                    },
                    body: new URLSearchParams(params),
                })
                .then(responseType=="json" ? response=>response.json() : response=>response.text())
                .then(content=>{
                    if (responseType=="json" && (content['Error'])){
                        console.log("Error: ", content['Error']);
                    }
                    callback(content);
                });
                break;
        }
    }


}