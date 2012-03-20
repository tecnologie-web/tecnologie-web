function focusOnSearchEtichetta() {
	document.getElementById('etich').focus();
}

var checkBox_array;
//var searchText_array;

//String.prototype.startsWith = function(str) 
//{return (this.match("^"+str)==str)}

//String.prototype.trim = function(){return 
//(this.replace(/^[\s\xA0]+/, "").replace(/[\s\xA0]+$/, ""))}

//function nameSearch() {
//onFormLoad(theForm);
////var x = document.getElementById("etichetta").value
////alert(nameToSearch.length);
//filter();
//return true;
//}
//function noEnter() {
//if (event.keyCode == 13) 
//return false;
//else
//return true;
//}


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


//function verifyString(myString, prefix) 
//{
////Remove any white space at the left of the string.
//myString = myString.trimStart();

////Set to lower case.
//myString = myString.toLowerCase();

////Determine if the string starts with the specified prefix.
//var hasPrefix = myString.startsWith(prefix.toString());
//if (hasPrefix === true)
//{
////alert("The string \"" + myString + "\" starts with \"" + prefix + "\""); 
//return true;
//}
//else
//{
////alert("The string \"" + myString + " does not start with \"" + prefix + "\""); 
//return false;
//}
//}

//function startsWith(str, prefix) 
//{
//return (str.match("^"+prefix)==prefix);
//}

function filter(){
//	per ogni per ogni checkbox controllo tutti i div e se trovo
//	che uno dei dd hai il valore da non mostrare allora non lo mostro.
	onFormLoad(document.getElementById("search"));

	var div_array = document.getElementsByClassName("pr_container");
	var temp = document.getElementById("etichetta").value;
	var stringToSearch = temp.trim();
//	per ogni <div> cerco i sui <dd>
	for(i=0; i<div_array.length; i++){
		var flag = true;
		var dd_array = div_array[i].getElementsByTagName("dd");
//		per ogni checkbox controllo tutti i <dd>
		for(j=0; j<checkBox_array.length; j++){
			var nameMatch = false;
			for(t=0; t<dd_array.length; t++){
//				se è una ricerca anche per nome allora fa questo blocco if
//				var temp1 = new String(document.getElementById("etichetta").value);
//				var stringToSearch = temp.trim();
				if(stringToSearch != "" && !nameMatch){
//					flag = flag * startsWith(dd_array[t].innerHTLM, stringToSearch);
					var temp2 = dd_array[t].innerHTML;
					var str = temp2.trim();
					var pos = str.indexOf(stringToSearch);
					if(pos == 0)
						flag = flag * true;
					else
						flag = flag * false;

					nameMatch = true;
				}
//				se ce match tra il valore della checkbox e il valore dell tag
//				allora controllo se la checkbox è true o false
				if(checkBox_array[j].value == dd_array[t].innerHTML){
					flag = flag * checkBox_array[j].checked;
				}
			}
		}

		if(flag){
			div_array[i].style.display='block';
		}else{
			div_array[i].style.display='none';
		}
	}

}




function registration() {

	var flag = true;

	if(document.getElementById('username').value == ""){
		alert("username vuoto");
		flag =false;
	}else{
		if(document.getElementById('username').value.match(/[A-Za-z0-9]+/))
			var username = document.getElementById('username').value;
		else {
			flag=false;
//			document.getElementById('errorUsername_r').style.borderColor="red";
		}
	}



	if(document.getElementById('password').value == ""){
		alert("password vuota");
		flag =false;
	}else{
		if(document.getElementById('password').value.match(/\w+/))
			var password = document.getElementById('password').value;
		else {
			flag=false;
//			document.getElementById('errorPassword_r').style.borderColor="red";
		}
	}

	if(document.getElementById('confirm_password').value == ""){
		alert("conferma password vuota");
		flag =false;
	}else{
		if(document.getElementById('confirm_password').value.match(/\w+/))
			var confirmPassword = document.getElementById('confirm_password').value;
		else {
			flag=false;
//			document.getElementById('errorConfirm_password').style.borderColor="red";
		}
	}

	if(document.getElementById('nome').value == ""){
		alert("campo nome vuoto");
		flag =false;
	}else{
		if(document.getElementById('nome').value.match(/^[A-Za-z]+/))
			var nome = document.getElementById('nome').value;
		else {
			flag=false;
//			document.getElementById('errorConfirm_password').style.borderColor="red";
		}
	}

	if(document.getElementById('cognome').value == ""){
		alert("campo cognome vuoto");
		flag =false;
	}else{
		if(document.getElementById('cognome').value.match(/^[A-Za-z]+/))
			var cognome = document.getElementById('cognome').value;
		else {
			flag=false;
//			document.getElementById('errorConfirm_password').style.borderColor="red";
		}
	}

	if(document.getElementById('email').value == ""){
		alert("campo email vuoto");
		flag =false;
	}else{

		if(document.getElementById('email').value.match(/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/))
			var email = document.getElementById('email').value;
		else {
			alert("formato email sbagliato");
			flag=false;
//			document.getElementById('errorConfirm_password').style.borderColor="red";
		}
	}

	if(document.getElementById('telefono').value == ""){
		alert("campo telefono vuoto");
		flag =false;
	}else{
		var telefono = document.getElementById('telefono').value;
		var pos = telefono.search(/[0-9]/);
		if(pos != 0){
			alert("inserire solo numeri");
			flag = false;
		}
	}


	if(flag==false) {

		return false;
	}
	else {
		if(password==confirmPassword) {
			return true;
		}
		else {
//			document.getElementById('errorPassword_r').style.borderColor="red";
//			document.getElementById('errorConfirm_password').style.borderColor="red";
			alert("uno o più campi sbagliati");
			return false;
		}

	}
//	}

//	function verifyDateFormat(DateString, DateFormat) {
//	var match;
//	var tmpDate;
//	var validFormat = false;

//	match = DateString.match(/^(\d?\d)\D(\d?\d)\D(\d{4}|\d{2})$/);

//	if (match != null) {
//	if (DateFormat == "en") {
//	tmpDate = new Date(match[3], match[1] - 1, match[2]);
//	validFormat = ((tmpDate.getMonth()==match[1]-1) && (tmpDate.getDate()==match[2]));
//	} else if (DateFormat == "it"){
//	tmpDate = new Date(match[3], match[2] - 1, match[1]);
//	validFormat = ((tmpDate.getMonth()==match[2]-1) && (tmpDate.getDate()==match[1]));
//	}
//	}
//	return validFormat;
}