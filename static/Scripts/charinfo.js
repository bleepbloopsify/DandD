var character = {};
var retrieveCharacter = function(){
  urlpieces = window.location.href.split('/');
  charid = urlpieces[urlpieces.length - 1];
  $.ajax({
    url:"/charinfo/" + charid,
    method:"POST",
    success: function(data){
      character = JSON.parse(data);
    }
  });
};
