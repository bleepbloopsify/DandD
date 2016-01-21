var character = {};
var retrieveCharacter = function(){
  urlpieces = window.location.href.split('/');
  charid = urlpieces[urlpieces.length - 1];
    console.log(charid);
    $.ajax({
    	url:"/charinfo/" + charid,
    	method:"POST",
    	success: function(data){
    	    character = JSON.parse(data);
            populateInfo();
    	}
  });
};

var populateInfo = function(){
    addname();
    addfields();
};

var addname = function(){
    var element = $('<div/>', {id:"displaycharname"});
    element.html(character['charname']);
    element.prependTo(".body");

};

var addfields = function(){
    for (var value in character){
	if(value != "idnum" && value != "charname"){
	    var element = $('<div/>');
	    element.html(value+": "+character[value]);
	    element.prependTo("#left-col");
	};
    };
};


$(document).ready(function(){
    retrieveCharacter();
});
