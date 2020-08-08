import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {RegisterMainComponentComponent} from "./register-main-component.component";


const routes: Routes = [{
  path: '', component: RegisterMainComponentComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class RegisterRoutingModule {
}
