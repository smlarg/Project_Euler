#include <stdio.h>
#include <math.h>

main()
{
	int n,o,p,q;
	n=1;
	o=1;
	p=2;
	q=p;
	while(p<1000001)
	{
		n=n+p;
		q=p;
		p=p+o;
		o=q;
	}
	printf("%d \n",n);
	printf("%d \n",o);
}
