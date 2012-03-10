
function filter(value, theCleckBox) {
	var div_array = document.getElementsByClassName("pr_container");

	for(i=0; i<div_array.length; i++){
		var dd_array = div_array[i].getElementsByTagName("dd");
		for(j=0; j<dd_array.length; j++){
			if(!theCleckBox.checked)
			{
				if(dd_array[j].innerHTML == value)
				{
					div_array[i].style.display='none';
				}
			}
			else
			{
				if(dd_array[j].innerHTML == value)
				{
					div_array[i].style.display='';
				}
			}
		}

	}

}
