var game = {};
var retrieveGame = function(){
  urlpieces = window.location.href.split('/');
  gameid = urlpieces[urlpieces.length - 1];
  $.ajax({
    url:"/gameinfo/" + gameid,
    method:"POST",
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
