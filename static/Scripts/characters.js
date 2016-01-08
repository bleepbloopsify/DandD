// var chartable = document.getElementById("chartable");
//$("#chartable")
// var start = function(){
//     for (var r=0, row; row = chartable.rows[r]; r++){
// 	for (var c=0, col; col = row.cells[c]; c++){
// 	    col.appendChild(img);
// 	    col.addEventListener('mouseover',function(){
// 		var descript = "sample description";
// 		showDescript(this.innerHTML,descript);
// 	    });
// 	}
//     }
// }
//
// var showDescript = function showDescript(name,descript){
//     for (var r=0, row; row = chartable.rows[r]; r++){
// 	for (var c=0, col; col = row.cells[c]; c++){
// 	    if (col.innerHTML == name){
// 		col.innerHTML = descript;
// 		col.addEventListener('mouseout',function(){
// 		    console.log("ok");
// 		    hideDescript(name, descript);
// 		});
// 	    }
// 	}
//     }
// }
//
// var hideDescript = function hideDescript(name,descript){
//     for (var r=0, row; row = chartable.rows[r]; r++){
// 	for (var c=0, col; col = row.cells[c]; c++){
// 	    if (col.innerHTML == descript){
// 		col.innerHTML = name;
// 		col.addEventListener('mouseover',function(){
// 		    showDescript(name, descript);
// 		});
// 	    }
// 	}
//     }
// }
//
// var cellsPerRow = 3;
// var addCell = function addCell(info){
//     var lastRow = chartable.rows[chartable.rows.length-1];
//     var rowSize = lastRow.cells.length;
//     console.log(rowSize);
//     if (rowSize < cellsPerRow){
// 	var newItem = lastRow.insertCell(rowSize);
// 	newItem.innerHTML = info;
//     }
//     else{
// 	var newRow = chartable.insertRow(chartable.rows.length);
// 	var newItem = newRow.insertCell(0);
// 	newItem.innerHTML = info;
//     }
// }
//
// var totalChars = document.getElementById("hiddenchars").innerHTML;
//
// var img = document.createElement('img');
// img.src = "http://pmaadvantage.com/wp-content/uploads/2013/09/Icon-Placeholder.png";
//
// addCell(totalChars);
// addCell("chars2");
//
// start();

//sentChars is defined as dictionary of all characters that belong to this user.

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

  $.ajax({
    url:"/characters",
    method:"POST",
    data: inputs ,
    success: function(data){
      console.log(data);
      window.location.href = "/charinfo/" + data;
    }
  })
};

$(document).ready( function(){
  $("#create_char").click(openwindow);
  $("#closewindow").click(closewindow);
  $("#createchar").click(sendgame);
  populateList();
});


var populateList = function(){
  for (var char in sentChars){
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
  this.html(sentChars[ this.attr('id') ][ 'description' ]);
};

var hideDescript = function(){
  this.html(sentChars[ this.attr('id') ][ 'name' ]);
};
