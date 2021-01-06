import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponentComponent } from './main-component.component';
import {MainRoutingModule} from "./main-routing.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {AppModule} from "../../app.module";
import {HeaderComponentComponent} from "./main-content-component/Header/header-component/header-component.component";
import {HomeComponentComponent} from "./main-content-component/tab-components/home-component/home-component.component";
import {ProfileComponentComponent} from "./main-content-component/tab-components/profile-component/profile-component.component";
import {AboutComponentComponent} from "./main-content-component/tab-components/about-component/about-component.component";
import {LearnComponentComponent} from "./main-content-component/tab-components/learn-component/learn-component.component";
import {AssessComponentComponent} from "./main-content-component/tab-components/assess-component/assess-component.component";
import {MainContentComponentComponent} from "./main-content-component/main-content-component.component";
import {HttpClientModule} from "@angular/common/http";
import {GeneralServiceService} from "../../services/general-service.service";
import {SummaryPopupComponent} from "../../components/summary-popup/summary-popup.component";
import {ChartsModule} from "ng2-charts";





@NgModule({
  declarations: [ MainComponentComponent,HeaderComponentComponent,HomeComponentComponent,ProfileComponentComponent,AboutComponentComponent,LearnComponentComponent,AssessComponentComponent,MainContentComponentComponent,SummaryPopupComponent],
  exports: [SummaryPopupComponent],
  imports: [
    CommonModule,
    MainRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    ChartsModule,
  ],
  providers: [
  GeneralServiceService
]
})
export class MainModuleModule { }
