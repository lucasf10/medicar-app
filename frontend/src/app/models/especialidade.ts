interface EspecialidadeJSON extends Especialidade { }

export class Especialidade {

  private id: number;
  private nome: string;

  static fromJSON(json: EspecialidadeJSON): Especialidade {

    let especialidadeObj = Object.create({});
    especialidadeObj = Object.assign(especialidadeObj, json, {});
    
    return especialidadeObj;
  }

  constructor(especialidade?: Especialidade) {

    if (especialidade) {

      this.id = especialidade.id;
      this.nome = especialidade.nome;
    }
  }
}
