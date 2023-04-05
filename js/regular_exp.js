"doubledare".search(/le/);

var slash = /\//;
"AC/DC".search(slash);

var digitSurroundedBySpace = /\s\d\s/;
"1a 2 3d".search(digitSurroundedBySpace);

var notABC = /[^ABC]/;
"ABCBACCBBADABC".search(notABC);

var datePattern = /\d\d\/\d\d\/\d\d\d\d/;
"born 15/11/2003 (mother Spot): White Fang".search(datePattern);

/a/.test("blah");

/^a$/.test("blah");

// 转义字符\b可以匹配“单词边界”---它可以是标点符号、空格、字符的开头或结尾
/cat/.test("concatenate"); // -> true
/\bcat\b/.test("concatenate"); // -> false

// 在正则表达式里，重复表示子模式也是可以的。在元素后面跟一个星号(*)表示可以重复匹配任意次数（包括零次）;元素后面跟一个加号（+）要求至少要匹配一次；元素后面跟一个问好（?）表示该元素可选（它可能出现零次或一次）。
var parenthethicText = /\(.*\)/;
"Its (the sloth's) claws were gigantic!".search(parenthethicText);

// 在必要的时候，可以使用花括号来指定一个元素可能发生的次数。
var datePattern = /\d{1, 2}\/\d\d?\/\d{4}/;
"born 15/11/2003 (mother Spot): White Fang".search(datePattern);

//子表达式分组
//
var cartoonCrying = /boo(hoo+)+/i;
cartoonCrying.test("Boohoooohoohooo");

// 多选一
// 对于更高级的“分支”模式，可以使用竖线（|）表示允许模式在多个元素中选择一个
var holyCow = /\b(sacred|holy) (cow|bovine|bull|taurus)\b/i;
holyCow.test("Sacred bovine!");

// 字符串有一个match方法，接收正则表达式作为参数。如果匹配失败就返回null；如果匹配成功则返回匹配的字符串组成的数组。
"No".match(/yes/i); // null
"... yes".match(/yes/i);    // ["yes"]
"Giant Ape".match(/giant (\w+)/i);  // ["Giant Ape", "Ape"]

function extractDate(string){
    var found = string.match(/\b(\d\d?)\/(\d\d?)\/(\d{4})\b/);
    if(found == null)
        throw new Error("No date found in '" + string + "'.");
    return new Date(Number(found[3]), Number(found[2]) - 1, Number(found[1]));
}

// 字符串值的replace方法可以接收一个正则表达式作为其第一个参数。
"Borobudur".replace(/[ou]/g, "a");
// -> "Barabadar"
// 请注意，正则表达式后面的字符g代表“全局”，这意味着匹配该模式的字符的每个部分都应该被替换掉。当省略g时，只有第一个字符o被替换掉，这是一种常见的错误。
