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


$(document).ready(function(){
    retrieveCharacter();
});
