var days = (function(){
    var names = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"];
    return {
        getDayName: function(number) {return names[number];},
        getDayNumber: function(name) {
            for(var number = 0; number < names.length; number++){
                if(names[number] == name) return number;
            }
        }
    };
})();

days.getDayNumber("Wednesday");
