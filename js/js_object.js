function makePerson(first, last) {
    return {
        first: first,
        last: last,
        fullName: function() {
            return this.first + ' ' + this.last;
        },
        fullNameReversed: function() {
            return this.last + ', ' + this.first;
        }
    }
}

/*
> s = makePerson("Simon", "Willison")
> s.fullName()
Simon Willison
> s.fullNameReversed()
Willison, Simon
*/

/**********************************/
function Person(first, last) {
    this.first = first;
    this.last = last;
    this.fullName = function() {
        return this.first + ' ' + this.last;
    }
    this.fullNameReversed = function() {
        return this.last + ', ' + this.first;
    }
}

var s = new Person("Simon", "Willison");

/*
 * Our person objects are getting better, 
 * but there are still some ugly edges to them.
 * Every time we create a person object we are creating two brand new function objects within it
 * wouldn't it be better if this code was shared?
*/
function personFullName() {
    return this.first + ' ' + this.last;
}

function personFullNameReversed() {
    return this.last + ', ' + this.first;
}

function Person(first, last) {
    this.first = first;
    this.last = last;
    this.fullName = personFullName;
    this.fullNameReversed = personFullNameReversed;
}

/*
 * That's better: we are creating the method functions only once,
 * and assigning references to them inside the constructor. 
 * Can we do any better than that? The answer is yes:
 * */

function Person(first, last) {
    this.first = first;
    this.last = last;
}

Person.prototype.fullName = function() {
    return this.first + ' ' + this.last;
}
Person.prototype.fullNameReversed = function() {
    return this.last + ', ' + this.first;
}
/*
 * Person.prototype is an object shared by all instances of Person.
 * It forms part of a lookup chain (that has a special name, "prototype chain"):
 * any time you attempt to access a property of Person that isn't set, 
 * JavaScript will check Person.prototype to see if that property exists there instead. 
 * As a result, anything assigned to Person.prototype becomes available to all instances of that constructor via the this object.
 * */
