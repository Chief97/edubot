import { Component, OnInit } from '@angular/core';
import {GeneralServiceService} from "../../services/general-service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-register-main-component',
  templateUrl: './register-main-component.component.html',
  styleUrls: ['./register-main-component.component.css']
})
export class RegisterMainComponentComponent implements OnInit {


  constructor(private httpService: GeneralServiceService,public router: Router) { }
    firstName;
    lastName;
    email;
    username;
    password;
    confPassword;
  ngOnInit(): void {
  }

  registerUser() {
    this.firstName = (<HTMLInputElement>document.getElementById("firstName")).value
    this.lastName = (<HTMLInputElement>document.getElementById("lastName")).value
    this.email = (<HTMLInputElement>document.getElementById("email")).value
    this.username = (<HTMLInputElement>document.getElementById("username")).value
    this.password = (<HTMLInputElement>document.getElementById("password")).value
    this.confPassword = (<HTMLInputElement>document.getElementById("confPassword")).value
    if(this.authenticateEmptyField() && this.validateEmail() && this.passwordValidation()) {
      console.log("Authenticated")
      let json = {
        "data": {
          "firstName": this.firstName,
          "lastName": this.lastName,
          "age": 99,
          "username":this.username,
          "password":this.password,
          "gender": "not needed",
          "email": this.email,
          "dob": "01/01/2000"
        }
      }
      this.httpService.registerUser(json).subscribe((data:any) => {
        if(data == 'User was successfully registered') {
          this.router.navigate(["/login"])
        }
        if(data == 'Username already Exists') {
          alert("Username exists, Please choose different username");
          (<HTMLInputElement>document.getElementById("username")).value = "";
          (<HTMLInputElement>document.getElementById("password")).value = "";
          (<HTMLInputElement>document.getElementById("confPassword")).value = "";
        }
      })

    }
  }

  authenticateEmptyField(){
    if(this.firstName ==''){
      alert("Please enter First Name")
      return false;
    }
    if(this.lastName ==''){
      alert("Please enter Last Name")
      return false;
    }
    if(this.email ==''){
      alert("Please enter Email")
      return false;
    }
    if(this.username ==''){
      alert("Please enter Username")
      return false;
    }
    if(this.password ==''){
      alert("Please enter Password")
      return false;
    }
    if(this.confPassword ==''){
      alert("Please Confirm the Password")
      return false;
    }
    return true
  }

  validateEmail() {
    let re = new RegExp('^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$');
    if(!re.test(this.email)){
      alert("Enter Valid Email address")
      return false;
    }
    return true
  }

  passwordValidation() {
    if(this.password != this.confPassword){
      alert("Please confirm the password correctly")
      return false;
    }
    return true;
  }
}
