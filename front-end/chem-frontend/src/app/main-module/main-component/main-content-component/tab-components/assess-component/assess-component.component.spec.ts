import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AssessComponentComponent } from './assess-component.component';

describe('AssessComponentComponent', () => {
  let component: AssessComponentComponent;
  let fixture: ComponentFixture<AssessComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AssessComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AssessComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
