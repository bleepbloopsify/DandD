var game = {};
var retrieveGame = function(){
  urlpieces = window.location.href.split('/');
  gameid = urlpieces[urlpieces.length - 1];
  console.log(gameid);
  $.ajax({
    url:"/getgame/" + gameid,
    method:"GET",
    success:function(data){
      game = JSON.parse(data);
      populateInfo();
    }
  })
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
  retrieveGame();
})
