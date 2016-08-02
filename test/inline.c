#include <stdio.h>

void extern inline noarg_noreturn() {
	int n1 = 10, n2 = 24234, i, gcd;

	for (i = 1; i <= n1 && i <= n2; ++i) {
		// Checks if i is factor of both integers
		if (n1 % i == 0 && n2 % i == 0)
			gcd = i;
	}

	printf("G.C.D of %d and %d is %d", n1, n2, gcd);
}
void extern inline arg_noreturn(int arg1) {
	int n = arg1, i;
	for (i = 1; i <= 10; ++i) {
		printf("%d * %d = %d \n", n, i, n * i);
	}
	i = 0;
	int t1 = 0, t2 = 1, nextTerm = 0;
	for (i = 3; i <= n; ++i) {
		nextTerm = t1 + t2;
		t1 = t2;
		t2 = nextTerm;
		printf("%d, ", nextTerm);
	}
}
int extern inline noarg_return() {
	char c = 'c';

	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		printf("%c is an alphabet.", c);
	else
		printf("%c is not an alphabet.", c);

	return 0;
}
int extern inline arg_return(int arg1) {
	int year = arg1;

	if (year % 4 == 0) {
		if (year % 100 == 0) {
			// year is divisible by 400, hence the year is a leap year
			if (year % 400 == 0)
				printf("%d is a leap year.", year);
			else
				printf("%d is not a leap year.", year);
		} else
			printf("%d is a leap year.", year);
	} else
		printf("%d is not a leap year.", year);

	return 0;
}

void use1() {
	int arg1 = 12;
	noarg_noreturn();
	arg_noreturn(arg1);
	noarg_return();
	arg_return(arg1);
}
void use2() {
	int arg1 = 12;
	noarg_noreturn();
	arg_noreturn(arg1);
	noarg_return();
	arg_return(arg1);
}
void use3() {
	int arg1 = 12;
	noarg_noreturn();
	arg_noreturn(arg1);
	noarg_return();
	arg_return(arg1);
}
void use4() {
	int arg1 = 12;
	noarg_noreturn();
	arg_noreturn(arg1);
	noarg_return();
	arg_return(arg1);
}

int main() {
	use1();
	use2();
	use3();
	use4();
}
