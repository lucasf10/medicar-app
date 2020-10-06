import { Medico } from './medico';

interface ConsultaJSON extends Consulta { }

export class Consulta {
    
  private id: number;
  private dia: string;
  private horario: string;
  private data_agendamento: string;
  private medico: Medico;

  static fromJSON(json: ConsultaJSON): Consulta {

    let consultaObj = Object.create(Consulta.prototype);
    consultaObj = Object.assign(consultaObj, json, {
      medico: Medico.fromJSON(json.medico)
    });
    
    return consultaObj;
  }

  constructor(consulta?: Consulta) {

    if (consulta) {
      this.id = consulta.id;
      this.dia = consulta.dia;
      this.horario = consulta.horario;
      this.data_agendamento = consulta.data_agendamento;
      this.medico = consulta.medico;
    }
  }

  public getId(): number {
    return this.id;
  }



    
}
