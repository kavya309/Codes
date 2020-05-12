#include<iostream>
#include<vector>
using namespace std;
int main()
{
	vector<int> d{1,2,3,10,14};
	//pushes at the back O(1)
	d.push_back(16);
	//pop O(1) / removes the last element 
	d.pop_back();
	
	//Insert element at index d.begin()+3 with 100 4 times
	d.insert(d.begin()+3,4,100);
	
	//erase some element in the middle
	d.erase(d.begin()+3);
	d.erase(d.begin()+3,d.begin()+5);
	
	//size
	cout<<d.size()<<endl;
	cout<<d.capacity()<<endl;
	
	//resize / capacity doesnt change
	d.resize(8);
	cout<<d.capacity()<<endl;
	
	//clear
	d.clear();
	
	//isempty()
	if(d.empty()){
	    cout<<"Empty"<<endl;
	}
	
	d.push_back(10);
	d.push_back(11);
	d.push_back(12);
	//front and back
	cout<<d.front()<<endl;
	cout<<d.back()<<endl;
	for(int x:d){
		cout<<x<<",";
	}
	//rerserve
	vector<int> v;
	v.reserve(1000);
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	    int no;
	    cin>>no;
	    v.push_back(no);
	    cout<<v.capacity()<<" "<<endl;
	}
	for(int x:v){
	    cout<<x<<",";
	}
}
