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
};

var addname = function(){
  var element = $('<div/>', {class:"charname"});
  element.html(character['charname']);
  element.prependTo(".body");
};


$(document).ready(function(){
    retrieveCharacter();
});
