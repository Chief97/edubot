import { TestBed } from '@angular/core/testing';

import { SelfLearnServiceService } from './self-learn-service.service';

describe('SelfLearnServiceService', () => {
  let service: SelfLearnServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SelfLearnServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
