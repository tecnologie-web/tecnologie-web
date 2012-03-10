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
//function registrazione() {
//
//	var flag = true;
//	var errore = "Devi completare i campi: \n";
//
//	if(document.getElementById('name').value.match(/^[A-Za-z]+/))
//		var name = document.getElementById('name').value;
//	else {
//		flag=false;
//		document.getElementById('errorName').style.borderColor="red";
//	}
//	
//	if(document.getElementById('surname').value.match(/^[A-Za-z]+/))
//		var surname = document.getElementById('surname').value;
//	else {
//		flag=false;
//		document.getElementById('errorSurname').style.borderColor="red";
//	}
//	
//	if(document.getElementById('birthdate').value!="") {	
//		var validDate = verifyDateFormat(document.getElementById('birthdate').value, "it");
//		if(validDate == false) {
//			document.getElementById('errorBirthday').style.borderColor="red";
//			flag = false;
//		}
//	}
//	else {
//		document.getElementById('errorBirthday').style.borderColor="red";
//		flag = false;
//	}
//
//	var address = document.getElementById('address').value;
//	var cap = document.getElementById('postal_code').value;
//	var city = document.getElementById('city').value;
//	var province = document.getElementById('province').value;
//	var telephone = document.getElementById('telephone').value;
//
//	if(document.getElementById('usernameRegistration').value.match(/[A-Za-z0-9]+/))
//		var username = document.getElementById('usernameRegistration').value;
//	else {
//		flag=false;
//		document.getElementById('errorUsername_r').style.borderColor="red";
//	}
//	if(document.getElementById('passwordRegistration').value.match(/\w+/))
//		var password = document.getElementById('passwordRegistration').value;
//	else {
//		flag=false;
//		document.getElementById('errorPassword_r').style.borderColor="red";
//	}
//	if(document.getElementById('confirm_password').value.match(/\w+/))
//		var confirmPassword = document.getElementById('confirm_password').value;
//	else {
//		flag=false;
//		document.getElementById('errorConfirm_password').style.borderColor="red";
//	}
//
//	if(flag==false) {
//		return false;
//	}
//	else {
//		if(password==confirmPassword) {
//			return true;
//		}
//		else {
//			document.getElementById('errorPassword_r').style.borderColor="red";
//			document.getElementById('errorConfirm_password').style.borderColor="red";
//			return false;
//		}
//
//	}
//}
//
//function verifyDateFormat(DateString, DateFormat) {
//	var match;
//	var tmpDate;
//	var validFormat = false;
//
//	match = DateString.match(/^(\d?\d)\D(\d?\d)\D(\d{4}|\d{2})$/);
//
//	if (match != null) {
//		if (DateFormat == "en") {
//			tmpDate = new Date(match[3], match[1] - 1, match[2]);
//			validFormat = ((tmpDate.getMonth()==match[1]-1) && (tmpDate.getDate()==match[2]));
//		} else if (DateFormat == "it"){
//			tmpDate = new Date(match[3], match[2] - 1, match[1]);
//			validFormat = ((tmpDate.getMonth()==match[2]-1) && (tmpDate.getDate()==match[1]));
//		}
//	}
//	return validFormat;
//}
function filter(theCheckBox) {
	var div_array = document.getElementsByClassName("pr_container");

	for(i=0; i<div_array.length; i++){
		var dd_array = div_array[i].getElementsByTagName("dd");
		for(j=0; j<dd_array.length; j++){
			if(!theCheckBox.checked)
			{
				if(dd_array[j].innerHTML == theCheckBox.value)
				{
					div_array[i].style.display='none';
				}
			}
			else
			{
				if(dd_array[j].innerHTML == theCheckBox.value)
				{
					div_array[i].style.display='';
				}
			}
		}

	}

}
