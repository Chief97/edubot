import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChaptersChemComponent } from './chapters-chem.component';

describe('ChaptersChemComponent', () => {
  let component: ChaptersChemComponent;
  let fixture: ComponentFixture<ChaptersChemComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChaptersChemComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChaptersChemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
