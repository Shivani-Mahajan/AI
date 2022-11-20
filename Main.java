import java.util. *;

class Main{
public static void main(String[] args){
double x[]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
double memvalue = 0, factor = 0;
double gamma=1;
for (int i=0;i < 10;i++)
{
factor=(double)gamma * Math.abs((double)5 / Math.max(x[i], 5)-(double)i / Math.max(x[i], 5));

if (factor == 0)
  memvalue=1;
if (factor > 0 & & factor <= 1)
  memvalue=1-factor;
if (factor > 1)
  memvalue=0;
System.out.println(i+"->"+memvalue);
}
}
}

