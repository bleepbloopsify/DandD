var closewindow = function(){
  $("#creategameform").css("visibility", "hidden");
  console.log("unpls");
};

var openwindow = function(){
  $("#creategameform").css("visibility", "visible");
  console.log("pls");
};


// var sendgame = function(){
//   $.ajax({
//     url:"/creategame",
//     method:"POST",
//     data:{
//       username:$("#username").val(),
//       password:$("#password").val()
//     },
//     success: function(data){
//       if (data == 'success'){
//         $("#response").html("<success>Success!</success>");
//         window.location.href = "/home"
//       }else{
//         $("#response").html("<err>Incorrect username or password.</err>");
//       }
//     }
//   })
// };

$(document).ready(function(){
  $("#creategame").click( openwindow );
  $("#closegamewindow").click( closewindow );
});
