var closewindow = function(){
  $("#creategameform").css("visibility", "hidden");
};

var openwindow = function(){
  $("#creategameform").css("visibility", "visible");
};



var sendgame = function(){
  var inputs = {};
  $("#creatinggameform input").each( function(){
    inputs[ $(this).attr( "id" ) ] = $(this).val();
  });

  $.ajax({
    url:"/creategame",
    method:"POST",
    data: inputs ,
    success: function(data){
      console.log(data);
      console.log("yay");
      // window.location.href = "/gameinfo/" + data;
    }
  })
};

var attachListeners = function(){
  $("#creategame").click( openwindow );
  $("#closegamewindow").click( closewindow );
  $("#create").click( sendgame );
};

$(document).ready(function(){
  attachListeners();
});
