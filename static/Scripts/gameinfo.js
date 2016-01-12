var socket = io();
var Game

var connect = function(){
  socket.emit('connected', {data:user})
};
socket.on('connect', connect);

var retrieveGame = function(){
  Game = socket.emit('retrieve', {id: idnum});
}

$(document).ready(function(){

});
