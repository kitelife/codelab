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
