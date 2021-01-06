import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

const BASE_URL = 'http://127.0.0.1:5000';

@Injectable({
  providedIn: 'root'
})
export class SelfLearnServiceService {

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'my-auth-token',
      'Access-Control-Allow-Origin': '*'
    })
  };

  constructor(private http: HttpClient) { }

  generateReply(data) {
    return this.http.post(`${BASE_URL}//selfLearn/doubtDetection/getIntent`, data, this.httpOptions);
  }

  getChapter(data){
    return this.http.post(`${BASE_URL}/selfLearn/doubtResponse/getChapter`, data, this.httpOptions);
  }
}
