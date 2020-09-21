import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegisterMainComponentComponent } from './register-main-component.component';
import {MainRoutingModule} from "../../main-module/main-component/main-routing.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {LoginComponentComponent} from "../../components/login-component/login-component.component";




@NgModule({
  declarations: [RegisterMainComponentComponent,LoginComponentComponent],
  imports: [
    CommonModule,
    MainRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ]
})
export class RegisterModuleModule { }
