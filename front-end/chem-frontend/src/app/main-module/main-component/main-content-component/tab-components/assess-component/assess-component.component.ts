import { Component, OnInit } from '@angular/core';
import { ChartType, ChartOptions } from 'chart.js';
import { SingleDataSet, Label, monkeyPatchChartJsLegend, monkeyPatchChartJsTooltip } from 'ng2-charts';
import {SelfEvaluateServiceService} from "../../../../../services/self-evaluate-service.service";
@Component({
  selector: 'app-assess-component',
  templateUrl: './assess-component.component.html',
  styleUrls: ['./assess-component.component.css']
})
export class AssessComponentComponent implements OnInit {

  public pieChartColors: Array < any > = [{
    backgroundColor: ['rgba(144, 238, 144, 1)', 'rgba(255, 127, 127, 1)'],
    borderColor: ['rgba(144, 238, 144, 1)', 'rgba(255, 127, 127, 1)']
  }];

  chapterSelection;
  correctAnswer = 0
  inCorrectAnswer = 0
  correctSymbolAnswer = 0
  inCorrectSymbolAnswer = 0
  public pieChartOptions: ChartOptions = {
    responsive: true,
  };
  public pieChartLabels: Label[] = [['Correct'], ['Incorrect']];
  public pieChartData: SingleDataSet = [this.correctAnswer,this.inCorrectAnswer];
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [];




  correctAnswerArray = []
  correctSymbolAnswerArray = []
  incorrectAnswerArray = []
  incorrectSymbolAnswerArray = []
  seletedParagraph = null
  // questionAnswerList =
  //   [
  //     {
  //       "answerOptions": ["Dimitry Mendeleff", "Ernest Rutherfurd", "Neils Bohr", "John Doily"
  //       ],
  //       "correctAnswer": "Ernest Rutherfurd",
  //       "position": 1,
  //       "enteredAnswer": 0,
  //       "question": "Who invented planetary model?"
  //     },
  //     {
  //       "answerOptions": [
  //         "Dimitry Mend", "Neils B", "Ernest Rutherfurd", "John ily"
  //       ],
  //       "correctAnswer": "Ernest Rutherfurd",
  //       "position": 2,
  //       "enteredAnswer": 0,
  //       "question": "Who made planetary model?"
  //     }
  //   ]
  questionSymbolAnswerList = null
  questionAnswerList = null
  chapterList =[]
  showDropdown = false
  showQuestions = false
  showParagraph = false
  showSummary = false
  showSymbolSummary = false
  showSymbolQuestions = true
  constructor(private httpService : SelfEvaluateServiceService) { }

  ngOnInit(): void {
  this.fetchChapterListandContent()

    let json = {
      "data": {
        "questionType": "sample",
        "sectionName": "sample",
        "questionCategory": "section",
        "paragraph": "Sodium, potassium and calcium are highly reactive metals. Highly reactive metals are stored in kerosene and liquid paraffin. zinc and magnesium contacts will prevent rusting of iorn. Highly reactive metals are extracted by the electrolysis of the metals fused chloride. Moderate reactive metals are extracted by reducing the compounds by other elements. Silver, gold platinum are low reactive  metals. Low reactive metals are extracted using physical methods."
      }
    }

    // let json = {
    //   "data": {
    //     "questionType": "",
    //     "sectionName": "",
    //     "questionCategory": "database",
    //     "paragraph": ""
    //   }
    // }

    // this.httpService.allquestions(json).subscribe((data:any)=>{
    //   console.log(data)
    // })

    this.fetchSymbolQuestions()
  }

  fetchQuestionForChapter(){
    let e =(<HTMLSelectElement>document.getElementById("chapterType")).options
    let selectedChapter = (<HTMLSelectElement>document.getElementById("chapterType")).options[e.selectedIndex].value
    this.chapterSelection = selectedChapter
    console.log(selectedChapter)
    for(let i=0;i < this.chapterList.length;i++){
      if(this.chapterList[i].name == selectedChapter){
        this.seletedParagraph =  this.chapterList[i].paragraph
        this.showParagraph = true
      }
      if(selectedChapter == "none"){
        this.seletedParagraph = null;
        this.showQuestions = false
        this.showParagraph = false
      }
    }
  }

  getValue(question){
    let e = (<HTMLSelectElement>document.getElementById(question)).options
    let enteredAnswer =parseInt((<HTMLSelectElement>document.getElementById(question)).options[e.selectedIndex].value)
    console.log((<HTMLSelectElement>document.getElementById(question)).options[e.selectedIndex].value)
    for(let i = 0;i<this.questionAnswerList.length;i++){
      if(question == this.questionAnswerList[i].question){
        this.questionAnswerList[i].enteredAnswer = enteredAnswer
        console.log("Entered answer " + this.questionAnswerList[i].enteredAnswer)
      }
    }
    console.log(this.questionAnswerList)
  }

  displayChapterQuestions(){
    this.questionAnswerList = null
    this.showParagraph = false;
    this.showQuestions = true;

    let json = {
      "data": {
        "questionType": "sample",
        "sectionName": "sample",
        "questionCategory": "section",
        "paragraph": this.seletedParagraph
      }
    }

    this.httpService.allquestions(json).subscribe((data:any) =>{
      this.questionAnswerList = data
      console.log(data)
    })
  }
  submitQuiz(){
    this.correctAnswer =0
    this.inCorrectAnswer =0
    this.correctAnswerArray = []
    this.incorrectAnswerArray = []
    console.log(this.questionAnswerList.length)
    for(let i = 0; i< this.questionAnswerList.length;i++){
      let e = (<HTMLSelectElement>document.getElementById(this.questionAnswerList[i].question)).options;
      let answerValue = (<HTMLSelectElement>document.getElementById(this.questionAnswerList[i].question)).options[e.selectedIndex].value
      if(answerValue == this.questionAnswerList[i].position.toString()){
        this.correctAnswer = this.correctAnswer +1
        this.correctAnswerArray.push(this.questionAnswerList[i])
      }else {
        this.inCorrectAnswer = this.inCorrectAnswer +1
        this.incorrectAnswerArray.push(this.questionAnswerList[i])
      }
    }
   this.pieChartData = [this.correctAnswer,this.inCorrectAnswer];
    this.showQuestions =false
    this.showSummary =true
    console.log("Correct Answer : " + this.correctAnswer)
    console.log("Incorrect Answer : " + this.inCorrectAnswer)
    console.log("Questions : " + (this.inCorrectAnswer+this.correctAnswer) )
  }

  fetchChapterListandContent(){
    this.httpService.getChapterContent().subscribe((data:any) => {
      console.log(data)
      this.chapterList = data
    })
  }

  returnToParagraph(){
    this.showParagraph =true
    this.showQuestions =false
    this.showSummary =false
  }

  submitSymbolQuiz(){

    this.correctSymbolAnswerArray = []
    this.incorrectSymbolAnswerArray = []
    this.showSymbolQuestions =false
    this.showSymbolSummary = true
    this.correctSymbolAnswer =0
    this.inCorrectSymbolAnswer =0
    console.log(this.questionSymbolAnswerList.length)
    for(let i = 0; i< this.questionSymbolAnswerList.length;i++){
      let e = (<HTMLSelectElement>document.getElementById(this.questionSymbolAnswerList[i].question)).options;
      let answerValue = (<HTMLSelectElement>document.getElementById(this.questionSymbolAnswerList[i].question)).options[e.selectedIndex].value
      if(answerValue == this.questionSymbolAnswerList[i].position.toString()){
        this.correctSymbolAnswer = this.correctSymbolAnswer +1
        this.correctSymbolAnswerArray.push(this.questionSymbolAnswerList[i])
      }else {
        this.inCorrectSymbolAnswer = this.inCorrectSymbolAnswer +1
        this.incorrectSymbolAnswerArray.push(this.questionSymbolAnswerList[i])
      }
    }
    this.pieChartData = [this.correctSymbolAnswer,this.inCorrectSymbolAnswer];
    this.showQuestions =false
    this.showSummary =true
    console.log("Correct Answer : " + this.correctSymbolAnswer)
    console.log("Incorrect Answer : " + this.inCorrectSymbolAnswer)
    console.log("Questions : " + (this.inCorrectSymbolAnswer+this.correctSymbolAnswer) )
  }
  fetchSymbolQuestions(){
    let json = {
        "data": {
          "questionType": "",
          "sectionName": "",
          "questionCategory": "database",
          "paragraph": ""
        }
      }
      this.httpService.allquestions(json).subscribe((data:any) => {
        this.questionSymbolAnswerList = data
      })
  }

  reloadQuestions() {
    this.showSymbolSummary =false
    this.questionSymbolAnswerList = null
    this.showSymbolQuestions = true
    this.fetchSymbolQuestions()
  }
  returnParagraph(){
    this.showParagraph = true
    this.showSummary = false
  }
}
