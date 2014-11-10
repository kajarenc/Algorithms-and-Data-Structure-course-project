#include <iostream>
#include <algorithm>
#include <vector>
using namespace std; 
class Otrezok{

public:

	int start;
	int end;

	Otrezok() :start(0), end(0){}
	Otrezok(int s, int e) :start(s), end(e){}

};
bool sortByStart(const Otrezok &lhs, const Otrezok &rhs) { return lhs.start < rhs.start; }
int main()
{

	int n , m;
	cin >> n >> m;
	vector<Otrezok>  otrezoks(n);
	int * points = new int[m];

	for (int i = 0; i < n; i++){
		int start;
		int end;
		cin >> start >> end;
		otrezoks[i] = Otrezok(start, end);
	}
	for (int i = 0; i < m; i++){
		int point;
		cin >> point;
		points[i] = point;
	}

	sort(otrezoks.begin(),otrezoks.end(),sortByStart);

	for (int i = 0; i < m; i++)
	{
		int howManyTimes = 0;
		int j = 0;
		while (j<n && otrezoks[j].start <= points[i])
		{
			if (otrezoks[j].end >= points[i]){
				howManyTimes++;
			}
			j++;
		}
		cout << howManyTimes<<" ";
	}

}