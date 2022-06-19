#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int i, lower, upper, step;
	float celsius, fahr;

	if(argc < 4)
	{
		printf("Usage Error:\n");
		printf("Usage: ./1_3 <lower> <upper> <step>\n");
		exit(1);	
	}
	
	lower = atoi(argv[1]);
	upper = atoi(argv[2]);
	step = atoi(argv[3]);
	fahr = lower;

	printf ("Celsius\t\tFahrenheit\n");
	printf ("=======\t\t==========\n");

	while( fahr <= upper)
	{
		celsius = ((5.0/9.0) * (fahr - 32.0));
		printf("%3.0f\t\t%6.1f\n", fahr, celsius);
		fahr += step;
	}

}
