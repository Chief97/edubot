import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegisterMainComponentComponent } from './register-main-component.component';
import {MainRoutingModule} from "../../main-module/main-component/main-routing.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";




@NgModule({
  declarations: [RegisterMainComponentComponent],
  imports: [
    CommonModule,
    MainRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class RegisterModuleModule { }
