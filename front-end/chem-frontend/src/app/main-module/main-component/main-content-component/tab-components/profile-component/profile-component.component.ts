import { Component, OnInit } from '@angular/core';
import {GeneralServiceService} from "../../../../../services/general-service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-profile-component',
  templateUrl: './profile-component.component.html',
  styleUrls: ['./profile-component.component.css']
})
export class ProfileComponentComponent implements OnInit {
  profileDetails = null
  isUpdate = false;
  updateFirstName =null
  updateLastName =null
  updateEmail = null
  updateDob = null

  constructor(private httpService: GeneralServiceService,public router: Router) { }

  ngOnInit(): void {

    this.getUserByUsername()
  }

  getUserByUsername(){
    let json = {
      "data" : {
        "username" : localStorage.getItem("username")
      }
    }
    this.httpService.getUser(json).subscribe((data) => {
      this.profileDetails = data;
      console.log(this.profileDetails)
    })
  }

  enableUpdateOption () {
    this.isUpdate = true;
  }
  logout () {
    window.localStorage.clear();
    this.router.navigate(["/login"]);
  }
  confirmUpdate () {

    this.updateFirstName = (<HTMLInputElement>document.getElementById("firstNameUpdate")).value
    this.updateLastName = (<HTMLInputElement>document.getElementById("lastNameUpdate")).value
    this.updateDob = (<HTMLInputElement>document.getElementById("dobUpdate")).value
    this.updateEmail = (<HTMLInputElement>document.getElementById("emailUpdate")).value

    let json = {
      "data" : {
        "username" : localStorage.getItem("username"),
        "dob": this.updateDob,
        "email": this.updateEmail,
        "firstName": this.updateFirstName,
        "lastName": this.updateLastName
      }
    }
    this.httpService.updateUser(json).subscribe((data:any) =>{
      window.alert(data)
      this.getUserByUsername()
    })

    this.isUpdate = false;
  }
}
