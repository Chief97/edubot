import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { routing} from './app-routing.module';
import { AppComponent } from './app.component';
import {LoginComponentComponent} from "./components/login-component/login-component.component";
import {MainModuleModule} from "./main-module/main-component/main-module.module";
import {RegisterModuleModule} from "./register-module/register-main-component/register-module.module";
import { MainContentComponentComponent } from './main-module/main-component/main-content-component/main-content-component.component';
import {HttpClientModule} from "@angular/common/http";
import {GeneralServiceService} from "./services/general-service.service";
import { SummaryPopupComponent } from './components/summary-popup/summary-popup.component';


// import { ParticlesModule } from "../node_modules/angular-particle-updated";


@NgModule({
  declarations: [
    AppComponent,


  ],
  imports: [
    BrowserModule,
    MainModuleModule,
    routing,
    RegisterModuleModule,
    HttpClientModule
  ],
  providers: [
    GeneralServiceService
  ],
  exports: [

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
