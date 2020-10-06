import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AutenticacaoService } from '../services/autenticacao.service';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.scss']
})
export class CadastroComponent implements OnInit {

  public nome: string;
  public email: string;
  public password1: string;
  public password2: string;

  constructor(
    private _autenticacao: AutenticacaoService,
    private _router: Router
  ) { }

  ngOnInit(): void {
  }

  cadastrar() {
    this._autenticacao.cadastrarUsuario(this.email, this.nome, this.password1)
      .subscribe(
        resp => this._router.navigateByUrl('/'),
        error => console.log(error)
      );
      // .catch(resp => {
      //   console.log(resp)
      // });
  }

  goToLogin() {
    this._router.navigate(['/login'])
  }

}
