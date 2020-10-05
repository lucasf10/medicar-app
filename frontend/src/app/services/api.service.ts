import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators'
import { environment } from 'src/environments/environment';
import { Consulta } from '../models/consulta';

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

  getConsultas(): Promise<any> {

    return this._http.get(`${environment.apiUrl}/consultas/`).pipe(
      map(consultas => this.criarObjetosConsulta(consultas))
    ).toPromise();
  }

  public criarObjetosConsulta(consultasJson): Consulta[] {
    
    const listaConsultas: Consulta[] = [];
    
    consultasJson.forEach(consulta => listaConsultas.push(Consulta.fromJSON(consulta)));

    return listaConsultas;
  }
}
