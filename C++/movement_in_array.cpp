#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        long long int n;
        cin>>n;
        long long int a[n+1],c=0;
        for(long long int i=1;i<=n;i++){
            cin>>a[i];
        }
        long long int k=1,m;
        while(k<=n){
            if(a[k]>0){
                int j=a[k]+1;
                m=0;
                for(int i=k;i<=j;i++){
                    if(a[i]>m){
                        m=a[i]+1;
                    }
                }
                k+=m;
                c+=1;
            }
            else if(a[k]==0){
                cout<<-1<<endl;
                break;
            }
        }
        cout<<c<<endl;
    }
}
