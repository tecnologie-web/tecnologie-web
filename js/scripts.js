function focusOnSearchEtichetta() {
	var url = window.location.href;
	if(!document.getElementsByClassName){
		document.getElementById("search").style.display ='none';
	}
	
	if( !(url.indexOf('#' + 'v') != -1) ) {
		document.getElementById('etich').focus();	
	}
}

var checkBox_array;

function onFormLoad(theForm) {
	checkBox_array = [];
	checkBox_array = theForm.getElementsByTagName("input");
	var temp = [];
	for(i=0; i<checkBox_array.length; i++) {
		if(checkBox_array[i].getAttribute("type") != "text"){
			temp.push(checkBox_array[i]);
		}
	}
	checkBox_array = temp;
}

function filter(){
//	per ogni per ogni checkbox controllo tutti i div e se trovo
//	che uno dei dd hai il valore da non mostrare allora non lo mostro.
	onFormLoad(document.getElementById("search"));

	var div_array = document.getElementsByClassName("pr_container_wrapper");
	var temp = document.getElementById("etichetta").value;
	var stringToSearch = temp.trim().toUpperCase();
//	per ogni <div> cerco i sui <dd>
	for(i=0; i<div_array.length; i++){
		var flag = true;
		var dd_array = div_array[i].getElementsByTagName("dd");
//		per ogni checkbox controllo tutti i <dd>
		for(j=0; j<checkBox_array.length; j++){
			var isNameMatch = false;
			for(t=0; t<dd_array.length; t++){
//				se è una ricerca anche per nome allora fa questo blocco if
				if(stringToSearch != "" && !isNameMatch){
					var temp2 = dd_array[t].innerHTML;
					var str = temp2.trim().toUpperCase();
					var pos = str.indexOf(stringToSearch);
					if(pos != -1)
						flag = flag * true;
					else
						flag = flag * false;

					isNameMatch = true;
				}
//				se ce match tra il valore della checkbox e il valore dell tag
//				allora controllo se la checkbox è true o false
				if(checkBox_array[j].value.trim() == dd_array[t].innerHTML.trim()){
					flag = flag * checkBox_array[j].checked;
				}
			}
		}

		if(flag){
			div_array[i].style.display='block';
//			div_array[i].setAttribute("class",'pr_container');
		}else{
			div_array[i].style.display='none';
//			div_array[i].setAttribute("class",'pr_container_hidden');

		}
	}
}