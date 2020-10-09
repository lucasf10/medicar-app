import { Especialidade } from './especialidade';

interface MedicoJSON extends Medico { }

export class Medico {
  private id: number;
  private crm: string;
  private nome: string;
  private especialidade: Especialidade;

  static fromJSON(json: MedicoJSON): Medico {

    let medicoObj = Object.create(Medico.prototype);
    medicoObj = Object.assign(medicoObj, json, {
      especialidade: Especialidade.fromJSON(json.especialidade)
    });
    
    return medicoObj;
  }

  constructor(medico?: Medico) {

    if (medico) {

      this.id = medico.id;
      this.crm = medico.crm;
      this.nome = medico.nome;
      this.especialidade = medico.especialidade;
    }
  }
}