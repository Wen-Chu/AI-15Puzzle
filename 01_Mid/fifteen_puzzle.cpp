#include <bits/stdc++.h>
#define DIST(x, y) (abs((a[x][y] - 1) / 4 - (x)) + abs((a[x][y] - 1) % 4 - (y)))
#define MidDIST(x, y) (abs((state[x][y] - 1) / 4 - (x)) + abs((state[x][y] - 1) % 4 - (y)))
#define ZeroDIST(x, y) (abs(15 / 4 - (x)) + abs(15 % 4 - (y)))
using namespace std;
int t,dep,h,cost,total_cost,pop_num=0, f,g, a[4][4],state[4][4], ans[100];
 int dfs(int cur, int h, int x, int y, int dep)
{
	if (cur + h > dep){
		return 0;
	}
		
	if (!h)
	{
		for (int i = 0; i < cur; ++i){
			printf("%c ", "RLDU"[ans[i]]);
			switch ("RLDU"[ans[i]]){
				case 'R':
					swap(state[f][g],state[f][g+1]);
					g++;
					break;
				case 'L':
					swap(state[f][g],state[f][g-1]);
					g--;
					break;
				case 'D':
					swap(state[f][g],state[f+1][g]);
					f++;
					break;
				case 'U':
					swap(state[f][g],state[f-1][g]);
					f--;
					break;
			}
			//�p��u�ꦨ��h*(s)
			int hstar = 0;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++){
					if(state[i][j])
						hstar += MidDIST(i, j);
					else
						hstar += ZeroDIST(i,j);
				}
			//���state
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					if(state[i][j]==0)						//�]���Ʀr���ഫ�A�ҥH��ܫe����^��
						state[i][j]=15;
					else
						state[i][j]--;
					if(i==3&&j==3){							//�L�Xstate�M�u�ꦨ�� 
						cout<<state[i][j];
						total_cost += hstar;
						cout<<"\th(x)�G"<< hstar << endl;
					}
					else
						cout<<state[i][j]<<", ";
					if(state[i][j]==15)						//��^�{���ݱo����
						state[i][j]=0;
					else
						state[i][j]++;
				}
			}
		}
		return 1;
	}
	for (int i = 0, dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0}, tx, ty; i < 4; ++i)
		if (0 <= min(tx = x + dx[i], ty = y + dy[i]) && max(tx, ty) < 4){
			if (!cur || i != (ans[cur - 1] ^ 1))
			{
				pop_num ++;
//				cout << "from " << a[x][y]+15 << " to " << a[tx][ty]-1 <<endl;
				ans[cur] = i;
				int t = DIST(tx, ty);
												
				swap(a[x][y], a[tx][ty]);
				if (dfs(cur + 1, h - t + DIST(x, y), tx, ty, dep)){ 
					return 1;
				}
				swap(a[x][y], a[tx][ty]);		
			}
		}
					
	return 0;
}
int main()
{
	double START,END;
	{
		int num= 0, inv = 0, sx, sy;
		for (int x = 0; x < 4; ++x)
			for (int y = 0; y < 4; ++y)
			{
				scanf("%d%*c", &num);
				//�L�X�D��
				if (x == 0 && y == 0)			 
					cout <<"  " << num;
				else
					cout <<", " << num;
				//��Ʀr�令�{���ݱo��
				if(num == 15){								//�ťծ欰0�Ah*(s)�s�bcost	
					a[x][y]=state[x][y]=0;
					f=x;
					g=y;
					sx = x, sy = y;	
					cost = ZeroDIST(sx,sy);
				}
				else{										//��L��+1�Ah*(s)�s�bh 
					a[x][y]=state[x][y]=num+1;
					h += DIST(x, y);
					for (int i = x << 2 | y, j = 0; j < i; ++j)
						inv += a[j / 4][j % 4] > a[x][y];
				}
			}
		START = clock();
		if ((inv + sx) & 1){
			cout << "\th(x)�G" << cost + h << endl; 		//�L�X�@�}�l�D�ت��u�ꦨ��h*(s) 
			for (dep = h, cost += h; !dfs(0, h, sx, sy, dep);)
				++dep;						
		}
		else
			printf("This puzzle is not solvable.");
	}
	END = clock();
	cout << "\n\nStates_num�G"<<pop_num;
	cout << "\nMove�G"<<dep;
	cout << "\nTotal Cost�G"<< cost + total_cost+ (1+dep)*dep/2;	//cost�D�ؤ@�}�l��h(x)�A�L�{�Ҧ��`�I��hstar�M�A��Τ���g(x)���M 
	cout <<"\nTime�G"<<(END - START) / CLOCKS_PER_SEC  <<"sec"<< endl;
}
