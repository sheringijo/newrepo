function validate()
{
    var name=document.getElementById("user-id").value;
    var email1=document.getElementById("mail-id").value;
    var password=document.getElementById("pass-id").value;
    var cpass=document.getElementById("cpass-id").value;

    if (name==""||name=="NULL")
{
    alert('please fillout usename field');
    return false;
}

if (password=="")
{
    alert('enter password');
    return false;
}
if (password!==cpass)
{
    alert(' password does not match');
    return false;
}
if (password.length<5)
{
    alert("password length must be graterthan five");
    return false;
}
if (email1.indexOf("@")==-1 || email1.lastIndexOf(".")==-1)
{
    alert("invalid email id");
    return false;
}
     return true;
}