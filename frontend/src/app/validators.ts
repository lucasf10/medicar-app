
import { AbstractControl, FormGroup } from '@angular/forms';
export class ValidatorCustom {

    static ConfirmarSenha(control: AbstractControl) {
       let password = control.get('password1').value;

       let confirmpassword = control.get('password2').value;

        if(password != confirmpassword) {
            control.get('password2').setErrors( {ConfirmarSenha: true} );
        } else {
            return null;
        }
    }
}