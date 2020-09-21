import { TestBed } from '@angular/core/testing';

import { DoubtDetectionServiceService } from './doubt-detection-service.service';

describe('DoubtDetectionServiceService', () => {
  let service: DoubtDetectionServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DoubtDetectionServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
