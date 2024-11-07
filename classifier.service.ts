import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ClassifierService {
  private apiUrl = 'http://localhost:5000/predict';  // Your Flask API URL

  constructor(private http: HttpClient) {}

  classifyImage(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', file, file.name);

    return this.http.post<any>(this.apiUrl, formData);  // Send file to backend API
  }
}
