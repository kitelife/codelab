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

/*
 * Raphaël supports applying linear and gradient fills to elements. To achieve this, rather than 
 * specifying a color string on the  fill attribute, we specify a string of the following form 
 * in order to create linear gradients:
 * 
 * <angle>-<color>[-<color>[:<offset>]]*-<color>
 *
 * The following syntax is in order to create radial gradients:
 *
 * r[(<fx>, <fy>)]<color>[-<color>[:<offset>]]*-<color>
 *
 * */

// 2.4.5.1 Linear gradients

/*
 * 演示图：
 *  http://raphaeljsvectorgraphics.com/book/chapter-2/linear-gradients-1
 *  http://raphaeljsvectorgraphics.com/book/chapter-2/linear-gradients-coordinates
 *  http://raphaeljsvectorgraphics.com/book/chapter-2/linear-gradients-2
 * */

// 2.4.5.2 Radial gradients

/*
 * 演示图：
 *  http://raphaeljsvectorgraphics.com/book/chapter-2/radial-gradients-1
 *  http://raphaeljsvectorgraphics.com/book/chapter-2/radial-gradients-2
 *  http://raphaeljsvectorgraphics.com/book/chapter-2/radial-gradients-focus
 *  */

// 2.4.6 Grouping elements

/*
 * There are times when we wish to apply the same attributes, transformations, or animations to 
 * multiple elements. We can group elements in Raphaël by using the set method. 
 * */

var paper = Raphael('my-canvas', 540, 200);
var circle = paper.circle(100, 100, 80);
var rect = paper.rect(205, 40, 120, 120);
var ellipse = paper.ellipse(430, 100, 80, 60);
var group = paper.set();
group.push(circle, rect, ellipse);
group.attr({
    fill: '180-#09c-#fff:30-#f00',
    stroke: '#000',
    'stroke-width': 5
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-2/grouping-with-sets
 * */

// 2.5 Working with text

/*
 * Drawing text in the canvas rather than as HTML markup with CSS styling allows us to animate 
 * and transform it in the same way as we would for other shapes. Text is created using the  
 * text method and its properties (such as size and font-family) are modifiable as attributes. 
 * The text method has the following definition, where the text parameter is our text string 
 * and accepts the standard escape sequence '\n' as input, which places the proceeding text 
 * onto a new line:
 *
 * Paper.text(x, y, text)
 *
 * */

var text1 = paper.text(0, 15, 'I am text anchored start.');
text1.attr({
    'text-anchor': 'start',
});
var text2 = paper.text(270, 100, 'I am text\nanchored middle');
text2.attr({
    'text-anchor': 'middle'
});
var group = paper.set(text1, text2);
group.attr({
    'font-size': 20,
    'font-family': 'serif'
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-2/text
 *
 * You should notice that we have defined an individual attribute, text-anchor, on each text 
 * element. The text-anchor attribute has the effect of determining whether the origin x point 
 * on the text method is defined at the center of the text or at its leftmost edge. By default 
 * it is defined at its center.
* */

// 2.5.1 Embedding custom fonts


/******************************************************************************************************
 * 3. Drawing Paths
 * ***************************************************************************************************/

/*
 * Paths allow us to draw all manner of shapes by defining points connected by lines, arcs, and curves
 * representing the outline of the shape itself.
 *
 * Paths, such as basic shapes, are elements meaning that user interaction, painting, transformations, 
 * and animation are all possible with paths.
 *
 * */

// 3.1 Path drawing concepts

/*
 * The process of drawing with a pen on paper can be broken down into the following steps:
 *  1. You place your pen at a particular point on a piece of paper.
 *  2. You press and move the pen freely from this point to another point.
 *  3. You keep your pen at this point or lift up the pen and place it at another point on the paper.
 *  4. The process is repeated until you have finished drawing.
 *
 * Path drawing works in much the same way. The point at which you place your pen, known as the 
 * current point, defines the start of a path while the free movement of the pen describes the 
 * path itself.
 *  
 * */

// 3.2 Path drawing commands

/*
 * Paths are based on a number of drawing commands executed in the order in which they're defined. 
 * Commands are expressed as a single letter that is either uppercase, meaning that a subsequent 
 * drawing uses absolute coordinates in the drawing context, or lowercase, meaning that a 
 * subsequent drawing uses coordinates relative to the current point.
 *
 * We draw paths in Raphaël using the  path method, which accepts either a path string or 
 * an array as a parameter. Arrays are usually a more convenient and more readable way of 
 * defining paths.
 * 
 * */

// 3.2.1 The moveto command

/*
 * The moveto command establishes a new current point. In the pen analogy detailed in the 
 * previous section, issuing a moveto command has the effect of lifting the pen off the page 
 * and placing it at a given point. All paths start with a moveto command.
 *
 * --------------------------------------------------------------
 *  Command         Parameters          Example
 * --------------------------------------------------------------
 *  M or m          (x, y)+             M 50, 50 100, 100
 * --------------------------------------------------------------
 * 
 * You may have noticed that the moveto syntax allows us to repeat the  x and  y parameters 
 * (indicated by the  + symbol). For example:
 *
 * "M 50,50 100,150"
 *
 * The first (x, y) pair moves the pen to the point (50, 50) on our canvas as we would expect. 
 * However, the second (x, y) pair has the effect of drawing a line to the point (100, 150), 
 * as well as moving the current point. This behavior means that the moveto command can be 
 * used to draw polygons(多边形).
 *
 * The following code draws a triangle with vertices at (250, 50), (200, 100), and (300, 100) 
 * using only the moveto command:
 * */

var path = paper.path([
                      'M', 250, 50
                      200, 100,
                      300, 100,
                      250, 50
]);

/*
 * You should notice that all the (x, y) points mentioned are absolute, that is, defined 
 * relative to the origin point of our canvas. Were we to specify the lowercase variant of
 * the command,  m , every successive (x, y) pair would be relative to the previous one 
 * (but note that the first (x, y) pair is always positioned using absolute coordinates 
 * regardless of the  M command's case).
 * */

// 3.2.2 The lineto commands

/*
 * The lineto commands draw straight lines from the current point to a point specified.
 * There are three lineto commands:
 *  L for drawing lines to any (x, y) point
 *  H for drawing horizontal lines in x
 *  V for drawing vertical lines in y
 * 
 * ------------------------------------------------------------------
 *  Command         Parameters          Example
 * ------------------------------------------------------------------
 *  L or l          (x, y)+             L 100 100
 *  H or h          x+                  H 75
 *  V or v          y+                  V -75
 * ------------------------------------------------------------------
 * */

var sideLength = 100;
var x = sideLength * Math.cos(Raphael.rad(60));
var y = sideLength * Math.sin(Raphael.rad(60));
var hexagon = paper.path(
    ['M', 250, 15,
        'l', sideLength, 0,
        x, y,
        -x, y,
        -sideLength, 0,
        -x, -y,
        x,-y,
    ]
);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/04_lineto_hexagon
 *
 * Note that in JavaScript, the trigonometric functions expect a value of angle measured 
 * in radians to be passed so we have used the  rad utility method on the  Raphael object
 * to convert 60 degrees into radians.
 * */

// 3.2.3 The closepath command

/*
 * The closepath command draws a straight line from the current point to the starting point 
 * of the current subpath.
 *
 * The closepath command character is  Z and does not accept any parameters. 
 * */

var hexagon = paper.path(
    ['M', 250, 15,
        'l', sideLength, 0,
        x, y,
        -x, y,
        -sideLength, 0,
        -x, -y,
        'z' // in place of the line to (x, -y)
    ]
);

/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/05_closepath
 *
 * Note that the closepath command can be either uppercase or lowercase but this has 
 * no effect on its behavior.
 * 
 * */


// 3.3 Drawing curves

/*
 * There are three types of curve path: quadratic Bézier curves(二次贝塞尔曲线), 
 * cubic Bézier curves(三次贝塞尔曲线), and arcs(弧线).
 *
 * Bézier curves are curves defined between a start and end point but whose direction 
 * we can determine by using control points, while arcs are a portion of the circumference(圆周) 
 * of an ellipse(椭圆).
 * 
 * */

// 3.3.1 Quadratic Bézier curves

/*
 * A quadratic Bézier curve is a curve between two points with a single control point.
 *
 * 演示： http://www.jasondavies.com/animated-bezier/
 *
 * There are two quadratic Bézier curve commands:
 *
 * ------------------------------------------------------------
 *  Command         Parameters          Example
 * ------------------------------------------------------------
 *  Q or q          (x1, y1, x, y)+     Q 100 50 200 250
 *  T or t          (x y)+              T 400 250
 * ------------------------------------------------------------
 *
 * The Q command (or q for relative points) describes a curve drawn from the current point 
 * on a path to the point (x, y) using (x1, y1) as a control point. For example, consider 
 * the following code:
 * */

paper.path(['M', 50, 150, 'Q', 225, 20, 400, 150]);
/*
 * 效果：http://raphaeljsvectorgraphics.com/book/chapter-3/06_quadratic_bezier
 *
 * Moving the control point affects the way that the path is drawn.
 *
 * As with the other commands we have encountered so far, parameters can be repeatable, 
 * which allows us to draw multiple connected quadratic Bézier curves.
 * */

paper.path([
           'M', 50, 150
           'Q', 225, 20, 400, 150,
           575, 20, 750, 150
]);
/*
 * This has the effect of drawing a second curve from (400, 150) to the point (750, 150) 
 * with a control point at (575, 20).
 *
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/08_quadratic_bezier_03
 * 
 * The T or t command is shorthand whereby the control point coordinates are not specified. 
 * Instead, the control point is determined automatically as a reflection(镜像) of the previous 
 * control point.
 * 
 * */

paper.path([
           'M', 50, 150,
           'Q', 225, 20, 400, 150,
           'T', 750, 150
]);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/09_quadratic_bezier_04
 * 
 * The current point at the start of the path drawn by T is (400, 150). Relative to 
 * this point, a reflection of the previous control point (225, 20) is (575, 280).
 * 
 * */

// 3.3.2 Cubic Bézier curves

/*
 * The principles behind drawing cubic Bézier curves are similar to those for quadratic Bézier curves 
 * except that cubic Bézier curves have two control points. 
 * 
 * 演示：http://www.jasondavies.com/animated-bezier/
 *
 * There are two cubic Bézier curve commands:
 *
 * --------------------------------------------------------------------------------
 *  Command                 Parameters                  Example
 * --------------------------------------------------------------------------------
 *  C or c                  (x1, y1, x2, y2, x, y)+     C 150 25 350 50 500 300
 *  S or s                  (x2, y2, x y)+              S 200 -100 200 50
 * --------------------------------------------------------------------------------
 * */

paper.path([
           'M', 200, 20,
           'C', 400, 140, 400, 180, 200, 120,
           'z'
]).attr({fill: '#222'});
/*
 * Note also that we have closed the path and applied an attribute fill.
 *
 * 效果见： http://raphaeljsvectorgraphics.com/book/chapter-3/11_cubic_bezier_01
 *
 * The  S command has a similar effect to the  T command in automatically creating a control point 
 * reflected about the current point. What it actually does is to reflect the second control point 
 * about the current point and this becomes the first control point for our new subpath, for which 
 * we now have to specify our second control point.
 * */

paper.path([
           'M', 200, 20,
           'C', 400, 140, 400, 180, 200, 120,
           'S', 0, 100, 200, 220,
           'z'
]);

/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/12_cubic_bezier_02
 *
 * The  S path starts from the current point (200, 120) and finishes at (200, 220) as shown.
 * The second control point from our first curve, defined at (400, 180), is reflected about
 * the current point, which creates a control point at (0, 60). We have then specified a 
 * second control point at (0, 100).
 *
 * The hardest thing about working with Bézier curves is deciding where to define your control points. 
 * Figuring these out is usually achieved by one of the following:
 *  Trial and error
 *  Mathematical computation
 *  Using a graphic package such as Inkscape to aid you in drawing
 * */

// 3.3.3 Drawing arcs

/*
 * The syntax for arc drawing:
 *
 * ------------------------------------------------------------------------
 *  Command         Parameters              Example
 * ------------------------------------------------------------------------
 *  A or a          (rx, ry,                a 25 50 0 1 0 100 200
 *                  x-rotation,
 *                  large-arc-flag,
 *                  sweep-flag,
 *                  x, y)+
 * ------------------------------------------------------------------------
 *
 * The following table describes each of the individual parameters:
 * -----------------------------------------------------------------------------------------
 *  Parameters          Description
 * -----------------------------------------------------------------------------------------
 *  rx and ry           Since an arc is a portion of an ellipse, it has a radius in x and y
 *  x-rotation          The counterclockwise rotation(旋转) of the ellipse along which the 
 *                      arch is drawn(a value in degrees)
 *  large-arc-flag      Whether our arc is drawn as a major(1) or minor(0) arc
 *  sweep-flag          Whether the arc is drawn in a positive(1), that is, clockwise or
 *                      negative(0), that is, counterclockwise, angular(角度) direction
 *  x and y             The end point of our arc
 * -----------------------------------------------------------------------------------------
 * */

paper.path([
           'M', 50, 60,
           'a', 150, 80, 0, 1, 1, 0, 80
]);
/*
 * We first move to the current point (50, 60) and then draw an arc with an x-radius of 150 
 * and a y-radius of 80. We set the  x-rotation value equal to 0 and identify that we're 
 * drawing the large arc by setting  large-arc-flag equal to 1. The sweep-flag value is 
 * equal to  1 and we use the lowercase, that is, relative, variant of the  A command meaning 
 * our final  x and  y parameters (0, 80) are units relative to the start point, that is: 0 
 * additional pixels in  x and 80 additional pixels in  y giving end point coordinates of (50, 140). 
 *
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/13_arcs_01
 *
 * Were we to specify a  large-arc-flag value equal to 0:
 *
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/14_arcs_02
 * */


// 3.4 Utility methods for working with paths

// 3.4.1 Element.getTotalLength()

var pin = paper.path({
    'M', 130, 350,
    'A', 100, 180, 0, 1, 0, 210, 350,
    'C', 290, 100, 50, 100, 130, 350,
    'z'
});
var totalLength = pin.getTotalLength();
paper.text(
    180, 50,
    "Total Length: " + totalLength.toPrecision(2)
);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/16_get_total_length
 * 
 * */

// 3.4.2 Element.getPointAtLength(length)

/*
 * We can get the x and y coordinates of any point along the length of a path using the getPointAtLength 
 * method. This method returns an object with  x and  y attributes.
 * */

var totalLength = pin.getTotalLength();
p1 = pin.getPointAtLength(totalLength / 8);
p2 = pin.getPointAtLength(totalLength / 2);
paper.circle(p1.x, p1.y, 10);
paper.circle(p2.x, p2.y, 10);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/17_get_point_at_length
 *
 * Another attribute of the object returned by  getPointAtLength is the  alpha attribute.
 * This returns the positive angle relative to the x-axis subtended by the gradient or 
 * derivative line at the point.
 *
 * Knowing the derivative at a point is useful as it informs us of the extent to which thearc is changing 
 * in x and y at that particular point.
 * */

// 3.4.3 Element.getSubpath(from, to)

var path = paper.path([
                      'M', 100, 100, 'c', 0, 100, 200, -100, 200, 0
]);
path.attr('stroke-width', 5);
var totalLength = path.getTotalLength();
var subPath = path.getSubpath(
    totalLength /4, totalLength / 2
);
paper.path(subPath).attr('stroke-width', 15);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/18_get_subpath
 * */

// 3.4.4 Catmull-Rom curves

/*
 * In those cases where we need to draw a curve that passes through a prescribed set of points, 
 * a Catmull-Rom curve is often appropriate. Catmull-Rom curves are commonly used in charting 
 * (that is, in data plotting) and gaming (for example, to move a character along a predefined 
 * trajectory).
 *
 * Raphaël provides a path command to facilitate the drawing of Catmull-Rom curves.
 *
 * -------------------------------------------------------------------------------
 *  Command         Parameters              Example
 * -------------------------------------------------------------------------------
 *  R or r          x1, y1 (xi, yi)+        R 25 50 0 1 0 100 200
 * -------------------------------------------------------------------------------
 *
 * The point  (x1, y1) is the second point the curve should pass through while the (xi, yi) 
 * points are every subsequent point. The first point should always be our current point, 
 * from which the curve starts. 
 * */

var data = [
    {x: 50, y: 250}, {x: 100, y: 100}, {x: 150, y: 150},
    {x: 200, y: 140}, {x: 250, y: 250}, {x: 300, y: 200},
    {x: 350, y: 180}, {x: 400, y: 230}
];
/*
 * To plot these data points, we iterate over the array and draw a circle at each x and y 
 * position (note that the points are grouped in to a set which makes applying attributes
 * to them easier):
 * */
var plottedPoints = paper.set();
for(var i = 0, num = data.length; i < num; i+=1) {
    var point = data[i];
    plottedPoints.push(paper.circle(point.x, point.y, 5));
};
plottedPoints.attr({fill: '#09c', 'stroke-width':0});
/*
 * When constructing our path string or path array, we make the current point our first data point 
 * using the  M command and append the  R command to begin drawing our Catmull-Rom curve.
 * */
var path = ['M', data[0].x, data[0].y];
path.push('R');
/*
 * We then iterate over all remaining points (all points except the first) and append their values
 * to our path array.
* */
for(var i = 1, num = data.length; i < num; i+=1) {
    path.push(data[i].x);
    path.push(data[i].y);
}
var curve = paper.path( path );

/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-3/19_catmull_rom
 * */


/************************************************************************************************
 * 4. Transformations and Event Handling
 * *********************************************************************************************/

/*
 * When you create an element in Raphaël, you are effectively creating a Document Object Model
 * (DOM) object. Like the DOM objects you are already familiar with elements drawn on to our 
 * canvas will trigger events when interacted with by a user. Raphaël provides a number of 
 * convenient, cross-browser methods for interacting with elements and also provides methods 
 * that facilitate the drag-and-drop functionality.
 *
 * Transformations are equally versatile: Raphaël gives us the ability to transform (translate, 
 * scale, and rotate) elements with ease using the concept of a transformation string. 
 * */

// 4.1 Basic transformations and event handling

/*
 * We perform transformations in Raphaël using the  transform method on elements, which accepts 
 * as an argument a transformation string. Transformation strings define a sequence of transformations 
 * to take place on a particular element.
 * */

// 4.1.1 Basic transformations

/*
 * Like a path string, a transformation string is composed of a number of commands defined in the order
 * in which they are to be interpreted. The syntax for the basic commands is as follows:
 *
 * ----------------------------------------------------------------------------------------
 *  Command         Parameters                      Example
 * ----------------------------------------------------------------------------------------
 *  T or t          x, y                            t 50, 100
 *  R or r          angle of clockwise rotation,    R 45, 0, 0
 *                  (rotation_point_x,
 *                  rotation_point_y)
 *  S or s          scale_x,                        S 2, 4.5, 75, 125
 *                  scale_y,
 *                  (scale_point_x,
 *                  scale_point_y)
 *                  or
 *                  scale_factor,
 *                  (scale_point_x,
 *                  scale_point_y)
 * ----------------------------------------------------------------------------------------
 *
 * As with a path string, transformation strings have uppercase and lowercase variants. 
 * The uppercase variant means that we transform, irrespective of the previous transformation, 
 * while the lowercase variant takes previous transformations into account.
 * */

// 4.1.1.1 Translation

var triangle = paper.path("M 150 20 l 100 160 l -200 0 z").attr({
    'stroke-dasharray': '- ',
    'stroke-width': 5
});
var triangleCopy = triangle.clone(); // Clones our object
triangleCopy.attr({
    'stroke-dasharray': ''
});
// We then perform a translation of 300px on the x-axis and 0px on the y-axis as follows:
triangleCopy.transform("T 300 0");
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/01_basic_transformations
 *
 * Note that while the  clone method is convenient, it is known to affect performance adversely 
 * when cloning multiple elements. When cloning multiple elements, creating a new element using 
 * the original path is advised. 
 * */

// 4.1.1.2 Rotation

/*
 * Creating another cloned triangle now and transforming it with the transformation string 
 * below gives us a triangle rotated 45 degrees clockwise about its own center point 
 * (the default when we do not specify a rotation point) after being translated 350px in x 
 * and -35px in y.
 * */

triangleCopy.transform("t 350 -35 r 45");
/*
 * 效果见： http://raphaeljsvectorgraphics.com/book/chapter-4/01_basic_transformations
 * */

// 4.1.1.3 Scaling

/*
 * Scaling can be performed either equally on all points about a scaling point or a factor
 * in x and y. The scaling for the "t 300 0 s 0.5" transformation scales all points by 0.5
 * times their original about the center point of the element.
 *
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/01_basic_transformations
 *
 * Scaling in x and y by the "t 310 0 s 1.2 0.5" transformation string scales the element 
 * 1.2 times in x and 0.5 times in y.
 * 
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/01_basic_transformations
 * */

// 4.1.2 Basic event handling

// 4.1.2.1 Registering basic event handlers

/*
 * We will demonstrate registering the double-click, mouse over, and mouse out event handling 
 * methods on a salinon shape. 
 * */

var salinon = paper.path([
                         'M', 100, 200,
                         'a', 150, 150, 0, 0, 1, 300, 0,
                         50, 50, 0, 0, 0, -100, 0,
                         50, 50, 0, 0, 1, -100, 0,
                         50, 50, 0, 0, 0, -100, 0
]);
salinon.mouseover(function() {
    this.transform('R 180');
});
salinon.dblclick(function() {
    this.transform('r 45');
});
salinon.mouseout(function() {
    this.transform('');
});
/*
 * 效果见： http://raphaeljsvectorgraphics.com/book/chapter-4/02_basic_event_handling
 *
 * Concerning the resetting of transformations, passing an empty string to the transform 
 * method has the effect of returning the shape to its original position.
 *
 * You will notice by running the previous code that the 45 degree rotation is performed 
 * relative to its initial position, not that defined by the 180 degrees rotation. This is 
 * because every invocation of the  transform method is relative to the original state of 
 * the element.
 *
 * If, however, we want to transform an element from its current state—that resulting from 
 * the previous invocation of  transform —we can prefix our transformation commands with 
 * an ellipsis(省略号) in order to append a new transformation.
 * */

salinon.click(function() {
    this.transform('t 300 0 R 180');
});
salinon.dblclick(function() {
    this.transform('...t 200 0 r 45');
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/03_transformation_ellipsis
* */

// 4.1.2.2 Unregistering basic event handlers

/*
 * The unregistering event handlers are methods of the element to which you have
 * registered event handlers and accepted as a parameter the event handling function.
 * */

var square = paper.rect(50, 50, 100, 100);
var clickHandler = function() {
    this.transform('...r 15');
};
square.click(clickHandler);
circle.dblclick(function() {
    square.unclick(clickHandler);
}

/*
 * You can register and unregister multiple event handlers for an event on a single element. 
 * The handlers are run in the order in which they're defined.
 * */


// 4.2 Working with matrices

// 4.2.1 Transformation matrices

/*
 * Transformations in Raphaël are known as affine transformations. The idea is that we treat 
 * every point in 2D space as a point in 3D space, which allows us to represent a transformation 
 * using matrices. The 3D point is fixed at 1 so that an (x, y) point is represented as (x, y, 1), 
 * that is, it does not vary in the third dimension.
 * */

// 4.2.1.1 Using transformation matrices

/*
 * When creating transformations, you can pass matrix parameters directly to a transformation string 
 * using the syntax  "M a, b, c, d, e, f" . This has the effect of applying a transformation matrix 
 * to every point on an element.
 * */

/*该部分内容（根据矩阵做图形变换）可以单独翻译出来。
 * */

// 4.3 The drag-and-drop functionality

// 4.3.1 The Element.drag() method

/*
 * The  drag method of an element has the following syntax:
 *
 *      Element.drag(
 *          onmove, onstart, onend, [mcontext], [scontext], [econtext]
 *      )
 *
 * The "onmove", "onstart", and "onend" functions are callback functions invoked during the life cycle 
 * of a dragged element, while "mcontext", "scontext", and "econtext" define the "this" variable in 
 * the scope of these functions (defaulting to the element that is being dragged).
 * 
 * */

// 4.3.2 The onstart event handler

// 4.3.3 The onend event handler

// 4.3.4 The onmove event handler

/*
 * The  onmove event handler is called every time an element is moved during dragging. It has the 
 * parameters "dx" and "dy" that describe the amount by which the element has been dragged in x 
 * and y respectively.
 * */

// 4.3.4.1 Dragging by example

/*
 * We first define our element and keep a reference to its start x and y positions in the "onstart" 
 * event handler. To highlight that our element is in a "drag" state, we also paint it pink. In our 
 * "onend" event handler, we reset the fill to be black to indicate that dragging has finished.
 * */

Raphael('my-canvas', 800, 400, function() {
    var paper = this;
    
    var square = paper.rect(100, 100, 100, 100).attr('fill', '#000');

    var startX, startY;

    function onstart() {
        startX = this.attr('x');
        startY = this.attr('y');

        this.attr('fill', 'pink');
    }

    function onend() {
        this.attr('fill', '#000');
    }

    function onmove(dx, dy) {
        this.attr({
            x: startX + dx,
            y: startY + dy
        });
    }

    square.drag(onmove, onstart, onend);
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/14_drag_drop_01
 * */

// 4.3.5 Dropping elements

/*
 * At the end of dragging an element, we can perform checks to see where it has ended up relative to 
 * other elements. A "drop" is essentially a check to see whether our element falls within some 
 * particular set of bounds.
 * */

// 4.3.5.1 Bounding box overlapping(范围边框(bounding)有重合)

/*
 * Every element has a bounding box that defines the smallest rectangular region containing all points
 * of an element. By checking to see whether two bounding boxes overlap we can determine whether or not
 * an element was "dropped" on to another.
 * */

Raphael('my-canvas', 800, 400, function() {
    var paper = this;

    var target = paper.rect(400, 100, 200, 200).attr('fill', '#ddd');
    var square = paper.rect(100, 100, 100, 100).attr('fill', '#000');

    var startX, startY;

    function onstart() {
        startX = this.attr('x');
        startY = this.attr('y');

        this.attr('fill', 'pink');
    }

    function onend() {
        var bBox = this.getBBox(),
        targetBBox = target.getBBox();

        if(Raphael.isBBoxIntersect(bBox, targetBBox)) {
            this.undrag();
            this.attr({
                x: 450,
                y: 150
            });
        }
    }

    function onmove(dx, dy) {
        this.attr({
            x: startX + dx,
            y: startY + dy
        });
    }

    square.drag(onmove, onstart, onend);
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/15_drag_drop_02
 *
 * This time, in our "onend" event handler, we get the bounding boxes of each of our square and target element
 * using the "getBBox" method and then check whether or not the elements overlap using "isBBoxIntersect". 
 * */

// 4.3.5.2 Bounding box inside bounding box(一个物体的范围边框完全在另一个物体的范围边框之内)

/*
 * While the "isBBoxIntersect" method is convenient, we sometimes need to know whether or not all points on 
 * an element are inside another.
 *
 * we could check to see whether the top-left vertex and bottom-right vertex of our square's bounding box 
 * fall within the target bounding box using the "isPointInsideBBox" method.
 * 
 * */

function onend() {
    var targetBBox = target.getBBox();
    var topLeftVertex = {
        x: this.attr('x'),
        y: this.attr('y')
    };
    var bottomRightVertex = {
        x: this.attr('x') + this.attr('width'),
        y: this.attr('y') + this.attr('height')
    };
    var point1InsideBox = Raphael.isPointInsideBBox(
        targetBBox, topLeftVertex.x, topLeftVertex.y
    );
    var point2InsideBox = Raphael.isPointInsideBBox(
        targetBBox, bottomRightVertex.x, bottomRightVertex.y
    );
    if(point1InsideBox && point2InsideBox) {
        this.undrag();
        this.attr({ x: 450, y: 150 });
    }
}
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-4/16_drag_drop_03
 * */


/***********************************************************************************************************
 * 5. Vector Animation
 * ********************************************************************************************************/

/*
 * Animation affords us the ability to change graphics with regard to time, that is, we can modify the 
 * attributes of a vector graphic over some non-zero time interval.
 * 
 * */

// 5.1 Basic animation

/*
 * Animation is accomplished using the "animate" method of an element. The method takes the following parameters 
 * in the order that they're defined.
 *
 * -----------------------------------------------------------------------------------------
 *  Parameter               Type                    Description
 * -----------------------------------------------------------------------------------------
 *  attributes              Object                  Key-value pair attributes as per the 
 *                                                  Element.attr() method
 *  duration                Number                  The number of milliseconds that the
 *                                                  duration should last for
 *  easing(optional)        String                  A string describing the rate of change
 *                                                  of an attribute with regard to time
 *  callback(optional)      Function                A function that is executed at the point
 *                                                  at which the animation ends
 * ------------------------------------------------------------------------------------------
 * */

var circle = paper.circle(100, 100, 50).attr({fill: 'green'});
circle.animate({
    cx: 500,
    r: 15
}, 1000);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/01_animation_01
 * */

var rectangle = paper.rect(100, 50, 20, 50).attr({
    fill: '#345'
});
rectangle.animate({
    opacity: 0.6,
    x: 400,
    y: 100,
    width: 100,
    'stroke-width': 10
}, 1000);
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/02_animation_02
 * */

// 5.2 Animating paths

/*
 * While the basic shapes have intrinsic x and y or  cx and  cy attributes and width and height, paths do not
 * and so we will animate custom paths from one path to another.
 * */

var star = paper.path(
    'M 100,40 40,210 190,90 10,90 160,210 z'
);
var square = paper.rect(500, 100, 50, 50).attr({
    'fill': '#09c', cursor: 'pointer'
});
square.click(function() {
    star.animate({
        path: [
            'M', 100, 180,
            'a', 140, 140, 0, 0, 1, 280, 0,
            90, 90, 0, 0, 0, -180, 0,
            50, 50, 0, 0, 0, -100, 0
        ]
    }, 1000);
});

/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/03_animation_03
 * */

var pathStart = [
    'M', 50, 250,
    'R', 100, 100, 150, 150, 200, 140, 250, 200, 300, 80,
    350, 130, 400, 250,
    'H', 50,
    'z'
];
var pathEnd = [
    'M', 50, 250,
    'R', 100, 130, 150, 220, 200, 200, 250, 100, 300, 200,
    350, 180, 400, 250,
    'H', 50,
    'z'
];
var curve = paper.path(pathStart).attr({
    'stroke-width': 0,
    'stroke-linejoin': 'round'
    'fill': 'green'
});
square.click(function() {
    curve.animate({
        path: pathEnd
    }, 500);
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/04_animation_04
 * */

// 5.3 Animation easing(动画缓冲 / 缓动函数)

/*
 * "Easing" describes how the value of an attribute varies with regard to time. By default, the value of an attribute 
 * changes consistently—that is, linearly—over the course of an animation but by specifying a particular easing type, 
 * we can change the way in which the attribute is animated.
 *
 * For each easing type, the rate at which the attribute changes varies along the graph in the time axis. Each easing 
 * type can be described as such:
 *  - Linear: The value varies consistently from its start value to its end value over the course of the animation.
 *  - Ease Out: The value increases quickly towards its end point before slowing down towards the end of the animation.
 *  - Ease In Out: The value decreases slowly at first and then increases quickly  before finally slowing down to its 
 *                  end point towards the end of the animation. 
 * */

// 5.3.1 Built-in easing formulas

// 演示：http://raphaeljs.com/easing.html

// consider applying an easing type of  'bounce' to our Catmull-Rom path animation curve:

square.click(function() {
    curve.animate({
        path: pathEnd
    }, 500, 'bounce');
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/05_animation_05
 * */

// 5.3.2 Custom easing using the cubic Bezier format

/*
 * The format for CSS3 transitions describing animation easing can be used to define custom easing paths in Raphaël. 
 * The syntax is  'cubic-bezier(point1_x, point1_y, point2_x, point2_y)' , where each parameter defines the x and y
 * positions of anchor points describing a cubic Bézier curve from (0, 0) to (1,1) in attribute value and time.
 * */


// 5.4 Animating transformations

/*
 * As with paths, an element's transform is an attribute on the element meaning we can animate in the same manner.
 * */

square.click(function() {
    this.animate({
        transform: ['...r 45']
    }, 300);
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/07_animation_07
 * */

var anim = Raphael.animation({
    transform: [
        '...', 'M', 1, 0, Math.tan(Raphael.rad(5)), 1, 0, 0
    ]
}, 300);
square.click(function() {
    this.animate(anim);
});
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/08_animation_08
 * */


// 5.5 Animation using custom attributes

// 5.5.1 Custom attributes

/*
 * A custom attribute is a custom-defined function that returns a set of attributes to be applied to an element. 
 * It can be thought of as a helper function for which existing attributes are derived based on calculation. A 
 * custom attribute is  defined as an attribute of the  customAttributes namespace as follows:
 *
 * Paper.customAttributes.yourAttribute = function(a1, a2, ...){};
 * 
 * */

var paper = Raphael('my-canvas', 600, 300);
var data = [
    {
        name: 'Taiwan',
        population: 0.1,
        density: 1
    },
    {
        name: 'South Korea',
        population: 0.32,
        density: 0.5
    },
    {
        name: 'Netherlands',
        population: 0.05,
        density: 0.22
    },
    {
        name: 'Belgium',
        population: 0,
        density: 0.07
    },
    {
        name: 'Japan',
        population: 1,
        density: 0
    }
];

paper.customAttributes.popDensity = function(population, density) {
    var radius = 25 + (25 * population),
        fillColor = 'hsb(' + 0.3 * (1 - density) + ', 1, 0.85)';

    return {
        fill: fillColor,
        r: radius
    };
};

var currentX = 70;
for(var i = 0, ii = data.length; i < ii; i+=1) {
    var country = data[i];
    // -->
    paper.circle(currentX, 150, 50).attr({
        popDensity: [country.population, country.density],
        'stroke-width': 4
    });
    // <--
    paper.text(currentX, 225, country.name).attr({'font-size': 14});

    currentX += 100;
}

/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/09_animation_09
 *
 * 若将 paper.circle的调用替换成如下代码：
* */

var circle = paper.circle(currentX, 150, 50).attr({
    popDensity: [0, 0],
    'stroke-width': 4
});

circle.animate({
    popDensity: [country.population, country.density]
}, 1000, 'easeOut');
/*
 * 则效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/10_animation_10
* */

// 5.5.2 Animation along a path

var paper = Raphael('my-canvas', 600, 300);

var path = paper.path(
    ['M', 100, 100, 
    'C', 100, 0, 400, 200, 400, 100,
    'S', 100, 200, 100, 100,
    'z'
    ]
).attr({'stroke-width': 2});
var circle = paper.circle(0, 0, 13).attr({fill: '#09c', cursor: 'pointer'});

var pathLength = path.getTotalLength();
paper.customAttributes.pathFactor = function(distance) {
    var point = path.getPointAtLength(distance * pathLength);
    var dx = point.x,
        dy = point.y;
    return {
        transform: ['T', dx, dy]
    };
};

circle.attr({pathFactor: 0});

function runloop() {
    circle.animate({pathFactor: 1}, 4000, function() {
        this.attr({pathFactor: 0}); // Reset
        setTimeout(runloop);
    });
    circle.unclick().click(function() {
        this.pause();
    });
    circle.undblclick().dblclick(function() {
        this.resume();
    });
};
runloop();
/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/11_animation_11
* */

// 5.5.2.1 Pausing and resuming animation

/*
 * 效果见：http://raphaeljsvectorgraphics.com/book/chapter-5/11_animation_11
 * */

/********************************************************************************************************************
 * 6. Working with Existing SVGs
 * *****************************************************************************************************************/


// 6.1 Inkscape


// 6.2 Inspecting paths


// 6.3 SVG to Raphael conversion tools

// 6.3.1 Ready Set Raphael

/*
 * http://www.readysetraphael.com/
 * */

// 6.3.2 Other converters

/*
 * Charles Thomas's SVG to HTML converter ( http://www.irunmywebsite.com/raphael/SVGTOHTML_LIVE.php ) converts all 
 * primitive shapes to paths and ensures that all paths use absolute coordinates while the converter at 
 * http://toki-woki.net/p/SVG2RaphaelJS/ is fast and lightweight.
 * */


// 6.4 Choropleth maps

/*
 * Choropleth maps are maps that show some particular area or region with an associated measurement or statistic. 
 * */

// 6.4.1 Creating choropleth maps

/*
 * Often when you need to associate data with some geographical region or area, the best approach is to utilize 
 * an existing map in SVG format that you can then tailor to your needs (manually by modifying the raw XML or 
 * using a graphics editor such as Inkscape). 
 * */

// 6.5 Open source SVGs

/*
 * There are a number of SVGs available via the Open Clip Art Library at http://openclipart.org . 
 * */


/************************************************************************************************************************
 * 7. Creating a Suite of Social Media Visualizations
 ***********************************************************************************************************************/
