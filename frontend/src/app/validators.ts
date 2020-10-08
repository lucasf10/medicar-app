// import { AbstractControl } from '@angular/forms';

// export class Validador {

//   static validadorConfirmaSenha(control: AbstractControl) {
//     const password: string = control.get('password1').value;
//     const confirmPassword: string = control.get('password2').value;

//     if (password !== confirmPassword) {

//       control.get('password2').setErrors({ ConfirmaSenha: true });
//     }
//   }
// }

import { FormGroup } from '@angular/forms';

// custom validator to check that two fields match
export function MustMatch(controlName: string, matchingControlName: string) {
    return (formGroup: FormGroup) => {
        const control = formGroup.controls[controlName];
        const matchingControl = formGroup.controls[matchingControlName];

        if (matchingControl.errors && !matchingControl.errors.mustMatch) {
            // return if another validator has already found an error on the matchingControl
            return;
        }

        // set error on matchingControl if validation fails
        if (control.value !== matchingControl.value) {
            matchingControl.setErrors({ mustMatch: true });
        } else {
            matchingControl.setErrors(null);
        }
    }
}