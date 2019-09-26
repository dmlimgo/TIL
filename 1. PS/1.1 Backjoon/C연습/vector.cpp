#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<int>v;
	v.push_back(10);
	v.push_back(20);
	v.push_back(30);
	vector<int>::iterator iter;
	for (iter = v.begin(); iter != v.end(); iter++) {
		printf("%d", *iter);
	}
	iter = v.begin() + 2;
	printf("%d", *iter);
}