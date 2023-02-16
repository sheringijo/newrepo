function logValidate(){
  var name=document.getElementById('uid').value;
  var password=document.getElementById('pid').value;

  if (name==""||name=="NULL")
  {
    alert("Please enter your name");
    return false;
  }
    if (password == ""){
      alert("please enter the password");
      return false;
    }
    if(password.length < 5){
      alert(" password length must be above five");
      return false;
    }
    return true;
  }