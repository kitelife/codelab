/**
 * Created with JetBrains PhpStorm.
 * User: xiayf
 * Date: 5/1/13
 * Time: 1:30 AM
 * 《Learning jQuery》读书笔记
 */

// jQuery version
$('a#foo').click(function (e) {
    $(this).css('color', 'red');
    e.preventDefault();
});

// pure javascript version
var foo = document.getElementById('foo');
foo.addEventListener('click', function (e) {
    this.style.color = 'red';
    e.preventDefault();
});

// for Internet Explorer 8 and earlier
var foo = document.getElementById('foo');
foo.attachEvent('onclick', function (e) {
    // Either:
    foo.style.color = 'red';

    // Or:
    ((e.target) ? e.target : e.srcElement).style.color = 'red';

    e.returnValue = false;
});

// Writing a Wrapper Function
function addEventListener(element, event, handler) {
    if (element.addEventListener) {
        element.addEventListener(event, handler);
    } else if (element.attachEvent) {
        element.attachEvent('on' + event, function (e) {
            e.preventDefault = function () {
                e.returnValue = false;
            };
            handler.call(element, e);
        });
    }
}

//We can then call it using the following code (in any browser):
var foo = document.getElementById('foo');
addEventListener(foo, 'click', function (e) {
    this.style.color = 'red';
    e.preventDefault();
});

//###################################################
$('.bar').click(callback);
$(document).on('click', '.bar', callback);

// pure javascript version
/* document.getElementsByClassName returns a NodeList, not an array.
 One main difference between the two is that NodeLists update live,
 meaning that changes to the DOM also change the NodeList
 */
var bars = document.getElementsByClassName('bar');
for (var i = 0; i < bars.length; i++) {
    addEventListener(bars[i], 'click', callback);
}

var bars = document.getElementsByClassName('bar');
for (var i = 0, len = bars.length; i < len; i++) {
    addEventListener(bars[i], 'click', callback);
}

var paragraphs = document.getElementsByTagName('p');
paragraphs = Array.prototype.slice.call(paragraphs);
for (var i = 0; i < paragraphs.length; i++) {
    document.body.appendChild(paragraphs[i].clone(true));
}

//####################################################
document.addEventListener('click', function (e) {
    var element = e.srcElement;
    if (element.tagName === 'A') {
        var url = getAnchorURL(element);
        if (isEvil(url)) {
            e.preventDefault();
            // Inform user that they clicked an "evil" link
        }
    }
});

$(document).on('click', 'a', function () {
    var element = e.srcElement,
        url = getAnchorURL(element);
    if (isEvil(url)) {
        e.preventDefault();
        // Inform user that they clicked an "evil" click
    }
});

// for IE
var elements = document.getElementsByTagName('a');
for (var i = 0; i < element.length; i++) {
    (function (element) {
        element.attachEvent('onclick', function (e) {
            var url = getAnchorURL(element);
            if (isEvil(url)) {
                e.returnValue = false;
                e.cancelBubble = true;

                // Inform user that they clicked an "evil" link
            }
        });
    })(elements[i]);
}

function addEventListener(element, event, handler) {
    if (element.addEventListener) {
        element.addEventListener(event, handler);
    } else if (element.attachEvent) {
        element.attachEvent('on' + event, function (e) {
            e.preventDefault = function () {
                e.returnValue = false;
            };
            e.stopPropagation = function () {
                e.cancelBubble = true;
            };

            handler.call(element, e);
        })
    }
}

/*
 * To trigger an event in jQuery, we can simply use the .trigger method on the element, which will simulate the event
 * being trigger. It doesn't, however, actually trigger a JavaScript event - it just cycles through all events set by .on
 * (or any of the aliases, such as .click) and calls them. This means that it will only trigger event handlers set by jQuery
 * , and any event handlers set using addEventListener will be ignored. There is no way to trigger events set using JavaScript
 * using only jQuery.
 * */
// A wrapper function to trigger events
// wouldn't really recommend using it, it is just to show you how you can use a single function to fire events in all browsers
// The last statement is to demonstrate how this function can work for older browsers that still use DOM2.
function triggerEvent(element, event) {
    if (element.dispatchEvent) {
        var evt = document.createEvent('UIEvents');
        evt.initUIEvent(event, true, true, window, 1);
        element.dispatchEvent(evt);
    } else if (element.fireEvent) {
        // Internet Explorer support
        var evt = document.createEventObject();
        evt.button = 1;
        element.fireEvent('on' + event, evt);
    } else if (element['on' + event]) {
        element['on' + event].call();
    }
}

// To remove an event in jQuery, we can just use the .off method on the element
// The difference between the two calls to .off is that the first removes only the handler specified as the second argument,
// while the second removes all click handlers.
// Calling .off with no arguments would remove all event handlers of every type from that element(at least, ones set with jQuery).
function clickHandler() {
}
$('#foo').click(clickHandler);

// Either
$('#foo').off('click', clickHandler);

// Or:
$('#foo').off('click');


//#######################################

var listeners = [];
function addEventListener(element, event, handler) {
    if (element.addEventListener) {
        element.addEventListener(event, handler);
    } else if (element.attachEvent) {
        var newHandler = function (e) {
            e.preventDefault = function () {
                e.returnValue = false;
            };
            e.stopPropagation = function () {
                e.cancelBubble = true;
            };

            handler.call(element, e);
        };
        element.attachEvent('on' + event, newHandler);
        listeners.push([handler, newHandler]);
    }
}

function removeEventListener(element, event, handler) {
    if (element.removeEventListener) {
        element.removeEventListener(event, handler);
    } else if (element.detachEvent) {
        event = 'on' + event;
        for (var i = 0; i < listeners.length; i++) {
            if (listeners[i][0] === handler) {
                element.detachEvent(event, listeners[i][1]);
                break;
            }
        }
    }
}

/*
 * jQuery's .one method adds an event listener that will only be called once; once we call the event listener the first time,
 * it will be removed and thus will not be called again.
 * */


/*
 * Begin the names of your constructors with a capital letter; this will help you remember whether it is a function or a
 * constructor.
 * */

function Greeting(item) {
    this.item = item;
    console.log('New greeting created.');

    // Do something else here

    this.setItem = function (item) {
        this.item = item;
    };

    this.log = function () {
        console.log('Hello ' + this.item + '!');
    };
}

//################################################

function Add(number) {
    if (typeof number !== 'number') {
        number = 0;
    }

    this.add = function (num) {
        number += num;
        return this;
    };

    this.log = function () {
        console.log(number);
    };
}

new Add(10).add(5).add(1.5).log();


/*
 * The Document Object Model(DOM for short) is the API provided by the browser to enable you to view and interact with objects
 * (such as elements) in HTML and XML documents.
 *
 * The functions that make working with the DOM provided by jQuery can be rather hefty (especially in older browsers), and
 * it is often a lot faster to just use pure JavaScript.
 * */


document.getElementById('foo');
document.getElementsByClassName('bar');
document.getElementsByTagName('p');

/*
 * 'document.getElementById' gets the elements with ID foo. As there can be only be one element associated with each ID,
 * there is no need to return a NodeList here, and it will return either the element or null.
 *
 * 'document.getElementByClassName' gets all elements with "bar" as one of their classes. It will return the elements as
 * a NodeList, which is similar to an array.
 *
 * 'document.getElementByTagName' gets all paragraph elements and returns them as a NodeList.
 *
 * A NodeList is an object that acts like an array, but isn't. This means that you can access the elements using elements[i],
 * but you cannot directly use array methods like .splice and .forEach. However, you can use them with the Array prototype:
 * */

var elements = document.getElementsByClassName('bar');
Array.prototype.slice.call(elements, 2, 5);

/*
 * The .slice call will return an array of elements, not a NodeList.
 * */

// Selecting Elements with a CSS Selector
// It is possible to select elements using CSS selectors via .querySelector and .querySelectorAll:

document.querySelector('#foo');
document.querySelectorAll('.bar');
document.querySelectorAll('.bar span, #foo');
document.querySelectorAll('a[href*="danger"]');


// Sometimes you may want to select the children of an element. With jQuery:
$('#foo').children('.bar');

/* It is also fairly easy in JavaScript, as it is possible to use the .getElement... and .querySelector functions on
 * elements, as well as the document:
 */
document.getElementById('foo').getElementsByClassName('bar');
/*
 * Make sure that you don't attempt to run any of them on a NodeList, though --- it won't work. Instead, you must loop
 * through the elements. These functions only works on elements:
 * */
// Does not work:
document.getElementsByTagName('p').getElementsByClassName('test');

// This works:
var elements = document.getElementsByTagName('p'),
    allElements = [];

Array.prototype.forEach.call(elements, function (element) {
    children = element.getElementsByClassName('test');
    allElements = allElements.concat(Array.prototype.slice.call(children));
});

// This also works:
document.querySelectorAll('p .test');


// Selecting the Next Element
//jQuery
$('#foo').next('.bar');

// pure javascript
var element = document.getElementById('foo');
element = element.nextElementSibling;
while (element && element.className.indexOf('bar') === -1) {
    element = element.nextElementSibling;
}

/*
 * To find the previous element, you can use similar code, but with .previousElementSibling. To find a parent element
 * (.parent using jQuery), we can use .parentElement.
 * */

/*
 * To return all of an element's sibling (like jQuery's .siblings), you have to find the children of the parent element
 * (.parentNode.childNodes) and then loop through, removing all nodes that aren't elements, and removing the original element
 * itself:
 * */
var element = document.getElementById('foo');
var elements = element.parentNode.childNodes;

for (var siblings = [], i = 0; i < elements.length; i++) {
    if (elements[i].nodeType === 1 && elements[i] !== element) {
        siblings.push(elements[i]);
    }
}

console.log(siblings);

/*
 * There are two ways to create elements in JavaScript. One of them is to modify the .innerHTML of the element, but this
 * should usually be avoided as it converts the element(in this case, the body) into HTML, ands the new HTML, and parses
 * it back again. This means that any event listeners and formatting added on the fly will be lost.
 * The other way --- the correct way, in this context --- is to create the element using document.createElement, and then
 * append it using .appendChild:
 * */
// The wrong way, using innerHTML:
document.body.innerHTML += '<strong class="test">text</strong>';

// The correct way:
var newElement = document.createElement('strong');
newElement.setAttribute('class', 'test');
newElement.innerHTML = 'text';
document.body.appendChild(newElement);


//#################################################################
var TEXT_NODE = 3,
    ELEMENT_NODE = 1;

function replace(element, find, replacement) {
    var child, i, value,
        child = element.childNodes;

    for (i = 0; i < children.length; i++) {
        child = children[i];
        if (child.nodeType === TEXT_NODE) {
            child.nodeValue = value.replace(find, replacement);
        } else if (child.nodeType === ELEMENT_NODE) {
            replace(child, find, replacement);
        }
    }
}

var element = document.getElementById('foo');
replace(element, /swear/g, '*****');


// Cycling Through Elements
/*
 * Cycling through elements can be useful for, say, adding an event listener to each of them individually or changing
 * an attribute. In jQuery, cycling through a list of elements is easy:
 * */
$('.bar').each(function () {
    $(this).css('color', 'red');
});

// Pure JavaScript
var elements = document.getElementsByClassName('bar');
for (var i = 0; i < elements.length; i++) {
    elements[i].style.color = 'red';
}

/*
 * If you want to refer to the element as this, you can use an anonymous function with .call to set the scope:
 * */
var elements = document.getElementsByClassName('bar');
for (var i = 0; i < elements.length; i++) {
    (function () {
        this.style.color = 'red';
    }).call(elements[i]);
}

// Moving and Copying Elements
// In jQuery, we can use the following methods to move and copy elements:
$('#foo').insertBefore($('#bar'));  // moves #foo to directly before #bar
$('#foo').clone().insertAfter($('#bar'));   // copies #foo to after #bar

// To move an element in pure JavaScript, we can use the .insertBefore method:
var foo = document.getElementById('foo');
var bar = document.getElementById('bar');
bar.parentNode.insertBefore(foo, bar);
/*
 * .insertBefore uses a slightly strange syntax. You have to call it on the parent node, and send the element to insert
 * (elementToInsert) and the element to insert it before (insertBeforeThis) as arguments (in that order):
 * element.parentNode.insertBefore(elementToInsert, insertBeforeThis);
 * */

/*
 * To copy the element, we can simply call the .cloneNode method before calling insertBefore:
 * */
var foo = document.getElementById('foo').cloneNode(true);
var bar = document.getElementById('bar');
bar.parentNode.insertBefore(foo, bar);
/*
 * The argument being passed to .cloneNode should almost always be true. It tells JavaScript that you want to clone the
 * entire tree (the children of the element), as well as the element itself. Setting this to false or omitting the argument
 * entirely would just copy the children without cloning them, so making any changes to the children of the new element would
 * change the children of the old element (and vice versa).
 * */

/*
 * Sometimes it isn't worth loading the entire jQuery library to send a few requests and nothing else, or it doesn't provide 
 * enough control. It's also useful to know how jQuery does it, as it can help you when you're trying to debug your code.
 * */

// To send an AJAX request in jQuery
$.get('/ajax/?foo=bar', function (data) {
    console.log(data);  // The response
});

// Sending an AJAX request in JavaScript:
if (window.XMLHttpRequest) {
    var req = new XMLHttpRequest();
} else {
    // Internet Explorer
    var req = new ActiveXObject('Microsoft.XMLHTTP');
}
var url = '/ajax/?foo=bar';

req.open('GET', url, true);

req.onreadystatechange = function () {
    if (req.readyState === 4 && req.status === 200) {
        console.log(req.responseText);
    } else if (req.readyState === 4) {
        throw new Error('XHR Request failed: ' + req.status);
    }
};

req.send();
/*
 * The third argument of req.open should always be set to true, as it tells the browser
 * that you want to make the request asynchronous (runs in the background and
 * then calls the callback, as opposed to blocking the page until the request returns).
 * If set to false, it tells the browser that you want a synchronous request. This used
 * to cause a memory leak in Firefox, so Mozilla disabled it; attempting to send a
 * request synchronously now just throws an error. It was also bad practice to use it
 * when it did work.
 * */

// Sending POST Requests in JavaScript
if (window.XMLHttpRequest) {
    var req = new XMLHttpRequest();
} else {
    // Internet Explorer
    var req = new ActiveXObject('Microsoft.XMLHTTP');
}
var url = '/ajax/';
var data = 'foo=bar';

req.open('POST', url, true);
req.setRequestHeader('Content-type', 'application/x-www-form-urlencode');
req.onreadystatechange = function () {
    if (req.readyState === 4 && req.status === 200) {
        console.log(req.responseText);
    } else if (req.readyState === 4) {
        throw new Error('XHR Request failed: ' + req.status);
    }
};

req.send(data);

// A Wrapper Function
function request(method, url, data, callback) {
    if (window.XMLHttpRequest) {
        var req = new XMLHttpRequest();
    } else {
        // Internet Explorer
        var req = new ActiveXObject('Microsoft.XMLHTTP');
    }

    if (method === 'GET' && typeof data === 'string') {
        url += '?' + data;
    }
    req.open(method, url, true);
    if (method === 'POST' && typeof data === 'string') {
        req.setRequestHeader('Content-type', 'application/x-www-form-urlencode');
    }

    req.onreadystatechange = function () {
        if (req.readyState === 4 && req.status === 200) {
            var contentType = req.getResponseHeader('Content-type');
            if (contentType === 'application/json') {
                callback(JSON.parse(req.responseText));
            } else {
                callback(req.responseText);
            }
        } else if (req.readyState === 4) {
            throw new Error('XHR Request failed: ' + req.status);
        }
    };
    req.send((typeof data === 'string' && method === 'POST') ? data : null);
    return req;
}

function get(url, data, callback) {
    return request('GET', url, data, callback);
}

function post(url, data, callback) {
    return request('POST', url, data, callback);
}

//######################################
// JavaScript Conventions
//######################################

/*
* JavaScript has literal notations available for stuff like creating new objects and arrays,
* which allow you to shorten your code and make it clearer. It is better to use literals
* than the constructor functions, such as new Object() and new Array()
* */

/*
*  If you use the literal syntax, JavaScript knows exactly what you mean and gives you an object.
*  If you use the constructor function, however, then JavaScript has to check the current
*  scope, then cycle up through the parent scopes until it finds the Object constructor.
*  The first uses fewer resources and is slightly quicker.
* */

// Constructors and literals
//
// Constructors                         Literals
// var obj = new Object();              var obj = {};
// var ary = new Array();               var ary = [];
// var re = new RegExp('[a-z]+', 'g');  var re = /[a-z]+/g;
// var str = new String();              var str = '';
// var num = new Number();              var num = 0;
// var bool = new Boolean();            var bool = false;

// Optimizations
/*
* When finding an element using jQuery, you'd be wise to cache it instead of calling the jQuery function multiple times:
* */
$('#foo').click(function () {
    $.myFunc($('#foo'), function () {
       $('#foo').show();
    });
    $('#foo').hide();
});

// Better
var foo = $('#foo');
foo.click(function () {
    $.myFunc(foo, function () {
       foo.show();
    });
    foo.hide();
});

/* Function declarations and function expressions perform in different ways and can be used to complete different tasks.
 * Much like variables, function declarations are hoisted (placed the beginning of the scope) and so can be called before
 * they're actually defined. This doesn't happen with anonymous or named function expressions.
*/

/*
* A self-invoking function is an anonymous function that is defined, and then run straightaway. It is mainly useful for
* resolving scoping issues.
* */
(function () {
    // Do something
})();

/*
* Self-invoking functions can also have the parentheses to call the function inside the wrapper parentheses, but it is more
* common to find them outside:
* */
(function () {
    // Do something
}());

/*
* Self-defining functions use a similar concept, and are good for resolving browser compatibility issues.
* */
var matchesSelector = (function () {
   if (HTMLElement.prototype.matchesSelector) {
       return function (element, selector) {
           return element.matchesSelector(selector);
       };
   } else if (HTMLElement.prototype.webkitMatchesSelector) {
       return function (element, selector) {
           return element.webkitMatchesSelector(selector);
       };
   } else if (HTMLElement.prototype.mozMatchesSelector) {
       return function (element, selector) {
           return element.mozMatchesSelector(selector);
       };
   }
   // Load library here
    return function (element, selector) {
        // call library here
    };
})();

/*
* The action of DRYing your code (where DRY is Don't Repeat Yourself) moves repeating code into functions and assigns
* identical strings to variables. It leads to easier-to-read and easier-to-maintain code, and also reduces the footprint
* of the code, making it use less bandwidth.
* */

// Bad action
$('#foo').css('top', '-=10px');
$('#foo').css('left', '+=10px');
$('#bar').css('top', '-=10px');
$('#bar').css('left', '+=10px');
$('#hello').css('top', '-=10px');
$('#hello').css('left', '+=10px');
$('#world').css('top', '-=10px');
$('#world').css('left', '+=10px');

// Also bad
var dist = 10;
$('#foo').css('top', '-=' + dist + 'px');
$('#foo').css('left', '+=' + dist + 'px');
$('#bar').css('top', '-=' + dist + 'px');
$('#bar').css('left', '+=' + dist + 'px');
$('#hello').css('top', '-=' + dist + 'px');
$('#hello').css('left', '+=' + dist + 'px');
$('#world').css('top', '-=' + dist + 'px');

// Better
['#foo', '#bar', '#hello', '#world'].forEach(function(el) {
    $(el).css('top', '-=10px')
        .css('left', '+=10px');
});

/*
* The with statement was designed to offer a shorthand way to access properties of an object. Unfortunately, it doesn't
* always behave quite as expected and can be confusing, so you should avoid it.
*
* When you attempt to access a variable within a with statement, the browser first checks whether the object has that property,
* and if not, it accesses the variable normally.
*
* Consider the following code:
* */
with (obj) {
    a = b;
}
// It could be doing any one of the following:
a = b;
a = obj.b;
obj.a = b;
obj.a = obj.b;

// Without going back and looking at the object, we have no idea what is happening. It is also slower than accessing the object
// or variable directly.

// The Singleton Pattern

// The Factory Pattern
/*
* The Factory pattern is a creational pattern that helps create objects. It creates a generic interface for creating objects
* without using a constructor, where we can specify the type of the factory object to be created.
* */
function Ford(options) {
    this.color = options.color || 'blue';
    this.year = options.year || new Date().getFullYear();
}

function Mini(options) {
    this.color = options.color || 'red';
    this.model = options.model || 'Cooper';
}

function CarFactory(){}
CarFactory.prototype.carType = Ford;    // Default is ford
CarFactory.prototype.createCar = function (options) {
    if(options.carType === 'mini') {
        this.carType = Mini;
    } else if (options.carType === 'ford') {
        this.carType = Ford;
    }

    return new this.carType(options);
};

var factory = new CarFactory();
var mini = factory.createCar({
    carType: 'mini',
    model: 'One'
});

/*
* Another approach would be to have an object telling the .createCar method where all the cars are instead of having an
* if-else statement. This makes it easier to add other cars, and it also means that cars can be added on the fly.
* */
function Ford(options) {
    this.color = options.color || 'blue';
    this.year = options.year || new Date().getFullYear();
}

function Mini(options) {
    this.color = options.color || 'red';
    this.model = options.model || 'Cooper';
}

function CarFactory() {}
CarFactory.prototype.carType = Ford;    // Default is ford
CarFactory.prototype.carTypes = {
    ford: Ford,
    mini: Mini
};
CarFactory.prototype.createCar = function (options) {
    if(options.carType && this.carTypes[options.carType]) {
        this.carType = this.carTypes[options.carType];
    }

    return new this.carType(options);
}

// The Iterator Pattern

// The Facade Pattern
/*
* Basically, a facade function is a function that calls a number of other functions in order to make a process simpler
* for the user.
* */


/*
* As typeof [] returns "object", we cannot use it to detect an array. Instead, we can use the instanceof operator or the
* Array.isArray function:
* */
console.log([] instanceof Array);   // true
console.log(Array.isArray([])); // true
/*
* The instanceof operator isn't too reliable, as it can be tricked into returning the wrong answer. The best way of
* detecting an array is definitely to use the Array.isArray function. However, it is relatively new, and thus isn't
* supported in Internet Explorer 7 and lower. There are two ways around this. The first is to use jQuery's jQuery.isArray
* function:
* */
console.log($.isArray([])); //true
console.log($.isArray({})); //false
/*
* The second workaround is to create the Array.isArray function if it doesn't exist.
* */
if(!Array.isArray) {
    Array.isArray = function (vArg) {
        return Object.prototype.toString.call(vArg) === "[object Array]";
    };
}

/*
* There are two functions built into JavaScript that allow you to implement a delay into your code. The first, setTimeout,
* calls the given function after a specified time interval (specified in milliseconds, a thousandth of a second).
* */
setTimeout(function () {
    console.log('Hello world!');
}, 1000);
/*
* As JavaScript is an asynchronous language, this would not stop the code below from running.
* */
/*
* The second function that allows you to work with delays is setInterval, which calls the given function every x milliseconds,
* instead of just once like setTimeout does.
* */
setInterval(function () {
    console.log('Hello world!');
}, 2000);

/*
* When you call either setTimeout or setInterval, it returns a number that can then be passed to clearTimeout or clearInterval
* to stop the timeout or interval from running:
* */
var id = setInterval(function () {
    console.log('Hello world!');
}, 500);

setTimeout(function () {
    clearInterval(id);
}, 5050);