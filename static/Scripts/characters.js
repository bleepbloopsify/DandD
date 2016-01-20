var closewindow = function(){
  $("button[for=" + $(this).parent().attr("id") +"]").css("visibility", "inherit");
  $(this).parent().css("visibility", "hidden");
};

var openwindow = function(){
  console.log($(this).attr("for"));
  $("#" + $(this).attr("for")).css("visibility", "visible");
  $(this).css("visibility", "hidden");
};

var sendchar = function(){
  var inputs = {};
  $("#creatingcharform input,textarea").each( function(){
    console.log($(this).val());
    inputs[ $(this).attr( "id" ) ] = $(this).val();
  });
  console.log(inputs);
  $.ajax({
    url:"/characters",
    method:"POST",
    data: inputs ,
    success: function(data){
      window.location.href = "/charinfo/" + data;
    }
  });
};

$(document).ready( function(){
  $(".openwindow").click(openwindow);
  $(".closewindow").click(closewindow);
  $("#createchar").click(sendchar);
  $("#openaddfieldform").click(openAddfieldform);
  populateList();
});

var populateList = function(){
  for (var charkey in sentChars){
    char = sentChars[charkey];
    var element = $("<li/>", {"id":char["idnum"], "class":"char"});
    element.html(char["charname"]);
    element.on('mouseover', showDescript);
    element.on('mouseout', hideDescript);
    element.on('click', linktochar);
    element.appendTo("#chartable");
  }
}

var linktochar = function(){
  window.location.href = "/charinfo/" + $(this).attr('id');
}

var openAddfieldform = function(){
  $("#addfieldform").css("visibility", "visible");
  $("#openaddfieldform").css("visibility", "hidden");
}

var showDescript = function(){
  $(this).html(sentChars[ $(this).attr('id') ][ 'char-descrip' ]);
};

var hideDescript = function(){
  $(this).html(sentChars[ $(this).attr('id') ][ 'charname' ]);
};
