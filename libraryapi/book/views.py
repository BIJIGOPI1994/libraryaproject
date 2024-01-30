#from django.shortcuts import render
#from rest_framework.decorators import api_view
from book.models import Book
from book.serializer import bookserializer,userserializer
#from rest_framework import status
#from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#view set
class bookviewset(viewsets.ModelViewSet):#primary key and non primary key
    permission_classes=[IsAuthenticated,]#only authentication user(registed user only)  
    queryset=Book.objects.all()
    serializer_class=bookserializer
    
    


class userviewset(viewsets.ModelViewSet):#primary key and non primary key
    queryset=User.objects.all()
    serializer_class=userserializer# all function working(get,post,etc.)




# class userviewset(generics.List.CreateAPIView):#get and post
#     queryset=User.objects.all()
#     serializer_class=userserializer
    



#generic class
# class booklist(generics.ListCreateAPIView):     #non primary key base
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
    
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):   #primary key base
#     queryset=Book.objects.all()    
#     serializer_class=bookserializer  
    
    








#minixs method
# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
    
# class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Book.objects.all()    
#     serializer_class=bookserializer
#     def get(self,request,pk):
#         return self.retrieve(request)
    
#     def put(self,request,pk):
#         return self.update(request)
    
#     def delete(self,request,pk):
#         return self.destroy(request)

    





# @api_view(['GET','POST'])

#def booklist(request):
#     if(request.method=="GET"):
#         book=Book.objects.all()
#         s=bookserializer(book,many=True)
#         return Response(s.data)
#     elif(request.method=="POST"):
#         s=bookserializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#     return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['GET','PUT','DELETE'])       
# def bookdetail(request,pk):#primary key based
#     try:
#         book=Book.objects.get (pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
       
#     if(request.method=="GET"):
#         s = bookserializer(book)  
#         return Response(s.data)
#     elif(request.method=="PUT"):
#         s=bookserializer(book,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=='DELETE'):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
