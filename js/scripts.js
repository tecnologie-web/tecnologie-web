function focusOnSearchEtichetta() {
	document.getElementById('etich').focus();
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
				if(checkBox_array[j].value == dd_array[t].innerHTML){
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
function validateLogin() {

	var flag = true;

	if(document.getElementById('username').value == ""){
		document.getElementById('errorLog').innerHTML = "Campo Username vuoto";
		flag =false;
	}else{
		if(document.getElementById('username').value.match(/[A-Za-z0-9]+$/)){
			var username = document.getElementById('username').value;
			document.getElementById('errorLog').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorLog').innerHTML = "Inserire solo caratteri";
		}
	}



	if(document.getElementById('password').value == ""){
		document.getElementById('errorLog').innerHTML = "Campo Password vuoto";
		flag = false;
	}else{
		if(document.getElementById('password').value.match(/\w+/)){
			var password = document.getElementById('password').value;
			document.getElementById('errorLog').innerHTML = "";
		}else {
			flag = false;
			document.getElementById('errorLog').innerHTML = "Caratteri non validi";
		}
	}

	if(flag) {
		document.getElementById('errorLog').innerHTML = "";
		return true;
	}
	else {
		document.getElementById('errorLog').innerHTML = "I campi non coincidono";
		return false;
	}
}

function validateRegistration() {

	var flag = true;

	if(document.getElementById('username').value == ""){
		document.getElementById('errorUsername').innerHTML = "Campo Username vuoto";
		flag =false;
	}else{
		if(document.getElementById('username').value.match(/[A-Za-z0-9]+$/)){
			var username = document.getElementById('username').value;
			document.getElementById('errorUsername').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorUsername').innerHTML = "Inserire solo caratteri";
		}
	}



	if(document.getElementById('password').value == ""){
		document.getElementById('errorPassword').innerHTML = "Campo Password vuoto";
		flag =false;
	}else{
		if(document.getElementById('password').value.match(/\w+/)){
			var password = document.getElementById('password').value;
			document.getElementById('errorPassword').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorPassword').innerHTML = "Caratteri non validi";
		}
	}

	if(document.getElementById('confirm_password').value == ""){
		document.getElementById('errorCPassword').innerHTML = "Campo Conferma Password vuoto";
		flag =false;
	}else{
		if(document.getElementById('confirm_password').value.match(/\w+/)){
			var confirmPassword = document.getElementById('confirm_password').value;
			document.getElementById('errorCPassword').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorCPassword').innerHTML = "Caratteri non validi";
		}
	}

	if(document.getElementById('nome').value == ""){
		document.getElementById('errorName').innerHTML = "Campo Nome vuoto";
		flag =false;
	}else{
		if(document.getElementById('nome').value.match(/[A-Za-z]+$/)){
			var nome = document.getElementById('nome').value;
			document.getElementById('errorName').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorName').innerHTML = "Inserire solo caratteri";
		}
	}

	if(document.getElementById('cognome').value == ""){
		document.getElementById('errorSurname').innerHTML = "Campo Cognome vuoto";
		flag =false;
	}else{
		if(document.getElementById('cognome').value.match(/[A-Za-z]+$/)){
			var cognome = document.getElementById('cognome').value;
			document.getElementById('errorSurname').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorSurname').innerHTML = "Inserire solo caratteri";
		}
	}

	if(document.getElementById('email').value != ""){
		if(document.getElementById('email').value.match(/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/)){
			var email = document.getElementById('email').value;
			document.getElementById('errorEmail').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorEmail').innerHTML = "Formato email sbagliato";
		}
	}

	if(document.getElementById('telefono').value == ""){
		document.getElementById('errorPhone').innerHTML = "Campo Telefono vuoto";
		flag =false;
	}else{
		if(document.getElementById('telefono').value.match(/[0-9]+$/)){
			var telefono = document.getElementById('telefono').value;
			document.getElementById('errorPhone').innerHTML = "";
		}else {
			flag=false;
			document.getElementById('errorPhone').innerHTML = "Inserire solo numeri";
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
			document.getElementById('errorPassword').innerHTML = "I campi non coincidono";
			document.getElementById('errorCPassword').innerHTML = "I campi non coincidono";
			return false;
		}

	}
}