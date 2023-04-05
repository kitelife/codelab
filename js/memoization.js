// 函数属性 --- 备忘（memoization）模式

var myFunc = function (param) {
    if (!myFunc.cache[param]) {
        var result = {};
        // ... 开销很大的操作 ...
        myFunc.cache[param] = result;
    }
    return myFunc.cache[param];
};

// 缓存存储
myFunc.cache = {};

// 上面的代码假定该函数只需要一个参数param，并且它是一个基本数据类型（比如字符串类型）。
// 如果有更多以及更复杂的参数，对此的通用解决方案是将它们序列化。例如，可以将参数对象
// 序列化为一个JSON字符串，并使用该字符串作为cache对象的键：

var myFunc = function () {
    var cachekey = JSON.stringify(Array.prototype.slice.call(arguments)),
        result;

    if (!myFunc.cache[cachekey]) {
        result = {};
        // ... 开销很大的操作 ...
        myFunc.cache[cachekey] = result;
    }
    return myFunc.cache[cachekey];
};

myFunc.cache = {};
