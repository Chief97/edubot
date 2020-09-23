import { TestBed } from '@angular/core/testing';

import { SelfEvaluateServiceService } from './self-evaluate-service.service';

describe('SelfEvaluateServiceService', () => {
  let service: SelfEvaluateServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SelfEvaluateServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
