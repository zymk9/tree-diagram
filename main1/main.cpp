#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <cstring>
#include <string>
#include <bitset>
using namespace std;
bitset<32> DONE("11111011110001100001000000000000");
const unsigned long done = DONE.to_ulong();
int T,map[7][7],md;
int dx[8][2]={1,2,1,-2,-1,2,-1,-2,2,1,-2,-1,2,-1,-2,1};
typedef pair<unsigned long, int> P;
set <P> vis;
int idastar(int dep,unsigned long cur,int p)
{
    if(dep >= md)
        return cur==done&&p==13?1:0;
    int y = (p % 5)?(p % 5):5, x = p / 5 + 1;
    for(int i=0;i<8;i++)
    {
        int nx = x+dx[i][0], ny = y+dx[i][1];
        int b = (nx - 1) * 5 + ny;
        if(nx<1||nx>5||ny<1||ny>5) continue;
        bitset <32> bit(cur);
        int tt = bit[p-1];bit[p-1]=bit[b-1];bit[b-1]=tt;
        P tmp(bit.to_ulong(), b);
        if(vis.count(tmp)) continue;
        vis.insert(tmp);
        if(idastar(dep+1, bit.to_ulong(), b))  return 1;
        vis.erase(tmp);
    }
    return 0;
}
int main()
{
    int i,j,k,t1,t2,t3;
    scanf("%d",&T);
    while(T)
    {
        vis.clear();
        memset(map, 0, sizeof(map));
        char tmp[5];
        bitset<32> bit;
        P tt;
        for(i=1;i<=5;i++)
        {
            cin >> tmp;
            for(j=1;j<=5;j++)
            {
                bit[(i - 1) * 5 + j - 1] = tmp[j-1]=='*'?0:int(tmp[j-1]);
                if(tmp[j-1]=='*')   tt.second = (i-1)*5 + j;
            }
        }
        tt.first = bit.to_ulong();
        for(md=1;md<=15;md++)
        {
            vis.insert(tt);
            if(idastar(0, bit.to_ulong(), tt.second))
            {
                printf("%d\n",md);
                break;
            }
        }
        if(md==16)  printf("-1");
        T--;
    }
}