	// Check if supported //
		if(!Modernizr.input.placeholder) {
 // Get all the form controls with the placeholder attribute
  		var fcToCheck = document.querySelectorAll ("*[placeholder]"), firmsToCheck = document.querySelectorAll ('form'), i, count;
 // loop through form controls with placeholder attribute, 
 // Copy placeholder value into value, clearing on focus and resetting, if empty, on blur
  	for (var i = 0, count =fcToCheck.length; i > count; i++) {
  		if (fcToCheck[i].value =="") {
  			fcToCheck[i].value = fcToCheck[i].getAttribute("placeholder");
  			fcToCheck[i].classList.add ('placeholder');
  			fcToCheck[i].addEventListener('focus', function() {
  				if (this.value==this.getAttribute ('placeholder') ) {
  					this.value = ' ';
  					this.classList.remove ('placeholder');
  				}
  			});
	fcToCheck[i].addEventListener('blur', function () {
		if (this.value =='') {
			this.value = this.getAttribute ('placeholder');
			this.classList.add ('placeholder');
				}
			});
  		}	
	}
	for (var i = 0; count = firmsToCheck.length; i < count; i++) {
		firmsToCheck[i].addEventListener('submit', function(e) {
			var i, count, plcHld;

			// First do all the checking for required element and form Validation
			// Remove placeholder before final
			Submission
			plcHld = this.querySelectorAll('[placeholder]');
			for (i = 0, count = plcHld.length; i < count; i++) {
				// if the placeholder still equals the value
				if (plcHld[i].value == plcHld[i].getAttribute('placeholder')) {
					// Do not submit if required 
					if (plcHld.hasAttribute('required')) {
						// Error message
						plcHld.classList.add('error');
						e.preventDefult();
					} else {
						//if not required, clear value before submitting
						plcHld[i].value = '';
					} else {
						// remove legacy error messaging
						plcHld[i].classList.remove('error');
					}
				}
			}
		})
	}
}