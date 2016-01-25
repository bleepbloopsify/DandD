var game = {};

var closewindow = function(){
  $("button[for=" + $(this).parents("div:first").attr("id") +"]").css("visibility", "inherit");
  $(this).parents("div:first").css("visibility", "hidden");
};

var openwindow = function(){
  $("#" + $(this).attr("for")).css("visibility", "inherit");
  $(this).css("visibility", "hidden");
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
    })
};

var sortGame= function(){
  for (var valuekey in game){
    if (valuekey.split('[')[0] == "playerlist"){
      game['playerlist'].append(game.pop(valuekey));
    }
  }
};

var populateInfo = function(){
    addName();
    parseGame();
};

var addName = function(){
    name = game['name'] || game['host'] || "Game";
    var element = $("<div/>", {id:"displaygamename"});
    element.html(name);
    element.prependTo(".body");
}

var parseGame = function(){
  for (var fieldid in game){
    console.log(fieldid);
    var element = $('<div/>');
    console.log(element);
    element.attr('id', fieldid);
    element.html(game[fieldid]);
    element.appendTo("#gamelist");
  }
}

$(document).ready(function(){
    $(".openwindowbtn").click(openwindow);
    $(".closewindowbtn").click(closewindow);
    retrieveGame();
})
