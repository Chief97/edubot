import { Component, OnInit } from '@angular/core';
import {routing} from "../../app-routing.module";
import {Router} from "@angular/router";
import {GeneralServiceService} from "../../services/general-service.service";

@Component({
  selector: 'app-login-component',
  templateUrl: './login-component.component.html',
  styleUrls: ['./login-component.component.css']
})
export class LoginComponentComponent implements OnInit {

  constructor( private httpService: GeneralServiceService,public router: Router, ) { }
  username;
  password;
  ngOnInit(): void {
    this.httpService.dataLoad().subscribe();
  }

  checkLoginValidation() {
    this.username = (<HTMLInputElement>document.getElementById("username")).value
    this.password = (<HTMLInputElement>document.getElementById("password")).value


    if (this.authenticateEmpty()) {

      let json = {
        "data": {
          "username": this.username,
          "password": this.password
        }
      }
      this.httpService.validateUser(json).subscribe((data:any) => {
          if (data == 'User does not exists') {
            alert("The username you have entered is not valid, Please try again")
            this.router.navigate(["/login"]);
            (<HTMLInputElement>document.getElementById("username")).value = "";
            (<HTMLInputElement>document.getElementById("password")).value = "";
          }
          if (data == 'Invalid Password') {
            console.log(data)
            alert("Invalid Password");
            (<HTMLInputElement>document.getElementById("password")).value = "";
          }
          if (data == 'User is successfully logged in') {
            console.log(data)
            this.router.navigate(["/content/main"])
          }
      })

    }

  }

  authenticateEmpty(){
    if(this.username ==''){
      alert("Please enter Username")
      return false;
    }
    if(this.password ==''){
      alert("Please enter Password")
      return false;
    }
    return  true
  }
}
