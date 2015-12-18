$(document).ready(function(){
  $("#sendlogin").on("click", function(){
    console.log("llo");
    $.ajax({
      url:"/login",
      method:"POST",
      data:{
        username:$("#username").val(),
        password:$("#password").val()
      },
      success: function(data){
        if (data){
          $("#response").html("<success>Success!</success>");
          window.location.href = "/home"
        }else{
          $("#response").html("<err>");
        }
      }
    });
  })
});
