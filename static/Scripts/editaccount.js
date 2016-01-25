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
	    success: function(data){
		if (data == 'bothSuccess'){
		    $("#response").html("<success>Password and Username successfully updated!</success>");
		}
		else if (data == 'userSuccess'){
		    $("#response").html("<success>Username successfully updated!</success>");
		}
		else if (data == 'pwSuccess'){
		    $("#response").html("<success>Password successfully updated!</success>");
		}
		else{
		    $("#response").html("<err>Please fill out the fields correctly.</err>");
		}
	    }
        });
    })
});
