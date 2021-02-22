// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends


struct pos
{
    int i;
    int j;
    
};


class Solution {
public:
    int orangesRotting(vector<vector<int>>& matrix)
    {
        
    int R = matrix.size();
    int C = matrix[0].size();
    int count=0;
    int time=0;
    
    int x[]={-1,1,0,0};
    int y[]={0,0,-1,1};
    pos *qu=new pos[R*C+R*C];

    int vacant=0;
    int front=0;
    int last=0;
    for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)
            {
                if(matrix[i][j]==2)
                {
                    count++;
                    qu[last++]={i,j};
                    
                }
                if(matrix[i][j]==0)
                    vacant++;
            }
    
    qu[last++]={-1,-1};
    while(front!=last)
    {
        pos t=qu[front++];
        if(t.i==-1&&t.j==-1&&front!=last)
        {
            time++;
            
            qu[last++]={-1,-1};
            continue;
        }
        for(int i=0;i<4;i++)
        {
            int r=t.i+x[i];
            int c=t.j+y[i];
            if(r>=0&&c>=0&&r<R&&c<C&&matrix[r][c]==1)
            {
                count++;
                matrix[r][c]=2;
                qu[last++]={r,c};
            }
        }
        
    }
    if(count==R*C-vacant)
        return time;
    return -1;
        
    }
};


// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>grid(n, vector<int>(m, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		int ans = obj.orangesRotting(grid);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends
