#include <iostream>

using namespace std;

int main()
{
    int c;
    long long n, k, b, t;
    long long pos[51], speed[51];
    cin >> c;

    for(int i = 1; i <= c; i++)
    {
        cin >> n >> k >> b >> t;
        for(int j = 0; j < n; j++)
        {
            cin >> pos[j];
        }

        for(int j = 0; j < n; j++)
        {
            cin >> speed[j];
        }

        long num = 0;
        long result = 0;
        long swap = 0;

        for(int j = n - 1; j >= 0; j--)
        {
            long long distanceCover = speed[j] * t;
            long long distanceToCover = b - pos[j];

            if(distanceToCover <= distanceCover)
            {
                num++;

                if(swap > 0)
                {
                    result += swap;
                }
            }
            else
            {
                swap++;
            }

            if(num == k)
                break;
        }

        if(num < k)
        {
            cout << "Case #" << i << ": IMPOSSIBLE\n";
        }
        else
        {
             cout << "Case #" << i << ": " << result << endl;
        }

    }
    return 0;
}
