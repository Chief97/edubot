import { TestBed } from '@angular/core/testing';

import { DoubtResponseServiceService } from './doubt-response-service.service';

describe('DoubtResponseServiceService', () => {
  let service: DoubtResponseServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DoubtResponseServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
