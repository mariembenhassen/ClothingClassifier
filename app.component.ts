import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ImageClassifierComponent } from './components/image-classifier/image-classifier.component'; // Import ImageClassifierComponent

@Component({
  selector: 'app-root',
  standalone: true,  // Mark this component as standalone
  imports: [RouterOutlet, ImageClassifierComponent],  // Import other standalone components here
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent {
  title = 'fashion-classifier-frontend';
}
