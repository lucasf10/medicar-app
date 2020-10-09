import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http'
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AutenticacaoService {

  constructor(private _http: HttpClient) { }

  public loginUsuario(email: string, password: string): Observable<any> {

    const data = {
      'email': email,
      'password': password
    }
    
    return this._http.post<any>(`${environment.apiUrl}/login/`, data); //.toPromise()
  }

  public cadastrarUsuario(email: string, nome: string, password:string): Observable<any> {

    const data = {
      'email': email,
      'nome': nome,
      'password': password
    }
    
    return this._http.post<any>(`${environment.apiUrl}/usuario/criar/`, data); //.toPromise()
  }
}
