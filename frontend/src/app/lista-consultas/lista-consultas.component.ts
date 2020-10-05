import { Component, OnInit } from '@angular/core';

import { Consulta } from '../models/consulta';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-lista-consultas',
  templateUrl: './lista-consultas.component.html',
  styleUrls: ['./lista-consultas.component.scss']
})
export class ListaConsultasComponent implements OnInit {

  private _consultas: Consulta[];

  constructor(private _api: ApiService) { }

  ngOnInit(): void {

    this.getConsultas();
  }

  get consultas(): Consulta[] {
    return this._consultas;
  }

  set consultas(consultas: Consulta[]) {
    this._consultas = consultas;
  }

  getConsultas() {

    this._api.getConsultas().then(consultas => {
      this.consultas = consultas;
    });
  }

  desmarcar() {
    console.log('TODO: desmarcar()');
  }

}
