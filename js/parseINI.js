/*
格式：
searchengine=http://www.google.com/search?q=$1
spitefulness=9.7

; comments are preceded by a semicolon...
; these are sections, concerning individual enemies
[larry]
fullname=Larry Doe
type=kindergarten bully
website=http://www.geocities.com/CapeCanaveral/11451

[gargamel]
fullname=Gargamel
type=evil sorcerer
outputdir=/home/marijn/enemies/gargamel
 * */
function splitLines(string){
    return string.split(/\r?\n/);
}

function forEach(array, action){
    for(var i = 0; i < array.length; i++)
        action(array[i]);
}

function parseINI(string){
    var lines = splitLines(string);
    var categories = [];

    function newCategory(name){
        var cat = {name: name, fields: []};
        categories.push(cat);
        return cat;
    }
    var currentCategory = newCategory("TOP");

    forEach(lines, function(line){
        var match;
        if(/^\s*(;.*)?$/.test(line))
            return;
        else if(match = line.match(/^\[(.*)\]$/))
            currentCategory = newCategory(match[1]);
        else if(match = line.match(/^(\w+)=(.*)$/))
            currentCategory.fields.push({name: match[1], value: match[2]});
        else
            throw new Error("Line '" + line + "' is invalid.");
    });

    return categories;
}
