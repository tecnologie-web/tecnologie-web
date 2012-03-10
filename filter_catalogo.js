//function filterByName(theInput) {
//	var div_array = document.getElementsByClassName("pr_container");
//
//	for(i=0; i<div_array.length; i++){
//		var dt_array = div_array[i].getElementsByTagName("dd");
//		for(j=0; j<dd_array.length; j++){
//			if(dd_array[j].innerHTML != theInput.value)
//			{
//				div_array[i].style.display='none';
//			}
//
//			else
//			{
//				div_array[i].style.display='';
//			}
//		}
//
//	}
//}

function filter(theCleckBox) {
	var div_array = document.getElementsByClassName("pr_container");

	for(i=0; i<div_array.length; i++){
		var dd_array = div_array[i].getElementsByTagName("dd");
		for(j=0; j<dd_array.length; j++){
			if(!theCleckBox.checked)
			{
				if(dd_array[j].innerHTML == theCleckBox.value)
				{
					div_array[i].style.display='none';
				}
			}
			else
			{
				if(dd_array[j].innerHTML == theCleckBox.value)
				{
					div_array[i].style.display='';
				}
			}
		}

	}

}
