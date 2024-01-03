function myFunction() {
  console.log("i am from mmhauth/custom.js");
  var x = document.getElementById("id_password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
