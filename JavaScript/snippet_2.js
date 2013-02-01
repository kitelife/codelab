function positionOf(element, array, compare, start, end){
    if(start == null) start = 0;
    if(end == null) end = array.length;
    for(; start < end; start++){
        var current = array[start];
        if(compare ? compare(element, current) : element == current) return start;
    }
}

positionOf(2, [1, 2, 3, 4, 3, 2, 1], null, 3, 6);

// args里的可选参数{compare, start, end}
function positionOf(element, array, args){
    args = args || {};
    var start = (args.start == null) ? 0 : args.start,
        end = (args.end == null) ? array.length : args.end,
        compare = args.compare;
    for(; start < end; start++){
        var current = array[start];
        if(compare ? compare(element, current) : element == current) return start;
    }
}

positionOf(2, [1, 2, 3, 4, 3, 2, 1], {start: 3, end: 6});
