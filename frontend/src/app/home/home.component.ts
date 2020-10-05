import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private _router: Router) {

    if (!localStorage.getItem('token')) {

      this._router.navigate(['/login'])
    }
   }

  ngOnInit(): void {
  }

  get nomePaciente(): string {
    return localStorage.getItem('nomeUsuario')
  }

  logout() {

    localStorage.clear();
    this._router.navigate(['/login'])
  }

}
