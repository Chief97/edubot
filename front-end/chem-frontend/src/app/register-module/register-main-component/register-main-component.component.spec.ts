import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterMainComponentComponent } from './register-main-component.component';

describe('RegisterMainComponentComponent', () => {
  let component: RegisterMainComponentComponent;
  let fixture: ComponentFixture<RegisterMainComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegisterMainComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegisterMainComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
