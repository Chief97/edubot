import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { routing} from './app-routing.module';
import { AppComponent } from './app.component';
import { ChaptersChemComponent } from './chapters-chem/chapters-chem.component';
import {LoginComponentComponent} from "./components/login-component/login-component.component";
import {MainModuleModule} from "./main-module/main-component/main-module.module";
import {RegisterModuleModule} from "./register-module/register-main-component/register-module.module";

// import { ParticlesModule } from "../node_modules/angular-particle-updated";


@NgModule({
  declarations: [
    AppComponent,
    ChaptersChemComponent
    AppComponent,
    LoginComponentComponent
  ],
  imports: [
    BrowserModule,
    MainModuleModule,
    routing,
    RegisterModuleModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
