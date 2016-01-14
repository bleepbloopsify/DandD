$(document).ready(function(){

    $("#updatePassword").on("click", function(){
	     $.ajax({
	        url:"/editaccount",
          method:"POST",
          data:{
	            newPassword:$("#newPassword").val(),
              oldPassword:$("#password").val()
          },
        });
    })
});
