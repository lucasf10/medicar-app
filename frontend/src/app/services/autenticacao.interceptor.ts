import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';

import { ApiService } from './api.service';

@Injectable()
export class AutenticacaoInterceptor implements HttpInterceptor {

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    if (ApiService.getToken()) {

      request = request.clone({
        setHeaders: {
          'Content-Type' : 'application/json; charset=utf-8',
          'Accept'       : 'application/json',
          'Authorization': `Token ${ApiService.getToken()}`,
        },
      });
    }

    return next.handle(request);
  }
}