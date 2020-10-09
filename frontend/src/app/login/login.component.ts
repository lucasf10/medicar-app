import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AutenticacaoService } from '../services/autenticacao.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public formulario: FormGroup;
  public errorMsg: string;

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
        email: new FormControl(null, [Validators.email, Validators.required]),
        senha: new FormControl(null, [Validators.required])
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
        error => this.errorMsg = error.error['mensagem']
      );
  }

  goToCriarConta() {
    this._router.navigate(['/cadastro']);
  }

}
