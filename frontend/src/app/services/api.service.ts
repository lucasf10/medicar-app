import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { map } from 'rxjs/operators'
import { environment } from 'src/environments/environment';
import { Consulta } from '../models/consulta';
import { Observable } from 'rxjs';
import { Especialidade } from '../models/especialidade';
import { Medico } from '../models/medico';
import { Agenda } from '../models/agenda';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private _http: HttpClient) {}

  static getToken(): string | null {

    if (localStorage.getItem('token')){

      return localStorage.getItem('token');
    }
    return null;
  }

  getConsultas(): Observable<Consulta[]> {

    return this._http.get(`${environment.apiUrl}/consultas/`).pipe(

      map(consultas => this.criarObjetosConsulta(consultas))
    );
  }

  deleteConsulta(id: number): Promise<any> {

    return this._http.delete(`${environment.apiUrl}/consultas/${id}`).toPromise();
  }

  getEspecialidades(): Observable<Especialidade[]> {

    return this._http.get(`${environment.apiUrl}/especialidades/`).pipe(

      map(especialidades => this.criarObjetosEspecialidade(especialidades))
    );
  }

  getMedicosByEspecialidade(especialidade_id: number): Observable<Medico[]> {

    return this._http.get(`${environment.apiUrl}/medicos/?especialidade=${especialidade_id}`).pipe(

      map(medico => this.criarObjetosMedico(medico))
    );
  }

  getAgendaByMedico(medico_id: number): Observable<Agenda[]> {

    return this._http.get(`${environment.apiUrl}/agendas/?medico=${medico_id}`).pipe(

      map(agenda => this.criarObjetosAgenda(agenda))
    );
  }

  marcarConsulta(agenda_id: number, horario: string): Observable<Consulta> {

    const data = {
      'agenda_id': agenda_id,
      'horario': horario
    }

    return this._http.post(`${environment.apiUrl}/consultas/`, data).pipe(
      map((consulta => Consulta.fromJSON(<any>consulta)))
    );
  }

  private criarObjetosConsulta(consultasJson): Consulta[] {
    
    const listaConsultas: Consulta[] = [];
    consultasJson.forEach(consulta => listaConsultas.push(Consulta.fromJSON(consulta)));

    return listaConsultas;
  }

  private criarObjetosEspecialidade(especialidadesJson): Especialidade[] {
    
    const listaEspecialidades: Especialidade[] = [];
    especialidadesJson.forEach(especialidade => listaEspecialidades.push(Especialidade.fromJSON(especialidade)));

    return listaEspecialidades;
  }

  private criarObjetosMedico(medicosJson): Medico[] {
    
    const listaEspecialidades: Medico[] = [];
    medicosJson.forEach(medico => listaEspecialidades.push(Medico.fromJSON(medico)));

    return listaEspecialidades;
  }

  private criarObjetosAgenda(agendasJson): Agenda[] {
    
    const listaAgendas: Agenda[] = [];
    agendasJson.forEach(agenda => listaAgendas.push(Agenda.fromJSON(agenda)));

    return listaAgendas;
  }

}
