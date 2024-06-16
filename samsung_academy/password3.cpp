#include<cstdio>
#include<algorithm>
#include<list>
#include<string>

//삽입, 삭제, 추가
using namespace std;


void init() {

}

int main()
{


    for(int test=0;test<10;test++){
        // freopen("password_input.txt", "r", stdin);
        int T;
        scanf("%d", &T);

        list<int> password;
        list<int>::iterator cur=password.begin();

        for(int t;t<T;t++){
            int new_password;
            scanf("%d", &new_password);
            password.push_back(new_password);

            

        }

        //세 번째 줄
        scanf("%d", &T);
        for(int t; t<T; t++){
            char alpha;
            scanf("%c", &alpha);

            
            switch(alpha){
                //삽입
                case 'I':
                    int x, y;
                    scanf("%d, %d", &x, &y);
                    break;

                //삭제    
                case 'A':
                    int x, y;
                    scanf("%d, %d", &x, &y);
                    break;

                //추가
                case 'D':
                    int y, s;
                    scanf("%d, %d", &y, &s);
                    break;
                
                default:
                    break;
            }

            

            
        }
    }




    return 0;
}