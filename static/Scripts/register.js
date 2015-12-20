$(document).ready(function(){
  $("#sendregister").on("click", function(){
    $.ajax({
      url:"/register",
      method:"POST",
      data:{
        username:$("#username").val(),
        password:$("#password").val(),
        confmpwd:$("#confmpwd").val()
      },
      success: function(data){
        if (data == 'success'){
          $("#response").html("<success>Success!</success>");
          window.location.href = "/home"
        }else{
          $("#response").html("<err>Please fill out fields correctly.</err>");
        }
      }
    });
  })
});
