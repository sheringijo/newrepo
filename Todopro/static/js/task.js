function taskValidate(){
    var task=document.getElementById('title').value;
    
  
    if (task==""||task=="NULL")
    {
      alert("Please enter your task");
      return false;
    }
}