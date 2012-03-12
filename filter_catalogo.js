//function filterByName(theInput) {
//var div_array = document.getElementsByClassName("pr_container");

//for(i=0; i<div_array.length; i++){
//var dt_array = div_array[i].getElementsByTagName("dd");
//for(j=0; j<dd_array.length; j++){
//if(dd_array[j].innerHTML != theInput.value)
//{
//div_array[i].style.display='none';
//}

//else
//{
//div_array[i].style.display='';
//}
//}

//}
//}

function nameSearch() {
	if (event.keyCode == 13) 
		return false;
	else
		prova();
		return true;
}

function prova() {
	setTimeout("alert(\'tette\')",2000);
}
function registration() {

	var flag = true;
	var errore = "Devi completare i campi: \n";

//	if(document.getElementById('username').value.match(/^[A-Za-z]+/))
//	var username = document.getElementById('username').value;
//	else {
//	flag=false;
//	document.getElementById('errorName').style.borderColor="red";
//	}

//	if(document.getElementById('surname').value.match(/^[A-Za-z]+/))
//	var surname = document.getElementById('surname').value;
//	else {
//	flag=false;
//	document.getElementById('errorSurname').style.borderColor="red";
//	}

//	if(document.getElementById('birthdate').value!="") {	
//	var validDate = verifyDateFormat(document.getElementById('birthdate').value, "it");
//	if(validDate == false) {
//	document.getElementById('errorBirthday').style.borderColor="red";
//	flag = false;
//	}
//	}
//	else {
//	document.getElementById('errorBirthday').style.borderColor="red";
//	flag = false;
//	}

//	var address = document.getElementById('address').value;
//	var cap = document.getElementById('postal_code').value;
//	var city = document.getElementById('city').value;
//	var province = document.getElementById('province').value;
//	var telephone = document.getElementById('telephone').value;

	if(document.getElementById('username').value.match(/[A-Za-z0-9]+/))
		var username = document.getElementById('username').value;
	else {
		flag=false;
//		document.getElementById('errorUsername_r').style.borderColor="red";
	}
	if(document.getElementById('password').value.match(/\w+/))
		var password = document.getElementById('password').value;
	else {
		flag=false;
//		document.getElementById('errorPassword_r').style.borderColor="red";
	}
	if(document.getElementById('confirm_password').value.match(/\w+/))
		var confirmPassword = document.getElementById('confirm_password').value;
	else {
		flag=false;
//		document.getElementById('errorConfirm_password').style.borderColor="red";
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


var checkBox_array;

function onFormLoad(theForm) {
	checkBox_array = theForm.getElementsByTagName("input");
	var temp = [];
	for(i=0; i<checkBox_array.length; i++) {
		if(checkBox_array[i].getAttribute("type") != "text"){
			temp.push(checkBox_array[i]);
		}
	}
	checkBox_array = temp;
}

function filterByName() {
	
}

function filter(){
//	per ogni per ogni checkbox controllo tutti i div e se trovo
//	che uno dei dd hai il valore da non mostrare allora non lo mostro.
	onFormLoad(document.getElementById("search"));
	var div_array = document.getElementsByClassName("pr_container");
//	per ogni <div> cerco i sui <dd>
	for(i=0; i<div_array.length; i++){
		var flag = true;
		var dd_array = div_array[i].getElementsByTagName("dd");
//		per ogni checkbox controllo tutti i <dd>
		for(j=0; j<checkBox_array.length; j++){
			for(t=0; t<dd_array.length; t++){
//				se ce match tra il valore della checkbox e il valore dell tag
//				allora controllo se la checkbox è true o false
				if(checkBox_array[j].value == dd_array[t].innerHTML){
					flag = flag * checkBox_array[j].checked;
				}
			}
		}

		if(flag){
			div_array[i].style.display='block';
		}else
		{
			div_array[i].style.display='none';
		}
	}

}
