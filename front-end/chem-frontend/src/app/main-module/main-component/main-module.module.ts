import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponentComponent } from './main-component.component';
import {MainRoutingModule} from "./main-routing.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";




@NgModule({
  declarations: [MainComponentComponent],
  imports: [
    CommonModule,
    MainRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class MainModuleModule { }
