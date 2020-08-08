import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {MainComponentComponent} from "./main-component.component";

const routes: Routes = [{
  path: 'main', component: MainComponentComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class MainRoutingModule {
}
