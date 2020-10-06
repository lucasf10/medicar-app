import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AutenticacaoService } from '../services/autenticacao.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  
  public email: string;
  public password: string;

  constructor(
    private _autenticacao: AutenticacaoService,
    private _router: Router,
  ) { }

  ngOnInit(): void {
  }

  login() {
    this._autenticacao.loginUsuario(this.email, this.password)
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
