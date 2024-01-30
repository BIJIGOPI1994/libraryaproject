import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApicallService {

  constructor(private http:HttpClient) {}
token:any;
header:any;

getbooks()
{
  this.token=localStorage.getItem('token'); //retrives token from localstorae
  this.header=new HttpHeaders({"Authorization":this.token}) //create authorization header using token
  return this.http.get("http://127.0.0.1:8000/book/",{"headers":this.header})// sending api get request
  //with autorization header
}

postbooks(data:any)
{
  this.token=localStorage.getItem('token'); 
  this.header=new HttpHeaders({"Authorization":this.token})
  return this.http.post<any>("http://127.0.0.1:8000/book/",data,{"headers":this.header})
}

getbookbyid(id:any)
{
console.log(id)
return this.http.get<any>(`http://127.0.0.1:8000/book/${id}`,{"headers":this.header})
}
deletebookbyid(id:any)
{
  return this.http.delete<any>(`http://127.0.0.1:8000/book/${id}`,{"headers":this.header})
}
editbookbyid(id:any,data:any)
{
  return this.http.put<any>(`http://127.0.0.1:8000/book/${id}/`,data,{"headers":this.header})
}
register(data:any)
{
  return this.http.post<any>('http://127.0.0.1:8000/user/',data)
}
login(data:any)
{
  return this.http.post<any>('http://127.0.0.1:8000/api-token-auth/',data)
}
}
