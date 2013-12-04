/*
 * 读书笔记：<Learning Raphael JS Vector Graphic>
 * 
 */

/********************************************************************************************************
 * 1. The Graphical Web
 * *****************************************************************************************************/

/*
 * There are a number of technologies that have emerged to enable the process of browser-based drawing 
 * including, but not limited to VML and SVG, HTML5 Canvas, and WebGL. Each is generally suited to a particular
 * purpose - 2D vector drawing in the case of VML and SVG, bitmap drawing in the case of HTML5 Canvas, and 3D 
 * graphics rendering in the case of WebGL.
 * 
 *
 * Raphael takes care of outputting graphics at the SVG/VML specification level, which means that we only need
 * to concern ourselves with utilizing the library itself.
 */


// 1.1 Vector drawing on the web

/*
 * Vector graphics are composed of a number of primitive geometric objects such as points, lines, shapes, and 
 * polygons(多边形). Each individual object is represented by a mathematical expression rather than some fixed
 * physical point. Scaling vector graphics means changing the mathematical properties of the constituent objects
 * and not the the objects themselves and quality is not lost as a result.
 *
 * All graphics are ultimately rendered at the fixed point, or pixel, level. Your display is, after all, the sum 
 * of many millions of these points. The difference between bitmap and vector graphics is that in the case of 
 * vector graphics, the rendering is done at the very last moment. Scaling up a bitmap means creating new pixels 
 * based on the existing ones whereas with vector graphics, pixels are created at the resolution at which the 
 * final graphic is rendered based on the abstract mathematical definition of the object.
 * 
 * Vector drawing on the Web has predominantly taken shape in the following two forms:
 * 1. Vector Markup Language (VML)
 * 2. Scalable Vector Graphics (SVG)
 * */


/**************************************************************************************************************
 * 2. Basic Drawing with Raphael
 * ***********************************************************************************************************/

/*
 * Raphaël supports three fundamental types of graphics elements: shapes, images, and text. Shapes can be predefined 
 * shapes such as a rectangle, circle, or ellipse or they can be a combination of lines, curves, and paths. Vector 
 * graphics are by their very definition the sum of such shapes.
 * 
 * Images are either bitmap images (such as  .png or  .jpeg ) or existing SVG images, and can be manipulated by 
 * Raphaël in many of the ways that shapes can be.
 * 
 * Shapes and text can be painted, that is, filled and stroked (given an outline). Fills can be either a single 
 * color or a linear or radial gradient. Strokes can only be filled by a single color but the way in which a 
 * shape is stroked is modifiable.
 * */

// 2.1 The drawing context

/*
 * In order to be able to draw graphics we need to define a space into which our content can be rendered. 
 * 
 * The SVG specification refers to the drawing area itself as the viewport. Strictly speaking, a viewport 
 * is any rectangular viewing region. We will always refer to the browser window as the viewport and our drawing 
 * region as the canvas (not to be confused with the HTML5 Canvas).
 * 
 * We can create a canvas using the  Raphael constructor as follows:
 * */

var paper = Raphael(50. 100, 500, 300);

/*
 * This creates a canvas of width 500px and height 300px at 50px to the left of the viewport and 100px from 
 * the top of the viewport. 
 * 
 * More commonly we will want to use an existing DOM element as a container for our canvas rather than the viewport.
 * In this case, the left-/right- (x-/y-) offsets are not required as the canvas will always be rendered at the 
 * top-left corner of the element. Consider the element:
 * 
 * <div id="my-canvas"></div>
 *
 * We would create our 500px wide, 300px high canvas using the following code:
 * */

var paper = Raphael('my-canvas', 500, 300);

/*
 * Alternatively, we can pass a DOM element as the first parameter like so:
 * */

Raphael(document.getElementById('my-canvas'), 500, 300);

// 2.2 Drawing basic shapes

/*
 * Raphaël provides the rect, circle, and ellipse methods for drawing basic shapes.These are methods of the Paper 
 * object that is returned when we create our canvas.
 * 
 * The syntax for a rectangle:
 *
 * Paper.rect(x, y, width, height, [r]);
 *
 * A rectangle of width 50px and height 100px at x = 200px, y = 150px is created as follows:
 * */

var paper = Raphael('my-canvas', 500, 300);
var rectangle = paper.rect(200, 150, 50, 100);

/*
 * Similarly, we create a square of width 75px with a corner radius of 15px by:
 * */

var square = paper.rect(300, 150, 75, 75, 15);

/*
 * The syntax for a circle is:
 *
 * Paper.circle(x, y, r);
 *
 * While the x and y coordinates of a rectangle describe its top-left point, for a circle they define its 
 * center point. The third parameter, r, is the radius of the circle.
 *
 * The syntax for an ellipse is very similar to a circle except that we specify the individual x- and y-radius:
 *
 * Paper.ellipse(x, y, x-radius, y-radius);
 * 
 * */

// 2.3 Embedding images

/*
 * Raphaël allows us to embed bitmap ( .jpg or  .png ) images into our canvas. It does so using the image method 
 * of the the  Paper object. The following code demonstrates embedding a .jpg image:
* */

var paper = Raphael('my-canvas', 600, 252);
paper.image('stella.jpg', 15, 15, 144, 192);

// 2.4 Element attributes

/*
 * The shapes that we have drawn can have fills, strokes, and a number of other attributes applied to them. 
 * When we create a shape, an  Element object is returned. This object has an  attr method that accepts a number 
 * of key-value pair attributes.
 * */

// 2.4.1 Basic fills

var rect = paper.rect(200, 50, 200, 100);
rect.attr({fill: '#000'});
var square = paper.rect(450, 50, 50, 50);
square.attr({fill: 'rgb(0, 0, 0)'});
var circle = paper.circle(100, 100, 50);
circle.attr({fill: 'pink'});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-2/basic-fills
 * */

// 2.4.2 Image fills

var circle = paper.circle(100, 100, 80);
circle.attr({fill: 'url(bg_pattern.png)'});
/*
 * Image fills are always repeated in x and y.
 * 效果见： http://raphaeljsvectorgraphics.com/book/chapter-2/image-fills
* */

// 2.4.3 Applying strokes

/*
 * Elements can have a number of different stroke attributes. The most common are the stroke and stroke-width 
 * attributes. The  stroke attribute takes a string value for color in line with the CSS specification while 
 * stroke-width is a number in pixels.
 * */
var circle = paper.circle(100, 100, 70);
circle.attr({
    fill: '#09c',
    stroke: 'limegreen',
    'stroke-width': 10
});
/*
 * 效果见： http://raphaeljsvectorgraphics.com/book/chapter-2/stroke-widths
 * */

// 2.4.4 Other attributes

// 2.4.4.1 href

/*
 * The elements that we create are registered in the DOM and specifying a href attribute allows them to 
 * behave as hyperlinks.
 * */
var rect = paper.rect(30, 30, 140, 140);
rect.attr({
    href: 'http://www.packtpub.com'
});

// 2.4.4.2 opacity(不透明度)

/*
 * The opacity of elements can be set to a value between 0 (complete transparency) and 1 (complete opacity). 
 * We can also set the opacity on the fill and stroke separately by using the  stroke-opacity and fill-opacity 
 * attributes.
 * */

// 2.4.4.3 clip-rect

/*
 * Raphaël supports rectangular clipping of elements using the  clip-rect attribute. Clipping allows us to 
 * show only part of an element. We define a rectangular clipping region as follows:
 * */
var circle = paper.circle(100, 100, 80, 80);
circle.attr({
    fill: 'pink',
    'stroke-width': 0,
    'clip-rect': '20 20 80 80'
});
/*
 * The clip-rect attribute defines a rectangular region from a space-separated string of the form:
 *
 * "x y width height"
 *
 * 效果见： http://raphaeljsvectorgraphics.com/book/chapter-2/clip-rect
 * 同样 图片（image对象）也可以裁剪。
 * */

// 2.4.5 Applying gradients(渐变)


