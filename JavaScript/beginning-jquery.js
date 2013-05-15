/*
 《Beginning jQuery》读书笔记
*/

// <script type="text/javascript" src="path/to/your/file.js"></script>

/*
 * for HTML5 doctype(<!DOCTYPE html>)
 * <script src="path/to/your/files.js"></script>
 * is enough.
* */

/*
 * Within a typical HTML file, there are typically two places people use to load
 * their external JS files. The first is within the head, and the second is just
 * before the closing </body> tag. In the past, scripts were always loaded into 
 * the head element, but with performance and page loading speeds more critical 
 * than ever, it's often recommended to place your scripts at the bottom of your 
 * page.
 *
 * The browser renders the page from top to bottom, and when it comes across your 
 * scripts, it pauses rendering the page to load in your JS, the page loads slower 
 * because the rendering is blocked by your loading JavaScript files.
 * */

/*
 * one reason why jQuery is so valuable: everything it offers works just as well 
 * in an older version of Internet Explorer as it does in the latest release of 
 * Google Chrome or Mozilla Firefox.
 * */

/*
 * In DOM, there are three main types of nodes that you need to know: element,
 * text, and attribute nodes.
 * */

/*
 * jQuery uses minifier to compress itself. Minifier performs a number of actions 
 * to get the code down to as small as possible, including:
 * Stripping out all white space
 * Removing all comments
 * Renaming long variable names; for example, var myCar might become var a.
 * */

/*
 * All jQuery does is have a function bound to $. It can detect what you pass into 
 * it, and do certain things. So when you pass in $("body");, it knows to select 
 * the body element. But when you pass in $(function() {});, it detects you passed 
 * in a function, and acts accordingly.
 * */

// 外部CSS
// <link rel="stylesheet" type="text/css" href="style.css" />
$(function() {
    var box = $("#box");
    var para = $("p");
    var i = 0;

    para.text(i);
    function toggleBox(i) {
        box.fadeToggle(500, function() {
            i = i + 1;
            if(i < 10) {
                para.text(i);
                toggleBox(i);
            }
        });
    }

    toggleBox(i);
});

//#############################################################################

var myDiv = $("div");
// 1
myDiv.find("p");
// 2
myDiv.children("p");
// 3
$("div p");

//#############################################################################
$(".first-paragraph").siblings();
// 1
$(".first-paragraph").siblings().add(".first-paragraph");
// 2
$(".first-paragraph").siblings().addSelf();

// nextAll() gets all the siblings that are after the current element.
// prevAll()
// prev(), next()
$(".first-paragraph").nextAll();

//
$("strong").parents.not("html, body");

// parentsUntil gets all elements up to but not including the one your selector 
// matches.
$("strong").parentsUntil("body");

/*
 * Two filters that are very useful are the :even and :odd filters. Combing them 
 * with the filter() method, which takes a filter and returns the ones that pass 
 * , you can easily apply background colors to rows in order to make the table 
 * appeared striped.
 * */
$(function() {
    var rows = $("tr");
    rows.filter(":even").css("background", "red");
    rows.filter(":odd").css("background", "blue");
});

/*
 * you can also pass filter() a function that will evaluate each element in a set 
 * and return only those that match a certain condition.
 * 
 * When you pass filter() a function, it expects this function to return true or 
 * false. filter() runs once for each element, and will keep elements when the 
 * function you pass in evaluates to true. It will get rid of elements that make 
 * the function evaluate to false.
 * Within this function, you have access to the current element through the this 
 * keyword.*/

$(function() {
   var ps = $("p");

   var strongPs = ps.filter(function() {
    return $(this).children("strong").length > 0;
   });

   strongPs.css("background", "red");
});

/*
 * There's one way you could simplify the code. The filter() method still returns 
 * the jQuery object, which means it can be chained.
 * */
$(function() {
    var ps = $("p");

    ps.filter(function() {
        return $(this).children("strong").length > 0;
    }).css("background", "red");
});

/*
 * Here you are using a ps variable, but only referring to it once; get rid of it 
 * so that you're left with the following:
 * */
$(function() {
    $("p").filter(function() {
        return $(this).children("strong").length > 0;
    }).css("background", "red");
});

/*
 * DOM manipulation is often a huge bottleneck in web sites, so you would try to 
 * do it as little as possible.*/

/*
 * jQuery's css() method is very powerful. There are actually three primary ways 
 * that you'll work with it. The first is when determining the value of an element's 
 * property. Simply pass it one parameter --- the property whose value you want to
 * know:
 * */
$("div").css("width");
$("div").css("margin-right");
$("div").css("color");

/* It’s important to note that if you have a set of more than one element and 
 * you call css(), you’ll get the result as if css() was called on just the first 
 * element. Another important note is that you can’t use shorthand. For example, 
 * this won’t work:
 * $("div").css("margin");
 * */
/*
 * You can also use CSS to set values. To set just one value, pass in a property 
 * and a value as seperate parameters.
 * */
/*
 * What's more useful is that the css() method also accepts an object of key-value 
 * pairs that map CSS properties to the values you want to set:
 * */
$("div").css({
    "background": "red",
    "margin-left": "200px",
    "color": "black"
});

//#############################################################################
$("div").addClass("column");
$("div").removeClass("column");

// If you want to check if an element has a particular class, there' hasClass():
$("div").hasClass("column");
/*
 * That will return true or false. If you want to add a class to something, you 
 * can do it regardless of whether the element already has that class or not. 
 * jQuery is smart enough to sort all that out for you. There's no need to do this:
 * */
if(!$("div").hasClass("main")){
    $("div").addClass("main");
}
/*
 * Simply call addClass(). Similary, there's no need to check whether an element 
 * has a class before you remove that class. Both these methods can take multiple 
 * arguments:
 * */
$("div").addClass("one two three");
$("div").removeClass("four five six");

/*
 * In a situation where you'd like to add a class if the element doesn't have it 
 * --- but remove that same class if the element does have it:
 **/
$("div").toggleClass("main");

//#############################################################################
$("div").hide();
$("div").show();
/*
 * What’s great about them is that when you use hide() to hide an element, 
 * jQuery not only hides it but also remembers its display property. Then, 
 * when you call show() on that element, it sets the display property back to 
 * what it was previously. 
*/

// animate() and Animation Convenience Methods

// slideUp
// slideDown
// slideToggle
/*
* These methods animate elements by height. slideUp will animate an element to a 
* height of 0, creating the effect that the element slides up the page, with 
* its height getting smaller and smaller until it disappears. slideDown does 
* the reverse, animating an element's height to a specific value. Finally, 
* slideToggle will either slide an element up or down, based on the state it's in 
* when you call it. If you call slideToggle on an element that has height 0, it 
* will slide it down and reveal it. If you call slideToggle on an element that 
* is visible, it will slide it up.
* */

//#############################################################################
/*
 * To get and set attributes of DOM elements, jQuery provides the attr() method.
 * This works just like the css() method. There are three ways to do things:
 * */
// $("div").attr("id")  to get the value of the ID attribute.
// $("div").attr("id", "main")  to set the value of the ID attribute to "main"
// $("div").attr({
//      "id": "main",
//      "rel": "one"
// });  to set multiple attributes at once.

// prop() vs. attr()

//#############################################################################
// text() vs. html()
/* If you want to update some text within an element, the best way to do it is 
* by using the text() method.
*
* When you pass in HTML to the text() method, it is automatically escaped for you.
* This means that jQuery replaces the symbol "<" with its HTML entity, which is 
* "&lt;". The browser then displays this as the "<" symbol, but it's not HTML, 
* just plain text.
*
* html() works exactly the same as text() but will not escape any HTML within it.
*
* You shouldn't get into the practice of inserting complex HTML via these methods,
* though. jQuery provides a myriad of options for inserting into the DOM.
*/

//##############################################################################
// Removing Elements from the DOM
/*
 * remove() vs. detach()
 *
 * remove() will remove the set of elements from the DOM but also remove anything 
 * else associated with it --- such as events.
 * 
 * remove() returns the entire set of elements that match the selector, not just
 * the set of elements it just removed.
 * 
 * If you want to remove an element from the DOM but not its associations, there's 
 * detach(). 
 * */
/*
 * At times, you might want to remove everything within an element but not the
 * element itself. This is where empty() comes in.
 * */

/*
 * The final method for removing an element is unwrap(), which does roughly the
 * opposite of empty(). empty() takes an element and removes its children,
 * whereas unwrap() takes an element and removes its parent element.
 * */

// Creating New Elements
/*
* Before getting to inserting new content into the DOM, you first need to look
* at how to create a new object. 
* The easiest way is to create a string of HTML.
* However, this can get complicated very quickly if you're inserting structures
* that are more complex.
* */
var newDiv = $("<div></div>", {
    "text": "Hello",
    "class": "newDiv",
    "title": "Hello"
});
/*
 * That's the best way to create complicated elements, which have a lot of
 * attributes to set. 
 * You call jQuery on an empty element, and then pass in an object that maps
 * properties to values.
 * */

// Inserting into the DOM
/*
* 1. DOM Insertion, Around: These methods let you insert elements around existing
* ones.
* 2. DOM Insertion, Inside: These methods let you insert elements within
* existing ones.
* 3. DOM Insertion, Outside: These methods let you insert elements outside
* existing ones that are completely separate.
* */

// DOM Insertion, Around
/*
 * 1. wrap()
 * 2. wrapAll()
 * 3. wrapInner()
 * */

/*
 * <div>
 *  <p>hey</p>
 * </div>
 * */
$("p").wrap("<div></div>");
/*
 * <div>
 *  <div>
 *      <p>Hey</p>
 *  </div>
 * </div>
 * */

var newDiv = $("<div />", {
    "class": "Hello",
    "text": "Hey"
});
$("p").wrap(newDiv);

/*
 * wrapAll() does something similar with wrap(): it will take every element in
 * the set and wrap and wrap them all in the new element.
 * */
/*
 * <div>
 *  <p>Hey</p>
 *  <p>Hello</p>
 * </div>
 * */
$("p").wrapAll("<div />");
/*
 * <div>
 *  <div><p>Hey</p><p>Hello</p></div>
 * </div>
 * */
/*
 * The final wrap function is wrapInner(), which wraps the contents of each
 * element in the new element.
 * */
$("p").wrapInner("<strong />");
/*
 * <div><p><strong>Hey</strong></p> <p><strong>Hello</strong></p></div>
 * */


// DOM Insertion, Inside
/*
 * append()
 * appendTo()
 * html()
 * prepend()
 * prependTo()
 * text()
 * */

/*
 * <div></div>
 * <div></div>
 * <div></div>
 * */
var p = $("<p />", {
    "text": "Hello"
});
$("div").append(p);
/*
 * <div><p>Hello</p></div>
 * <div><p>Hello</p></div>
 * <div><p>Hello</p></div>
 * */

// DOM Insertion, Outside
/*
 * after()
 * before()
 * insertAfter()
 * insertBefore()
 * */
// <div><p>Hello</p></div>
$("p").after("<span>Hey</span>");
// <div><p>Hello</p><span>Hey</span></div>

// and if you were to do:
$("p").before("<span>Hey</span>");
// <div><span>Hey</span><p>Hello</p></div>

$("<span>Hey</span>").insertAfter("p");
$("<span>Hey</span").insertBefore("p");

/*
 * DOM manipulation is expensive. Relative to most of the JavaScript you'll
 * write, removing, manipulatiing, or inserting DOM elements is going to be the
 * slowest part.
 * */

// 为了提升效率，应尽可能少地操作DOM，下面的两段代码，片段2就优于片段1
// 代码片段1
$(function(){
    var i = 0;
    var newUl = $("<ul />").appendTo("body");
    while( i < 10 ) {
        $("<li />", {
            "text": i+1
        }).appendTo(newUl);
        i++;
    }
});

// 代码片段2
$(function() {
    var i = 0;
    var newUl = $("<ul />");
    while( i < 10 ) {
        $("<li />", {
            "text": i+1
        }).append(newUl);
        i++;
    }
    newUl.appendTo("body");
});
/*
 * The key here is that you don't append the unordered list to the body until
 * the loop is complete. You can create an element and add elements to it before
 * you add it that element to the DOM. That's the best way to do it.
 * */

//##############################################################################
// An introduction to Events

/*
 * Previously there were a huge number of methods, all focused on event binding.
 * There were individual handlers like click(), hover(), and so on. Then there
 * were more methods for general event binding, such as bind(), live() and
 * delegate(). this got complicated and required a lot of explaining. Those
 * methods all still exist in jQuery now, but it's highly advised that you
 * switch to just using on().
 * */

/*
 * hover() isn't actually an event, but it's shorthand for binding two functions
 * at once---one to the mouseenter event, which is executed when the mouse
 * hovers over the element in question, and one for the mouseleave event, which
 * is when the mouse stops hovering over the element.
 * */
$("div").hover(function() {
    alert("hovered in");
}, function() {
    alert("hovered out");
});

/*
 * If you would rather use the new on() method, you have to use the mouseenter
 * and mouseleave events:
 * */
$("div").on("mouseenter", function() {
    alert("hovered over");
}).on("mouseleave", function() {
    alert("hovered out");
});

/*
 * on() allows you to bind the same function to multiple events. Simply pass
 * them into the on() method as a space-demilited string:
 * */
$("div").on("mouseenter mouseleave", function() {
    alert("hovered on or out");
});

$("div").on("mouseenter mouseleave click dblclick", function() {
    alert("hovered on or out, clicked or double clicked");
});

/*
 * The main mouse events you need to be aware of are:
 * click
 * mouseenter
 * mouseleave
 * dblclick
 * */
/*
 * Another important part of jQuery'e events are the form events.
 * jQuery makes enhancing forms using JavaScript --- such as custom validation
 * --- really straightforward.
 * */
/*
<form action="/some/url" method="post">
    <label>Enter your first name: </label>
    <input type="text" name="first_name" >
    <input type="submit" name="submit" value="submit" >
</form>
*/
$("form").on("submit", function() {
    alert("you just submitted the form!");
});

/*
 * For dealing with events on individual inputs, the two events you will use
 * most often are focus and blur, which are exact opposites of each other.
 * The focus event is fired when an element has focus. The most obvious example 
 * is when the user clicks an input box or starts typing in it. At that moment,
 * the element has focus and the focus event is fired. When the user moves on,
 * clicking another element or just off the element, the blur method fired.
 * Think of focus and blur as being a little like mouseenter and mouseleave in
 * how they work. The most important difference is that focus and blur can be
 * triggered in more ways than just via a mouse. The can also be triggered via
 * the keyboard when the user tabs through a form. Thus, for events to be fired
 * based on an input element being active, never use mouseenter or mouseleave.
 * Always use focus and blur.
 * */

$("input").on("focus", function() {
    alert("you're focused on an input");
}).on("blur", function() {
    alert("this input just lost focus");
});


/*
 * Sometimes you might want to manually trigger an event. Perhaps you've got a
 * link that enables the user to fill out a form, and when it's clicked you'd
 * like to fire the submit event on a form. jQuery has the trigger() method to
 * do this for us:
 * */
$("a").on("click", function() {
    $("form").trigger("submit");
});

/*
 * Just as you have on() for binding to events, you have off() for unbinding
 * from events.
 * */
$("div").off();
/*
 * That will unbind all events from every div. You can also pass in an event as
 * the first parameter to unbind all events of that type.
 * */
// It's also possible to unbind just a specific function.
$(function() {
    var clickEvent = function() {
        alert("clickEvent");
    };
    $("p").on("click", function() {
        alert("click");
    }).on("click", clickEvent);

    $("p").off("click", clickEvent);
});

// The Event Object

/*
 * Whenever you bind an event to a function and that function is then triggered,
 * jQuery passes what’s known as the event object. This object contains a lot of 
 * information about the event. To get access to this, just make your event
 * handler take one parameter as an argument. jQuery then passes the event
 * object into this function, and you can get at it through the argument that
 * you denoted your function should take.
 * */
$(function() {
    $("p").on("click", function(event) {
        console.log(event);
    });
});

$(function() {
    $("div").on("hover", function(event) {
        if(event.type === 'mouseenter') {
            $(this).css("background", "blue");
        }else{
            $(this).css("background", "red");
        }
    });
});

/*
 * You can use the pageX and pageY properties to get the position of the mouse
 * when the event fired, relative to the top-left edge of the document window.
 * */
$(function() {
    $("div").on("click", function(event) {
        alert("Your mouse is at X " + event.pageX + " and at Y " + event.pageY);
    });
});

// Building an Accordion
$(function() {
    var headings = $("h2");
    var paragraphs = $("p");
    paragraphs.not(":first").hide();

    headings.on("click", function() {
        var t = $(this);
        if(t.next().is(":visible")) {
            return;
        }
        paragraphs.hide();
        t.next().show();
    });
});

// vs.
$(function() {
    var headings = $("h2");
    var paragraphs = $("p");
    paragraphs.not(":first").hide();
    headings.on("click", function() {
        var t = $(this);
        var tPara = t.next();
        if(tPara.is(":visible")) {
            return;
        }
        paragraphs.slideUp("normal");
        tPara.slideDown("normal");
    });
});

//##############################################################################

//// More Events

// Event Delegation

/*
 * Two problems:
 * 1. How can you run a function whenever a paragraph is clicked, but still bind
 * it efficiently when there are a lot of paragraphs?
 * 2. How can you make it so any new paragraph inserted into the DOM also run
 * the code when they are clicked?
 * */
/*
 * 'event delegation' means that instead of binding the event to each paragraph
 * individually, you bind the event to a parent element of all the paragraphs
 * and let it delegate the event to the paragraph.
 * */
/*
 * An explanation of how it works:
 * 1. The click event is bound to a parent element of all you paragraphs (keep it
 * simple and use the body element for this example).
 * 2. When the body element detects an event of the type you bound (click, in this
 * case), it checks to see if the click happened on a paragraph.
 * 3. If it was, it fires the function you bound to it. This is where the
 * delegation happens.
 * */

$(function() {
    $("p").on("click", function() {
        alert("Hello world");
    });
    $("<p />", {
        text: "Paragraph 6"
    }).appendTo("body");
});

// vs.
$(function() {
    $("body").on("click", "p", function() {
        alert("Hello world");
    });
    $("<p />", {
        text: "Paragraph 6"
    }).appendTo("body");
});

/*
 * If you're binding an event to just one element, there's no point in
 * delegating because you don't gain anything. 
 * */


// Event Propagation

/*
 * Event propagation is the same as event bubbling; they are simply two terms
 * meaning the same thing.
 * */
/*
 * When an event is fired on a element in the browser, it's not just fired on
 * that element, but every element that is a parent of it.
 * */
/*
 * While most events (including the ones you'll work with most often) propagate,
 * not all of them do.
 * */
// http://en.wikipedia.org/wiki/DOM_events

/*
 * Typically, the only time you need to worry about event propagation is when 
 * you are binding an event to both an element and the element's parent.
 * */
/*
 * Luckily, there is a way to stop event propagation. The event object has a
 * method named 'stopPropagation' that can prevents the event from bubbling up
 * the DOM tree, preventing any parent handlers from being notified of the
 * event.
 * */
$(function() {
    $("h5").on("click", function(event) {
        alert("header");
        event.stopPropagation();
    });
    $("div").on("click", function() {
        alert("div");
    });
});

/*
 * Unless the propagation of an event is causing an issue, don't prevent it.
 * */

// Preventing Default Behavior
/*
 * Sometimes when you bind to an event, you need to stop the browser from
 * performing the default action attached to that event.
 * */
$(function() {
    $("a").on("click", function(event) {
        event.preventDefault();
        $("div").css("background", "blue");
    });
});

//######
$(function() {
    $("a").on("click", function() {
        $("div").css("background", "blue");
        return false;
    });
});

/*
 * Making a handler return Boolean false has the effect of stopping the default
 * event action from being called and stopping the event from propagating. In
 * essence, it effectively is a shortcut for calling stopPropagation and
 * preventDefault.
 * As I explained, most of time you actually don't want to call stopPropagation,
 * so I strongly advise avoiding return false;, and instead use preventDefault.
 * */

// You Own Events
/*
 * A seldom-used but very useful feature of jQuery’s events is the ability to 
 * trigger and bind to your own custom events.
 */
$(function() {
    $("h5").on("click", function() {
        $("div").trigger("bgchange");
    });
    
    $("div").on("bgchange", function() {
        var t = $(this);
        t.css("background-color", "blue");
    });
});

/*
 * The beauty of custom events is that they give you a neat way to package up
 * your code and keep as much of it separate as possible. It also allows you to 
 * assign meaningful names to the events you create, keeping your code easy to 
 * follow and maintain.
 */


$(function() {
    var accordion = $("#accordion");
    var headings = $("h2");
    var paragraphs = $("p");
    paragraphs.not(":first").hide();
    accordion.on("click", "h2", function() {
        var t = $(this);
        var tPara = t.next();
        if(!tPara.is(":visible")) {
            tPara.trigger("showParagraph");
        }
    });

    accordion.on("showParagraph", "p", function() {
        paragraphs.slideUp("normal");
        $(this).slideDown("normal");
    });
});

//##############################################################################

// Animation
/*
* The animate() method can be used to animate a number of properties on an
* element over a period of time.
* */

animate({
    property: value,
    property2: value2
}, 500, function() {
    console.log("finished");
});
/*
 * Within the callback function, the value of this will refer to the DOM element 
 * that has just been animated. If you wanted to use jQuery methods on that
* object, you'd simply pass it through to jQuery, as follows: $(this)
* */


/*
 * fadeIn()
 * fadeOut()
 * fadeToggle()
 * fadeTo()
 * */

/*
 * slideUp()
 * slideDown()
 * slideToggle()
 * */
/*
 * If you ever find yourself checking whether an element is visible or not
 * before sliding/fading it in, use the toggle methods to save yourself some
 * work.
 * */

/*
 * show()
 * hide()
 * toggle()
 * */

// The Animation Queue
/*
 * When you run multiple animations on a single element, they are not all run at
 * the same time but are added to jQuery's animation queue.
 * */
/*
 * jQuery performs animation through a series of setTimeout() calls.
 * setTimeout() is a JavaScript method that runs code after a defined time
 * interval. When you run code to animate a div's opacity from 1 to 0, it
 * actually makes a large number of very small changes to the opacity over time
 * to emulate an animation. There's no actual fading occuring. It's just very
 * quickly changing the opacity by a small amount to give the illusion of
 * animation.
 * */

// The lag effect problem

$(function() {
    $("h5").on("click", function() {
        $("div").fadeToggle(500);
    });
});

// VS.

$(function() {
    $("h5").on("click", function() {
        $("div").stop().fadeToggle(500);
    });
});

// VS.

$(function() {
    $("h5").on("click", function() {
        $("div").stop(true, true).fadeToggle(500);
    });
});


// Making things as easy as possible is really important in my opinion.

//##############################################################################

// The Image Slider

/*
#slider {
    width: 300px;
    overflow: hidden;
    height: 400px;
}

#slider ul {
    list-style: none;
    width: 1500px;
    height: 300px;
    margin: 0;
    padding: 0;
}

#slider li {
    float: left;
    width: 300px;
    height: 300px;
}
*/

$(function() {
    var sliderWrapper = $("#slider");
    var sliderList = sliderWrapper.children("ul");
    var sliderItems = sliderList.children("li");
    var buttons = sliderWrapper.children(".button");

    var animateSlider = function(direction, duration) {
        sliderList.animate({
            "margin-left": direction + "=300px"    
        }, duration);
    };

    var isAtStart = function() {
        return parseInt(sliderList.css("margin-left"), 10) === 0;
    }

    var isAtEnd = function() {
        var imageWidth = sliderItems.first().width();
        var imageCount = sliderItems.length;
        var maxMargin = -1 * (imageWidth * (imageCount-1));
        return parseInt(sliderList.css("margin-left"), 10) === maxMargin;
    }

    /*
    buttons.on("click", function() {
        if($(this).hasClass("back")){
            animateSlider("+", 1000);
        } else {
            animateSlider("-", 1000);
        }
    });
    */
   buttons.on("click", function() {
       var $this = $(this);
       var isBackBtn = $this.hasClass("back");

       if(isBackBtn && isAtStart()) {
           return;
       }
       if(!isBackBtn && isAtEnd()) {
           return;
       }
       // if((isBackBtn && isAtStart()) || (!isBackBtn && isAtEnd())) { return; }
       animateSlider((isBackBtn ? "+" : "-"), 1000);
   });
});

/*
 * If the margin of the unordered list is set to 0, it means you are at the
 * first image, and hence the Back button should be disabled. If the margin is
 * set to -1200 pixels, you are at the last image.
 * */
