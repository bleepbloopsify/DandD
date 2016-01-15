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
	}
  });
};

$(document).ready(function(){
    retrieveCharacter();
});

var populateInfo = function populateInfo(){
    
};
