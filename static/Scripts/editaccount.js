$(document).ready(function(){

    $("#updatePassword").on("click", function(){
	$.ajax({
	    url:"/editaccount",
            method:"POST",
            data:{
		newUsername:$("#newUsername").val(),
	        newPassword:$("#newPassword").val(),
		oldPassword:$("#password").val()
            },
        });
    })
});
