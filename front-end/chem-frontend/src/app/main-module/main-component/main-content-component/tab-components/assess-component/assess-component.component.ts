import { Component, OnInit } from '@angular/core';
import { ChartType, ChartOptions } from 'chart.js';
import { SingleDataSet, Label, monkeyPatchChartJsLegend, monkeyPatchChartJsTooltip } from 'ng2-charts';
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

  correctAnswer = 0
  inCorrectAnswer = 0
  public pieChartOptions: ChartOptions = {
    responsive: true,
  };
  public pieChartLabels: Label[] = [['Correct'], ['Incorrect']];
  public pieChartData: SingleDataSet = [this.correctAnswer,this.inCorrectAnswer];
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [];




  correctAnswerArray = []
  incorrectAnswerArray = []
  seletedParagraph = null
  questionAnswerList =
    [
      {
        "answerOptions": ["Dimitry Mendeleff", "Ernest Rutherfurd", "Neils Bohr", "John Doily"
        ],
        "correctAnswer": "Ernest Rutherfurd",
        "position": 1,
        "enteredAnswer": 0,
        "question": "Who invented planetary model?"
      },
      {
        "answerOptions": [
          "Dimitry Mend", "Neils B", "Ernest Rutherfurd", "John ily"
        ],
        "correctAnswer": "Ernest Rutherfurd",
        "position": 2,
        "enteredAnswer": 0,
        "question": "Who made planetary model?"
      }
    ]
  chapterList =
    [
      {"name" : "Activity Series","paragraph" : "The series obtained by the arrangement of metals in the descending order of their reactivity is referred to as the activity series. The Activity Series has been built up by comparing the reactions of metals with air, water, dilute acids and salt solutions. Deciding on the methods of metal extraction, identification of methods that prevent corrosion of metals, selection of metals to construct electrochemical cells according to requirement are uses made from the activity series"},
      {"name" : "Atomic Number","paragraph" : "The atomic number is the number of protons in an atom of the element. Atomic number of the element is equal to the number of protons in an atom of the element. The atomic number of sodium is 11. The number of protons in every atom of the same element is equal. The number of protons in different elements is different. Therefore, the atomic numbers of two atoms of different elements will never be the same. The atomic number of an element is a unique characteristic of an element. The atomic number of an element is symbolized by Z. In a neutral atom, the number of protons is equal to the number of electrons. So, it implies that the atomic number of an element is equal to the number of electrons in an atom of that element. In chemical reactions electrons may be either lost from or gained by atoms and are called ions. The number of electrons in an ion may be less or more than the number of protons. But the number of protons in an ion formed by a particular atom does not change, its atomic number remains unchanged."},
    ]
  showQuestions = false
  showParagraph = false
  showSummary = false
  constructor() { }

  ngOnInit(): void {
  }

  fetchQuestionForChapter(){
    let e =(<HTMLSelectElement>document.getElementById("chapterType")).options
    let selectedChapter = (<HTMLSelectElement>document.getElementById("chapterType")).options[e.selectedIndex].value
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
  }

  displayQuestions(){
    this.showParagraph = false;
    this.showQuestions = true;
  }
  submitQuiz(){

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
}
