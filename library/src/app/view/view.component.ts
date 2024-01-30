import { Component } from '@angular/core';
import { ApicallService } from '../apicall.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.css']
})
export class ViewComponent {
constructor(private getapi:ApicallService, private route:Router){}
data:any;
ngOnInit(){
         this.getapi.getbooks().subscribe((res) => {
            //console.log(res);
            this.data=res;
            console.log(this.data);
          })

}
view(id:any){
  //console.log(id);
  this.route.navigate(['detail',id]) 

}

edit(id:any)
{
  this.route.navigate(['edit',id])
}

delete(id:any){
  console.log(id);
  if(confirm("are yoy sure you want to delete"))
  {
    this.getapi.deletebookbyid(id).subscribe((res)=>
    {
      console.log(res);
      this.ngOnInit()
    })
  }
}
}
