var closewindow = function(){
  $("#creategameform").css("visibility", "hidden");
};

var openwindow = function(){
  $("#creategameform").css("visibility", "visible");
};

var populateList = function(){
  for (var gamekey in games){
    
  }
};

var sendgame = function(){
  var inputs = {};
  $("#creatinggameform input").each( function(){
    inputs[ $(this).attr( "id" ) ] = $(this).val();
  });
  inputs.remove(["_id"])
  $.ajax({
    url:"/creategame",
    method:"POST",
    data: inputs ,
    success: function(data){
      window.location.href = "/gameinfo/" + data;
    }
  })
};

var attachListeners = function(){
  $("#creategame").click( openwindow );
  $(".closewindow").click( closewindow );
  $("#create").click( sendgame );
};

$(document).ready(function(){
  attachListeners();
});
