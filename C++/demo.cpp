#include<bits/stdc++.h>
using namespace std;
int main(){
	int x=1,y=4;
	int temp=x^y;
	int c=0;
	while(temp){
		temp=temp&temp-1;
		cout<<temp<<endl;
		c+=1;
	}
	cout<<"c "<<c;
	
}
