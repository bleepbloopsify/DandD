var character = {};
var retrieveCharacter = function(){
  urlpieces = window.location.href.split('/');
  charid = urlpieces[urlpieces.length - 1];
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
	var element = $('<div/>');
	element.html(value+": "+character[value]);
	console.log(value);
	if(value == "idnum"){
	    console.log(value);
	    element.prependTo("#right-col");
	}
	else if(value != "charname" && character[value]){
	    console.log(value);
	    element.prependTo("#left-col");
	}

    }
};


$(document).ready(function(){
  retrieveCharacter();
});
