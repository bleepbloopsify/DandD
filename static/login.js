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
        $("#response").html(data);
      }
    });
  })
});
