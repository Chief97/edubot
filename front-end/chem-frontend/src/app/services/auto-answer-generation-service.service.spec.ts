import { TestBed } from '@angular/core/testing';

import { AutoAnswerGenerationServiceService } from './auto-answer-generation-service.service';

describe('AutoAnswerGenerationServiceService', () => {
  let service: AutoAnswerGenerationServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AutoAnswerGenerationServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
