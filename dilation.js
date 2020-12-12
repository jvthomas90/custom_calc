// TODO: Add event listener

function run_cal()
{
  if (document.getElementById && document.createTextNode) {	
    var numb1=document.getElementById("num1").value;
	var n_tomatch = /^[0-9.]+$/;
	var n_ismatch = n_tomatch.test(numb1);
	if (n_ismatch) {
      var the_ans=100 * Math.sqrt (1 - ((numb1 * numb1) / (100 * 100)));
      document.getElementById("dil-percent").value=the_ans;	
	  return false;
	  
	}
    else {
	  window.alert("Numbers must be positive and without the % sign.");
	  return false;
	}
  }
}