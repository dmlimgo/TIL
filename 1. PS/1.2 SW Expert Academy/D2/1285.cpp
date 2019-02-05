#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		int N;
		int m;
		int cnt = 0;
		cin >> N;
		int *arr = new int[N];
		int *abs_arr = new int[N];
		for (int i = 0; i < N; i++) {
			cin >> arr[i];
			abs_arr[i] = abs(arr[i]);
		}
		m = *min_element(abs_arr, abs_arr + N);
		for (int i = 0; i < N; i++) {
			if (abs_arr[i] == m) {
				cnt++;
			}
		}
		cout << "#" << tc + 1 << ' ' << m << ' ' << cnt << endl;
		delete[] arr;
		delete[] abs_arr;
	}
}