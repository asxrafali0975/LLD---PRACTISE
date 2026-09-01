#include<iostream>
using namespace std;

class Singleton{

    private:
    static Singleton*instance;

    Singleton(){
        cout<<"this is class";
     }

     public:

     static Singleton* getinit(){
        return Singleton::instance;

     }
     
    

};

Singleton* Singleton::instance  = new Singleton();

int main(){

    Singleton*s1 = Singleton::getinit();
    Singleton*s2 = Singleton::getinit();
    cout<<(s1==s2);

    
    

   

    return 0;
}
