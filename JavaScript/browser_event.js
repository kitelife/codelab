/*
下面的函数遍历了一些事件对象属性，并确保每个属性都可以在标准的名称下找到。
增加一个stop方法，用于取消事件的冒泡行为和默认行为。有些浏览器已经提供了
这一功能，在这种情况下，就让它保持原样。
*/

function normalizeEvent(event){
    if(!event.stopPropagation){
        event.stopPropagation = function(){this.cancelBubble = true;};
        event.preventDefault = function(){this.returnValue = false;};
    }
    if(!event.stop)
        event.stop = function(){
            this.stopPropagation();
            this.preventDefault();
        };

    if(event.srcElement && !event.target)
        event.target = event.srcElement;

    if((event.toElement || event.fromElement) && !event.relatedTarget)
        event.relatedTarget = event.toElement || event.fromElement;
    if(event.clientX != undefined && event.pageX == undefined){
        event.pageX = event.clientX + document.body.scrollLeft;
        event.pageY = event.clientY + document.body.scrollTop;
    }
    if(event.type == "keypress")
        event.character = String.fromCharCode(event.charCode || event.keyCode);

    return event;
}

// 有了这个函数，就可以为registerEventHandler和unregisterEventHandler编写更方便的包装：
function addHandler(node, type, handler){
    function wrapHandler(event){
        handler(normalizeEvent(event || window.event));
    }
    registerEventHandler(node, type, wrapHandler);
    return {node: node, type: type, handler: wrapHandler};
}

function removeHandler(object){
    unregisterEventHandler(object.node, object.type, object.handler);
}

