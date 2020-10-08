import { Medico } from './medico';

interface AgendaJSON extends Agenda { }

export class Agenda {
    
  private id: number;
  private medico: Medico;
  private dia: string;
  private horarios: string[];

  static fromJSON(json: AgendaJSON): Agenda {

    let agendaObj = Object.create(Agenda.prototype);
    agendaObj = Object.assign(agendaObj, json, {
      medico: Medico.fromJSON(json.medico)
    });
    
    return agendaObj;
  }

  constructor(agenda?: Agenda) {

    if (agenda) {
      this.id = agenda.id;
      this.dia = agenda.dia;
      this.horarios = agenda.horarios;
      this.medico = agenda.medico;
    }
  }

  public getId(): number {
    return this.id;
  }

  public getDia(): string {
    return this.dia;
  }

  public getHorarios(): string[] {
    return this.horarios;
  }

}
