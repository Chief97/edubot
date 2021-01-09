import {Component, OnInit, ElementRef, ViewChild, Inject} from '@angular/core';
import {SelfLearnServiceService} from '../../../../../services/self-learn-service.service';
import {Router} from '@angular/router';
import {DOCUMENT} from '@angular/common';

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
  myForm = false;
  viewData = false;
  displayData = [];
  @ViewChild('scrollMe') private myScrollContainer: any;
  @ViewChild('chapter_number') chapterNumber: ElementRef;
  @ViewChild('section') section: ElementRef;
  @ViewChild('content') content: ElementRef;
  @ViewChild('myDiv') myDiv: ElementRef;

  // providers: [DatePipe];
  // constructor(public datePipe: DatePipe){}

  constructor(private httpService: SelfLearnServiceService, public router: Router, @Inject(DOCUMENT) document){
    document.getElementById('chapter_number');
  }
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
    this.scrollToBottom();
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
        console.log(data);
        if (data.type === 'textContent') {
          await this.delay(5000);
          this.viewData = false;
          this.displayData = [];
          this.displayData.push(await data);
          this.messages.push({userType: 'bot', userMsg: data.response, dataType: data.type, date: this.date.now()});
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
    this.viewData = true;
  }

  openForm() {
    this.myForm = true;
    console.log(this.myForm);
  }

  closeForm() {
    this.myForm = false;
  }

  scrollToBottom(): void {
    console.log('scroll method');
    this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
  }

  retrieveChapter(graded, chapValue){
    console.log('retrieve chapter');
    const chapter = {
      grade : graded,
      chapter: chapValue
    };
    console.log(chapter);
    this.httpService.getChapter(chapter).subscribe(async (data: any) => {
      // console.log(data);
      this.displayData = [];
      for (let i = 0; i < data.length; i++){
        this.displayData.push(await data[i]);
      }
      // console.log(this.chapterNumber.nativeElement.innerHTML);
      this.viewData = false;
      console.log(this.displayData[0].sectionName);
    });
  }

  back() {
    this.viewData = true;
    this.displayData = [];
  }
}
