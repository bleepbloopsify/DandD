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
