import { Component, OnInit} from '@angular/core';
import {DatePipe} from '@angular/common';
import {SelfLearnServiceService} from '../../../../../services/self-learn-service.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-learn-component',
  templateUrl: './learn-component.component.html',
  styleUrls: ['./learn-component.component.css']
})
export class LearnComponentComponent implements OnInit {
  date = Date;
  messages = [];
  data = '';
  typing = false;
  type = '../../assets/image/typing.gif';

  // providers: [DatePipe];
  // constructor(public datePipe: DatePipe){}

  constructor(private httpService: SelfLearnServiceService, public router: Router){}
  // getDate(){
  //   this.date = new Date();
  //   const latestDate = this.datePipe.transform(this.date, 'yyyy-MM-dd HH:mm:ss');
  //   console.log(latestDate);
  //   return latestDate;
  // }


  delay(ms: number){
    return new Promise( resolve => setTimeout(resolve, ms) );
  }

  input(){
    console.log('method initiated');
    // const timer = this.getDate();
    // this.messages.push({user: 'user', userMsg: text, time: timer});
    if (this.data !== ''){
      this.messages.push({userType: 'user', userMsg: this.data, date: this.date.now()});
      console.log(this.messages);
      const json = {
        data: this.data
      };
      console.log(json);
      this.httpService.generateReply(json).subscribe(async (data: any) => {
        console.log('content sent');
        this.data = '';
        this.typing = true;
        this.messages.push(this.type);
        if (data.type === 'textContent') {
          await this.delay(5000);
          this.messages.push({userType: 'bot', dataTitle: data.name, userMsg: data.html_text, dataType: data.type, date: this.date.now()});
        } else if (data.type === 'ConversationReply') {
          await this.delay(1500);
          this.messages.push({userType: 'bot', userMsg: data.output_value, dataType: data.type, date: this.date.now()});
        } else {
          await this.delay(800);
          this.messages.push({userType: 'bot', userMsg: data.output_value, date: this.date.now()});
        }
        this.typing = false;
      });
      console.log(this.messages);
    }
    }

  ngOnInit(): void {
    this.messages.push({userType: 'bot', userMsg: 'Hi! I am Edubot!', date: this.date.now()});
  }

}
