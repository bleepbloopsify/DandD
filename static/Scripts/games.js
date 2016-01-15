var closewindow = function(){
  $("#creategameform").css("visibility", "hidden");
};

var openwindow = function(){
  $("#creategameform").css("visibility", "visible");
};

var games = {};
var retrievegame = function(){
  $.ajax({
    url:"/getgame",
    method:"POST",
    success:function(data){
      games = JSON.parse(data);
    }
  });
};

var populateList = function(){
  for (var gamekey in games){
    game = games[gamekey];
    var element = $("<li/>", {"id":game['idnum'], "class":"game"});
    element.html(game['name']);
    element.on('mouseover', showDescript);
    element.on('mouseout', hideDescript);
    element.appendTo("#gametable");
  }
};

var creategame = function(){
  var inputs = {};
  $("#creatinggameform input").each( function(){
    inputs[ $(this).attr( "id" ) ] = $(this).val();
  });
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
  $("#createbtn").click( creategame );
};

$(document).ready(function(){
  attachListeners();
});
