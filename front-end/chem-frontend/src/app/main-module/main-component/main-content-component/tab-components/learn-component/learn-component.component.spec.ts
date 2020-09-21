import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LearnComponentComponent } from './learn-component.component';

describe('LearnComponentComponent', () => {
  let component: LearnComponentComponent;
  let fixture: ComponentFixture<LearnComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LearnComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LearnComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
