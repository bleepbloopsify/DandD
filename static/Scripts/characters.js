var chartable = document.getElementById("chartable");

var start = function(){
    for (var r=0, row; row = chartable.rows[r]; r++){
	for (var c=0, col; col = row.cells[c]; c++){
	    col.appendChild(img);
	    col.addEventListener('mouseover',function(){
		var descript = "sample description";
		showDescript(this.innerHTML,descript);
	    });
	}
    }
}

var showDescript = function showDescript(name,descript){
    for (var r=0, row; row = chartable.rows[r]; r++){
	for (var c=0, col; col = row.cells[c]; c++){
	    if (col.innerHTML == name){
		col.innerHTML = descript;
		col.addEventListener('mouseout',function(){
		    console.log("ok");
		    hideDescript(name, descript);
		});
	    }
	}
    }
}

var hideDescript = function hideDescript(name,descript){
    for (var r=0, row; row = chartable.rows[r]; r++){
	for (var c=0, col; col = row.cells[c]; c++){
	    if (col.innerHTML == descript){
		col.innerHTML = name;
		col.addEventListener('mouseover',function(){
		    showDescript(name, descript);
		});
	    }
	}
    }
}

var cellsPerRow = 3;
var addCell = function addCell(info){
    var lastRow = chartable.rows[chartable.rows.length-1];
    var rowSize = lastRow.cells.length;
    console.log(rowSize);
    if (rowSize < cellsPerRow){
	var newItem = lastRow.insertCell(rowSize);
	newItem.innerHTML = info;
    }
    else{
	var newRow = chartable.insertRow(chartable.rows.length);
	var newItem = newRow.insertCell(0);
	newItem.innerHTML = info;
    }
}

var totalChars = document.getElementById("hiddenchars").innerHTML;

var img = document.createElement('img');
img.src = "http://pmaadvantage.com/wp-content/uploads/2013/09/Icon-Placeholder.png";

addCell(totalChars);
addCell("chars2");

start();

