import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {MainComponentComponent} from "./main-component.component";
import {MainContentComponentComponent} from "./main-content-component/main-content-component.component";

const routes: Routes = [{
  path: 'main', component: MainContentComponentComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})

export class MainRoutingModule {
}
