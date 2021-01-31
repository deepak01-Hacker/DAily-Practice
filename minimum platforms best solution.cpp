sort(arr,arr+n);
sort(dep,dep+n);
int platneed = 0;
int result=0,i=1,j=0;
if(n==1)
return 1;
while(i<n&&j<n) {="" if(arr[i]<="dep[j])" {="" platneed++;="" i++;="" if="" (platneed=""> result)
result = platneed;
}
else
{
platneed--;
j++;
}
}
return result>0?result+1:0;
}
