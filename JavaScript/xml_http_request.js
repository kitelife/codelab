function requestObject(){
    if(window.XMLHttpRequest)
        return new XMLHttpRequest();
    else if(window.ActiveXObject)
        return new ActiveXObject("Msxml2.XMLHTTP");
    else
        throw new Error("Could not create HTTP request object.");
}

var request = requestObject();
request.open("GET", "files/data.txt", false);
request.send(null);

request.responseText;
//-> "This is the content of the file data.txt"
request.getResponseHeader("Content-Type");
//-> "text/plain"
request.status;
//-> 200
request.statusText;
//-> "OK"


// 发送异步请求
request.open("GET", "files/data.txt", true);
request.onreadystatechange = function(){
    if(request.readyState == 4)
        print(request.status + " " + request.statusText);
};
request.send(null);

// 基本的请求包装
function simpleHttpRequest(url, success, failure){
    var request = requestObject();
    request.open("GET", url, true);
    request.onreadystatechange = function() {
        if(request.readyState == 4){
            if(request.status == 200 || !failure)
                success(request.responseText);
            else if(failure)
                failure(request.status, request.statusText);
        }
    };
    request.send(null);
}
