var closewindow = function(){
  $("button[for=" + $(this).parents("div:first").attr("id") +"]").css("visibility", "inherit");
  $(this).parents("div:first").css("visibility", "hidden");
};

var openwindow = function(){
  $("#" + $(this).attr("for")).css("visibility", "visible");
  $(this).css("visibility", "hidden");
};

var games = {};
var retrievegame = function(){
  $.ajax({
    url:"/getgame",
    method:"GET",
    success:function(data){
      games = JSON.parse(data);
      populateList();
    }
  });
};

var populateList = function(){
  for (var gamekey in games){
    game = games[gamekey];
    var element = $("<li/>", {"id":game['idnum'], "class":"game"});
    element.html(game['name']);
    element.appendTo("#gametable");
  }
  $("#gametable li").last().css("border-bottom","None");
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

var addField = function(){
  var div = $('<div class="form-group">');
  var label=$('<label class="control-label col-sm-2">');
  label.html($("#fieldname").val() + ":");
  label.attr("for", $("#fieldname").val());
  div.append(label);
  switch ($("#fieldtype").val()) {
    case "text":
      var indiv = $('<div class="col-sm-3">');
      var input = $('<input type="text" class="form-control">');
      input.attr("id", $("#fieldname").val());
      indiv.append(input);
      div.append(indiv);
      break;
    case "textarea":
      var indiv = $('<div class="col-sm-6">');
      var input = $('<textarea rows="5" class="form-control">');
      input.attr("id", $("#fieldname").val());
      indiv.append(input);
      div.append(indiv);
      break;
  }
  var button = $('<button>X</button>');
  div.appendTo("#creatinggameform");
  $("#addfieldform input").val("");
}

var attachListeners = function(){
  $(".openwindowbtn").click( openwindow );
  $(".closewindowbtn").click( closewindow );
  $("#createbtn").click( creategame );
  $("#createfield").click( addField );
};

$(document).ready(function(){
  attachListeners();
  retrievegame();
});
