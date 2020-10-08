import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'dataLocale'})
export class DataLocale implements PipeTransform {

  transform(dateString: string): string {
    
    return new Date(dateString).toLocaleDateString();
  }
}