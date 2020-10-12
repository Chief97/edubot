import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";

const BASE_URL = "http://127.0.0.1:5000";


@Injectable({
  providedIn: 'root'
})
export class SelfEvaluateServiceService {

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': 'my-auth-token',
      'Access-Control-Allow-Origin': '*'
    })
  };

  constructor(private http: HttpClient) { }

  getChapterContent() {
    return this.http.get(`${BASE_URL}/selfAssess/getSectionPara`)
  }

  allquestions(data) {
    return this.http.post(`${BASE_URL}/selfAssess/getAllQuestions`,data,this.httpOptions)
  }

}
