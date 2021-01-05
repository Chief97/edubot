import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponentComponent} from "./components/login-component/login-component.component";
import {RegisterMainComponentComponent} from "./register-module/register-main-component/register-main-component.component";
import {MainComponentComponent} from "./main-module/main-component/main-component.component";
import {HeaderComponentComponent} from "./main-module/main-component/main-content-component/Header/header-component/header-component.component";


const APP_ROUTES: Routes = [
  {path: '', redirectTo:'/login', pathMatch:'full'},
  {path: 'register', component: RegisterMainComponentComponent},
  {path: 'login', component: LoginComponentComponent},
  {path: 'data-display', component: HeaderComponentComponent},
  {path: 'content', loadChildren: 'src/app/main-module/main-component/main-module.module#MainModuleModule' },
  {path: 'display', loadChildren: 'src/app/main-module/main-component/main-content-component/Header/header-component/header-component.component.html#data_display'}
];

export const routing = RouterModule.forRoot(APP_ROUTES, {useHash: false});
