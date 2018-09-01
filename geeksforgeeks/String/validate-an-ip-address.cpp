#include <bits/stdc++.h>
using namespace std;

int isValid(char *);

int main()
{
	//code
	int t;
	cin >> t;
	while (t--)
	{
		char s[10000];
		cin >> s;
		cout << isValid(s) << endl;
	}
	return 0;
}

int isValid(char *ip) {
	int length = strlen(ip);
	int i = 0, dotCount = 0;
	while(i < length) {
		if(ip[i] == '\0' || (ip[i] == '0' && (ip[i+1] == '0' || (ip[i+1] > '0' && ip[i+1] <= '9'))))
			return 0;

		int digitCount = 0, num = 0;

		while(ip[i] != '.' && i < length) {
			char c = ip[i++];
			if(c >= '0' && c <= '9') {
				digitCount++;
			}
			num = (num * 10) + (c - '0');
		}

		if(i < length) {
			dotCount++;
		}

		if(dotCount > 3 || num < 0 || num > 255 || digitCount == 0 || digitCount > 3) {
			return 0;
		}

		i++;
	}

	if(dotCount < 3) {
		return 0;
	}
	else {
		return 1;
	}
}