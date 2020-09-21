import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";

const BASE_URL = "http://127.0.0.1:5000";


@Injectable({
  providedIn: 'root'
})
export class GeneralServiceService {

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'my-auth-token',
      'Access-Control-Allow-Origin': '*'
    })
  };

  constructor(private http: HttpClient) { }

  registerUser(data) {
    return this.http.post(`${BASE_URL}/registerUser`,data,this.httpOptions)
  }

  validateUser(data) {
    return this.http.post(`${BASE_URL}/validateUser`,data,this.httpOptions)
  }
}
