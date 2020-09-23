import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SummaryPopupComponent } from './summary-popup.component';

describe('SummaryPopupComponent', () => {
  let component: SummaryPopupComponent;
  let fixture: ComponentFixture<SummaryPopupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SummaryPopupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SummaryPopupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
