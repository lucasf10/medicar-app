import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaConsultaComponent } from './lista-consulta.component';

describe('ListaConsultaComponent', () => {
  let component: ListaConsultaComponent;
  let fixture: ComponentFixture<ListaConsultaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListaConsultaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListaConsultaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
