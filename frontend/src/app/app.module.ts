import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms'
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatIconModule } from '@angular/material/icon';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { CadastroComponent } from './cadastro/cadastro.component';
import { HomeComponent } from './home/home.component';
import { ListaConsultasComponent } from './lista-consultas/lista-consultas.component';
import { CriaConsultaComponent } from './cria-consulta/cria-consulta.component';
import { AutenticacaoInterceptor } from './services/autenticacao.interceptor';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CadastroComponent,
    HomeComponent,
    ListaConsultasComponent,
    CriaConsultaComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
    MatIconModule
  ],
  entryComponents: [
    CriaConsultaComponent
  ],
  providers: [
    {
      provide : HTTP_INTERCEPTORS,
      useClass: AutenticacaoInterceptor,
      multi   : true,
    },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
