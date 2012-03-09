
function filter(value, theCleckBox) {
	var div_array = document.getElementsByClassName("pr_container");

	for(i=0; i<div_array.length; i++){
		var dd_array = div_array[i].getElementsByClassName("tipologia");

		if(!theCleckBox.checked)
		{
			if(dd_array[0].innerHTML == value)
			{
				div_array[i].style.display='none';
			}
		}
		else
		{
			if(dd_array[0].innerHTML == value)
			{
				div_array[i].style.display='';
			}
		}
	}

}
