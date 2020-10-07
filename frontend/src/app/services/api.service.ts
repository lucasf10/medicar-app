import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators'
import { environment } from 'src/environments/environment';
import { Consulta } from '../models/consulta';
import { Observable } from 'rxjs';

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

  private criarObjetosConsulta(consultasJson): Consulta[] {
    
    const listaConsultas: Consulta[] = [];
    consultasJson.forEach(consulta => listaConsultas.push(Consulta.fromJSON(consulta)));

    return listaConsultas;
  }

}
