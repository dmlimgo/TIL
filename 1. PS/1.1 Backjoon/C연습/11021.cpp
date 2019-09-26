#include <stdio.h>
int main() {
	int t, i = 0;
	scanf("%d", &t);
	while (i < t) {
		i++;
		int n, m;
		scanf("%d %d", &n, &m);
		printf("Case #%d: %d\n", i, n+m);
	}

	return 0;
}