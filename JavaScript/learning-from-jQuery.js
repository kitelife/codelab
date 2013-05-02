/**
 * Created with JetBrains PhpStorm.
 * User: xiayf
 * Date: 5/1/13
 * Time: 1:30 AM
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
} );

// Writing a Wrapper Function
function addEventListener(element, event, handler) {
    if(element.addEventListener) {
        element.addEventListener(event, handler);
    }else if (element.attachEvent) {
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
for(var i = 0, len = bars.length; i < len; i++) {
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
    if(element.tagName === 'A') {
        var url = getAnchorURL(element);
        if(isEvil(url)){
            e.preventDefault();
            // Inform user that they clicked an "evil" link
        }
    }
});

$(document).on('click', 'a' ,function(){
    var element = e.srcElement,
        url = getAnchorURL(element);
    if (isEvil(url)){
        e.preventDefault();
        // Inform user that they clicked an "evil" click
    }
});

// for IE
var elements = document.getElementsByTagName('a');
for(var i = 0; i < element.length; i++) {
    (function (element) {
        element.attachEvent('onclick', function (e) {
            var url = getAnchorURL(element);
            if(isEvil(url)) {
                e.returnValue = false;
                e.cancelBubble = true;

                // Inform user that they clicked an "evil" link
            }
        });
    })(elements[i]);
}

function addEventListener(element, event, handler) {
    if(element.addEventListener) {
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
    } else if(element['on' + event]) {
        element['on' + event].call();
    }
}

// To remove an event in jQuery, we can just use the .off method on the element
// The difference between the two calls to .off is that the first removes only the handler specified as the second argument,
// while the second removes all click handlers.
// Calling .off with no arguments would remove all event handlers of every type from that element(at least, ones set with jQuery).
function clickHandler(){}
$('#foo').click(clickHandler);

// Either
$('#foo').off('click', clickHandler);

// Or:
$('#foo').off('click');


//#######################################

var listeners = [];
function addEventListener(element, event, handler) {
    if(element.addEventListener) {
        element.addEventListener(event, handler);
    } else if(element.attachEvent) {
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
    if(element.removeEventListener) {
        element.removeEventListener(event, handler);
    } else if(element.detachEvent) {
        event = 'on' + event;
        for(var i = 0; i < listeners.length; i++) {
            if(listeners[i][0] === handler) {
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
    if(typeof number !== 'number') {
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
while(element && element.className.indexOf('bar') === -1){
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

for(var siblings = [], i = 0; i < elements.length; i++) {
    if(elements[i].nodeType === 1 && elements[i] !== element) {
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
    ELEMENT_NODE =1;

function replace(element, find, replacement) {
    var child, i, value,
        child = element.childNodes;

    for(i = 0; i < children.length; i++) {
        child = children[i];
        if(child.nodeType === TEXT_NODE) {
            child.nodeValue = value.replace(find, replacement);
        } else if(child.nodeType === ELEMENT_NODE) {
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
for(var i = 0; i < elements.length; i++) {
    elements[i].style.color = 'red';
}

/*
* If you want to refer to the element as this, you can use an anonymous function with .call to set the scope:
* */
var elements = document.getElementsByClassName('bar');
for(var i = 0; i < elements.length; i++) {
    (function (){
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