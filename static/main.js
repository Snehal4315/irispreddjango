function checkinput(){
    var sl = document.form.sl.value;
    var sw = document.form.sw.value;
    var pl = document.form.pl.value;
    var pw = document.form.pw.value;

    if(isNaN(sl) || isNaN(sw) || isNaN(pl) || isNaN(pw)){
        document.getElementById("error").innerHTML = "Please enter a number.";
        document.getElementById("error").style.color = "red";
        document.getElementById("subbtn").disabled = true;
    }
    else{
        if(parseFloat(sl) < 0 || parseFloat(sl) >= 10 ||
        parseFloat(sw) < 0 || parseFloat(sw) >= 10 || 
        parseFloat(pl) < 0 || parseFloat(pl) >= 10 || 
        parseFloat(pw) < 0 || parseFloat(pw) >= 10){
            document.getElementById("error").innerHTML = "Please enter valid value.";
            document.getElementById("error").style.color = "red";
            document.getElementById("subbtn").disabled = true;
        }
        else{
            document.getElementById("subbtn").disabled = false;
            document.getElementById("error").innerHTML = "";
        }
    }
}