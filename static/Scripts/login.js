$(document).ready(function(){
  $("#sendlogin").on("click", function(){
    $.ajax({
      url:"/login",
      method:"POST",
      data:{
        username:$("#username").val(),
        password:$("#password").val()
      },
      success: function(data){
        if (data == 'success'){
          $("#response").html("<success>Success!</success>");
          window.location.href = "/home"
        }else{
          $("#response").html("<err>Incorrect username or password.</err>");
        }
      }
    });
  })
});
