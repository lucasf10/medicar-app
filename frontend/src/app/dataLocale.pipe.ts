import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'dataLocale'})
export class DataLocale implements PipeTransform {

  transform(dateString: string): string {
    
    return new Date(dateString.concat(' 00:00:00')).toLocaleDateString();
  }
}