import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';

import { Agenda } from '../models/agenda';
import { Consulta } from '../models/consulta';
import { Especialidade } from '../models/especialidade';
import { Medico } from '../models/medico';

import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-cria-consulta',
  templateUrl: './cria-consulta.component.html',
  styleUrls: ['./cria-consulta.component.scss']
})
export class CriaConsultaComponent implements OnInit {

  public formulario: FormGroup;
  public errorMsg: boolean = false;
  private agendas: Agenda[];
  private agendaSelecionadaId: number;
  private _especialidades: Especialidade[] = [];
  private _medicos: Medico[] = [];
  private _datas: string[] = [];
  private _horarios: string[] = [];

  constructor(
    private _api: ApiService,
    private _formBuilder: FormBuilder,
    private _modal: MatDialogRef<CriaConsultaComponent>
  ) { 
    this.formulario = this.criarFormulario();
  }

  ngOnInit(): void {
    this.populaEspecialidades()
  }

  private populaEspecialidades() {
    this._api.getEspecialidades().subscribe((especialidades: Especialidade[]) => {
      this.especialidades = especialidades;
    });
  }

  private criarFormulario(): FormGroup {
    return this._formBuilder.group(
      {
        especialidade: new FormControl(null, [Validators.required]),
        medico: new FormControl({value: null, disable: true}, [Validators.required]),
        data: new FormControl({value: null, disable: true}, [Validators.required]),
        hora: new FormControl({value: null, disable: true}, [Validators.required])
      }
    );
  }

  populaMedicos() {
    this.datas = [];
    this.horarios = [];

    const especialidade_id = this.formulario.controls['especialidade'].value;

    if (especialidade_id) {

      this._api.getMedicosByEspecialidade(especialidade_id).subscribe((medicos: Medico[]) => {
        this.medicos = medicos;

        if (!this.arrayVazio(this.medicos)) {

          this.formulario.controls['medico'].enable();
          this.formulario.controls['data'].disable();
          this.formulario.controls['data'].patchValue(null);
          this.formulario.controls['hora'].disable();
          this.formulario.controls['hora'].patchValue(null);
        }
      });
    }
  }

  populaDatas() {
    this.horarios = [];
    const medico_id = this.formulario.controls['medico'].value;

    if (medico_id) {

      this._api.getAgendaByMedico(medico_id).subscribe((agendas: Agenda[]) => {
        this.agendas = agendas;
        agendas.forEach((agenda: Agenda) => {
          this.datas.push(agenda.getDia());
        });

        if (!this.arrayVazio(this.datas)) {

          this.formulario.controls['data'].enable();
          this.formulario.controls['hora'].disable();
          this.formulario.controls['hora'].patchValue(null);
        }
      });
    }
  }

  populaHoras() {
    const data = this.formulario.controls['data'].value;
    const agenda: Agenda = this.agendas.find((agenda: Agenda) => agenda.getDia() == data);

    if (agenda) {

      this.horarios = agenda.getHorarios();
      this.agendaSelecionadaId = agenda.getId()
    }

    if (!this.arrayVazio(this.horarios)) {

      this.formulario.controls['hora'].enable();
    }
  }

  get todosCamposPreenchidos(): boolean {
    
    return this.formulario.controls['especialidade'].enabled
      && this.formulario.controls['medico'].enabled
      && this.formulario.controls['data'].enabled
      && this.formulario.controls['hora'].valid;
  }

  criarConsulta() {

    console.log(this.formulario);

    this._api.marcarConsulta(
      this.agendaSelecionadaId,
      this.formulario.controls['hora'].value
    ).subscribe(
      (consulta: Consulta) => {
        this._modal.close(true);
      },
      error => {
        this.errorMsg = true;
      }
    );
  }

  datasDisplay(): string[] {
    return this.datas.map((data: string) => new Date(data).toLocaleDateString());
  }

  set especialidades(especialidades: Especialidade[]) {
    this._especialidades = especialidades
  }

  get especialidades(): Especialidade[] {
    return this._especialidades;
  }

  set medicos(medicos: Medico[]) {
    this._medicos = medicos
  }

  get medicos(): Medico[] {
    return this._medicos;
  }

  set datas(datas: string[]) {
    this._datas = datas
  }

  get datas(): string[] {
    return this._datas;
  }

  set horarios(horarios: string[]) {
    this._horarios = horarios
  }

  get horarios(): string[] {
    return this._horarios;
  }

  arrayVazio(array: any[]) {
    return !(array.length > 0);
  }

}
