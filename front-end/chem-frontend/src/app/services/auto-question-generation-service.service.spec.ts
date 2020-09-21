import { TestBed } from '@angular/core/testing';

import { AutoQuestionGenerationServiceService } from './auto-question-generation-service.service';

describe('AutoQuestionGenerationServiceService', () => {
  let service: AutoQuestionGenerationServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AutoQuestionGenerationServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
