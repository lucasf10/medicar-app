import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AutenticacaoService } from '../services/autenticacao.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public formulario: FormGroup;

  constructor(
    private _autenticacao: AutenticacaoService,
    private _router: Router,
    private _formBuilder: FormBuilder
  ) {
    this.formulario = this.criarFormulario()
   }

  ngOnInit(): void {
  }

  private criarFormulario(): FormGroup {
    return this._formBuilder.group(
      {
        email: [ null, [Validators.email, Validators.required]],
        senha: [null, [Validators.required]]
      },
    );
  }

  login() {
    this._autenticacao.loginUsuario(this.formulario.value.email, this.formulario.value.senha)
      .subscribe(
        resp => {
          localStorage.setItem('token', resp['token']);
          localStorage.setItem('nomeUsuario', resp['usuario'].nome);
          this._router.navigateByUrl('/');
        },
        error => console.log(error));
      /*.catch(resp => {
        console.log(resp)
      });*/
  }

  goToCriarConta() {
    this._router.navigate(['/cadastro']);
  }

}
