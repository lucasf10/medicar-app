import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AutenticacaoService } from '../services/autenticacao.service';
import { ValidatorCustom } from '../validators';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.scss']
})
export class CadastroComponent implements OnInit {

  public formulario: FormGroup;
  public errorMsg: string;

  constructor(
    private _autenticacao: AutenticacaoService,
    private _router: Router,
    private _formBuilder: FormBuilder
  ) { 
    this.formulario = this.criarFormulario();
  }

  ngOnInit(): void {
  }

  private criarFormulario(): FormGroup {
    return this._formBuilder.group(
      {
        nome: [null, [Validators.required]],
        email: [ null, [Validators.email, Validators.required]],
        password1: [null, [Validators.required]],
        password2: [null, [Validators.required]]
      },
      { validator: ValidatorCustom.ConfirmarSenha },
    );
  }

  cadastrar() {
    this._autenticacao.cadastrarUsuario(
      this.formulario.value.email,
      this.formulario.value.nome,
      this.formulario.value.password1
    ).subscribe(
      resp => {
        localStorage.setItem('token', resp['token']);
        localStorage.setItem('nomeUsuario', resp['usuario'].nome);
        this._router.navigateByUrl('/');
      },
      error => this.errorMsg = error.error['mensagem']
    );
  }

  goToLogin() {
    this._router.navigate(['/login'])
  }

  hasConfirmarSenhaErro(): boolean {
    return this.formulario.controls['password2'].hasError('ConfirmarSenha');
  }

}
