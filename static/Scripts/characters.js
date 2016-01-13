var closewindow = function(){
  $("#createcharform").css("visibility", "hidden");
};

var openwindow = function(){
  $("#createcharform").css("visibility", "visible");
};

var sendgame = function(){
  var inputs = {};
  $("#creatingcharform input").each( function(){
    inputs[ $(this).attr( "id" ) ] = $(this).val();
  });
  console.log(inputs);
  $.ajax({
    url:"/characters",
    method:"POST",
    data: inputs ,
    success: function(data){
      console.log(data);
      window.location.href = "/charinfo/" + data;
    }
  });
};


$(document).ready( function(){
  $("#create_char").click(openwindow);
  $(".closewindow").click(closewindow);
  $("#createchar").click(sendgame);
  populateList();
});


var populateList = function(){
  for (var charkey in sentChars){
    char = sentChars[charkey];
    var element = $("<li/>", {"id":char["idnum"], "class":"char"});
    element.html(char["name"]);
    element.on('mouseover', showDescript);
    element.on('mouseout', hideDescript);
    element.on('click', linktochar);
    element.appendTo("#chartable");
  }
}

var linktochar = function(){
  console.log($(this));
  window.location.href = "/charinfo/" + $(this).attr('id');
}

var showDescript = function(){
  $(this).html(sentChars[ $(this).attr('id') ][ 'char-descrip' ]);
};

var hideDescript = function(){
  $(this).html(sentChars[ $(this).attr('id') ][ 'name' ]);
};
