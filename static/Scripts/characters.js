var sentChars = {};
var retrievechars = function(){
  $.ajax({
    url:"/getchars",
    method:"GET",
    success:function(data){
      sentChars = JSON.parse(data);
      populateList();
    }
  });
};

var closewindow = function(){
  $("button[for=" + $(this).parents("div:first").attr("id") +"]").css("visibility", "inherit");
  $(this).parents("div:first").css("visibility", "hidden");
};

var openwindow = function(){
  $("#" + $(this).attr("for")).css("visibility", "inherit");
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
  $(".openwindowbtn").click(openwindow);
  $(".closewindowbtn").click(closewindow);
  $("#createchar").click(sendchar);
  $("#createfield").click(addField);
  retrievechars();
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
  $("#chartable li").last().css("border-bottom","None");
}

var linktochar = function(){
  window.location.href = "/charinfo/" + $(this).attr('id');
}

var showDescript = function(){
  if (sentChars[$(this).attr('id') ]['char-descrip']){
    $(this).html(sentChars[ $(this).attr('id') ][ 'char-descrip' ]);
  }
};

var hideDescript = function(){
  $(this).html(sentChars[ $(this).attr('id') ][ 'charname' ]);
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
  button.click( removefield );
  button.attr("type", "button");
  div.append(button);
  div.appendTo("#creatingcharform");
  $("#addfieldform input").val("");
}

var removefield = function(){
  $(this).parent().remove();
}
