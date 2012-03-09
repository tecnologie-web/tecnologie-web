
function filter(value) {
	var div_array = document.getElementsByClassName("pr_container");

	for(i=0; i<div_array.length; i++){
		var dd_array = div_array[i].getElementsByClassName("tipologia");
		
		if(dd_array[0].innerHTML == value)
		{
			
		}
		else
		{
			alert("non ce");
		}
	}

}
