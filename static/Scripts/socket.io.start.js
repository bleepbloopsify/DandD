// var socket = io.connect("http://localhost:8000/gameinfo");
//
// socket.on('connect', function(){
//   socket.emit('connected', {data: "Connection Received!"} );
// });
//
// socket.on('blah', function(data){
//   console.log(data['data']);
// });

var socket = io();

socket.emit('test', {data:"lol", room:"12345"});

$(document).ready(function(){
  $("#button").click(function(){
    console.log("hhi");
    socket.emit('clicked!!!', {data:"pls"});
  });
});
