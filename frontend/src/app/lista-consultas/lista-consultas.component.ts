import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { CriaConsultaComponent } from '../cria-consulta/cria-consulta.component';

import { Consulta } from '../models/consulta';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-lista-consultas',
  templateUrl: './lista-consultas.component.html',
  styleUrls: ['./lista-consultas.component.scss']
})
export class ListaConsultasComponent implements OnInit {

  private _consultas: Consulta[];

  constructor(
    private dialog: MatDialog,
    private _api: ApiService
  ) { }

  ngOnInit(): void {

    this.getConsultas();
  }

  get consultas(): Consulta[] {
    return this._consultas;
  }

  set consultas(consultas: Consulta[]) {
    this._consultas = consultas;
  }

  listaConsultasEstaVazia(): boolean {
    return this.consultas.length > 0;
  }

  getConsultas() {

    this._api.getConsultas().subscribe((consultas: Consulta[]) => {
      this.consultas = consultas;
    });
  }

  removerConsultaPorId(id: number) {
    const indexConsultaParaRemover = this.consultas.findIndex(
      (consulta: Consulta) => consulta.getId() === id
    );
    this.consultas.splice(indexConsultaParaRemover, 1);
  }

  desmarcarConsulta(id: number) {
    this._api.deleteConsulta(id).then(() => {
      this.removerConsultaPorId(id);
    }
    ).catch(error => {
      console.log(error);
    });
  }

  abrirNovaConsulta() {
    let dialogRef = this.dialog.open(CriaConsultaComponent, {
      height: '400px',
      width: '600px',
      disableClose: true,
    });
  }

}
