var chartable = document.getElementById("chartable");

for (var r=0, row; row = chartable.rows[r]; r++){
    for (var c=0, col; col = row.cells[c]; c++){
	col.addEventListener("click",function(){
	    console.log("ok");
	    showDescript(this.innerHTML);
	});
    }
}

var showDescript = function showDescript(n){
    for (var r=0, row; row = chartable.rows[r]; r++){
	for (var c=0, col; col = row.cells[c]; c++){
	    if (col.innerHTML == n){
		col.innerHTML =  " sample description ";
	    }
	}
    }
}

var cellsPerRow = 3;
var addCell = function addCell(info){
    var rowSize = chartable.rows[chartable.rows.length-1].cells.length;
    console.log(rowSize);
    if (rowSize < cellsPerRow){
	var newItem = chartable.rows[chartable.rows.length-1].insertCell(rowSize);
	newItem.innerHTML = info;
    }
    else{
	var newRow = chartable.insertRow(chartable.rows.length);
	var newItem = newRow.insertCell(0);
	newItem.innerHTML = info;
    }
}

addCell("a");
addCell("a");

