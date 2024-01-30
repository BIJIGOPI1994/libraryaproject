import { Component } from '@angular/core';
import { ApicallService } from '../apicall.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  constructor(private regapi:ApicallService){}
data={
'username':'',
'password':''}

  onsubmit()
    {
    console.log(this.data);
    this.regapi.register(this.data).subscribe((res)=>
    {console.log(res);
    this.data=res;
  })
    }
  

}
