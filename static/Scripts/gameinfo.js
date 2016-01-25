var game = {};

var closewindow = function(){
  $(this).parents("div:first").css("visibility", "hidden");
};

var openwindow = function(){
  $("#" + $(this).attr("for")).css("visibility", "inherit");
};

var retrieveGame = function(){
    urlpieces = window.location.href.split('/');
    gameid = urlpieces[urlpieces.length - 1];
    $.ajax({
	     url:"/getgame/" + gameid,
       method:"GET",
       success:function(data){
         game = JSON.parse(data);
         sortGame();
         populateInfo();
      }
    });
};

var sortGame= function(){
  game['playerlist'] = [];
  for (var valuekey in game){
    if (valuekey != "playerlist" && valuekey.split('[')[0] == "playerlist"){
      game['playerlist'].push(game[valuekey]);
      delete game[valuekey];
    }
  }
};

var populateInfo = function(){
    addName();
    parseGame();
    addPlayers();
    setupFields();
};

var addName = function(){
    name = game['name'] || game['host'] + "'s Game" || "Game";
    var element = $("<div/>", {id:"displaygamename"});
    element.html(name);
    element.prependTo(".body");
}

var parseGame = function(){
    for (var fieldid in game){
    	if (fieldid && fieldid != "name" && fieldid != "playerlist" && fieldid != "id" && fieldid != 'user' && fieldid != 'host'){
  	    var element = $('<div/>');
  	    element.html(fieldid+": "+game[fieldid]);
        element.attr("class", "gamefield");
        element.attr("for", fieldid);
  	    element.appendTo("#gamelist");
      }
    }
}

var setupFields = function(){
  $(".gamefield").each(addfieldedit);
  $(".gamefield").each(addremovefield);
}

var addfieldedit = function(){
  var input = $("<input/>");
  input.attr("type", "text");
  input.attr('id', $(this).attr("for"));
  $(this).append(input);
}

var editchar = function(){
  var char = $(this).parent().attr("for`");
};

var addremovefield = function(){
  var closebtn = $('<button type="button"/>');
  closebtn.attr("class", "closebtn");
  closebtn.html("X");
  closebtn.click(removefield);
  $(this).append(closebtn);
};

var removefield = function(){
  var fore = $(this).parent().attr("for");
  delete game[fore]
  $(this).parent().remove();
}

var addPlayers = function(){
  game['playerlist'].forEach(retrievechar);
};

charlist = []
var retrievechar = function(data){
  var char = {};
  $.ajax({
    url:"/charinfo/"+data,
    method:"POST",
    success:function(res){
      console.log(res);
      char = JSON.parse(res);
      charlist.push(char);
      if (data >= game['playerlist'].length){
        charlist.forEach(function(data){
          var element = $("<li/>");
          element.html(data['charname']);
          element.attr("for",data['id']);
          element.click(openwindow);
          addeditform(element, data);
          element.appendTo("#gameplayers");
        });
      }
    }
  });
};
var addeditform = function(element, data){
  var container = $('<div class="container"/>');
  container.attr("id", data['id']);
};

var updategame = function(){
  if ($(this).val() && $(this).parent()){
    game[$(this).parent().attr("for")] = $(this).val();
  }
}

var sendgame = function(){
  $(".gamefield input").each(updategame);
  $.ajax({
    url:"/gameinfo/" + game['id'],
    method:'POST',
    data:game,
    success:function(data){
      $("#gamelist, #gameplayers, #displaygamename").html("");
      retrieveGame();
    }
  });
}

var updatefield = function(){
  $(this).html(game[$(this).attr("for")])
};


$(document).ready(function(){
    $(".openwindowbtn").click(openwindow);
    $(".closewindowbtn").click(closewindow);
    $("#savegame").click(sendgame);
    retrieveGame();
})
