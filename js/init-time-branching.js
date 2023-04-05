var utils = {
    addListener: function (el, type, fn) {
        if (typeof window.addEventListener === 'function') {
            el.addEventListener(type, fn, false);
        } else if (typeof document.attachEvent === 'function') { // IE
            el.attachEvent('on' + type, fn);
        } else { // 更早版本的浏览器
            el['on' + type] = fn;
        }
    },
    removeListener: function(el, type, fn) {
        if (typeof window.removeEventListener === 'function') {
            el.removeEventListener(type, fn, false);
        } else if (typeof document.detachEvent === 'function') {
            el.detachEvent('on' + type, fn);
        } else {
            el['on' + type] = null;
        }
    }
}

//
//

var utils = {
    addListener: null,
    removeListener: null
}

if (typeof window.addEventListener === 'function') {
    utils.addListener = function (el, type, fn) {
        el.addEventListener(type, fn, false);
    };
    utils.removeListener = function (el, type, fn) {
        el.removeEventListener(type, fn, false);
    };
} else if (typeof document.attachEvent === 'function') {
    utils.addListener = function (el, type, fn) {
        el.attachEvent('on' + type, fn);
    };
    utils.removeListener = function (el, type, fn) {
        el.detachEvent('on' + type, fn);
    };
} else {
    utils.addListener = function (el, type, fn) {
        el['on' + type] = fn;
    };
    utils.removeListener = function (el, type, fn) {
        el['on' + type] = null;
    };
}
