#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

char* itoa(int num, char* buffer, int base)   
{  
int current = 0;  
if (num == 0) {  
buffer[current++] = '0';  
buffer[current] = '\0';  
return buffer;  
}  
int num_digits = 0;  
if (num < 0) {  
if (base == 10) {  
num_digits ++;  
buffer[current] = '-';  
current ++;  
num *= -1;  
}  
else  
return NULL;  
}  
num_digits += (int)floor(log(num) / log(base)) + 1;  
while (current < num_digits)   
{  
int base_val = (int) pow(base, num_digits-1-current);  
int num_val = num / base_val;  
 char value = num_val + '0';  
buffer[current] = value;  
current ++;  
num -= base_val * num_val;  
}  
buffer[current] = '\0';  
return buffer;  
}  


void main(){
  FILE *f1,*f2,*f3,*f4,*f5,*f6;
  int lc,sa,i=0,j=0,m[10],pgmlen,len,k,len1,l=0;
  char name[10],opnd[10],la[10],mne[10],s1[10],mne1[10],opnd1[10];
  char lcs[10],ms[10];
  char sym[10],symaddr[10],obj1[10],obj2[10],s2[10],q[10],s3[10];
  f1=fopen("input.txt","r");
  f2=fopen("optab.txt","r");
  f3=fopen("symtab.txt","w+");
  f4=fopen("symtab1.txt","w+");
  f5=fopen("output.txt","w+");
  f6=fopen("result.txt","w");

  fscanf(f1,"%s%s%s",la,mne,opnd);
    if(strcmp(mne,"START")==0){
      sa=atoi(opnd);
      strcpy(name,la);
      lc=sa;
  }
  strcpy(s1,"*");
  fscanf(f1,"%s%s%s",la,mne,opnd);
  while(strcmp(mne,"END")!=0){
    if(strcmp(la,"-")==0){
      fscanf(f2,"%s%s",mne1,opnd1);
      while(!feof(f2)){
        if(strcmp(mne1,mne)==0){
          m[i]=lc+1;
          fprintf(f3,"%s\t%s\n",opnd,s1);
          fprintf(f5,"%s\t0000\n",opnd1);
          lc=lc+3;
          i=i+1;
          break;
        }
        else{
         fscanf(f2,"%s%s",mne1,opnd1);
        }
     }
    }
    else{
      fseek(f3,SEEK_SET,0);
      fscanf(f3,"%s%s",sym,symaddr);
      while(!feof(f3)){
        if(strcmp(sym,la)==0){
          itoa(lc,lcs,10);
          fprintf(f4,"%s\t%s\n",la,lcs);
          itoa(m[j],ms,10);
          j=j+1;
          fprintf(f5,"%s\t%s\n",ms,lcs);
          i=i+1;
          break;
        }
        else{
          fscanf(f3,"%s%s",sym,symaddr);
        }
      }  //f3
      if(strcmp(mne,"RESW")==0)
          lc=lc+3*atoi(opnd);
         else if(strcmp(mne,"BYTE")==0)
         {
          strcpy(s2,"-");
          len=strlen(opnd);
          lc=lc+len-2;
          for(k=2;k<len;k++)
          {
          q[l]=opnd[k];
          l=l+1;
          }
          fprintf(f5,"%s\t%s\n",q,s2);
          break;
         }
         else if(strcmp(mne,"RESB")==0)
          lc=lc+atoi(opnd);
         else if(strcmp(mne,"WORD")==0)
         {
           strcpy(s3,"#");
           lc=lc+3;
           fprintf(f5,"%s\t%s\n",opnd,s3);
           break;
         }
        } // else la=-
     
     
         fseek(f2,SEEK_SET,0);
         fscanf(f1,"%s%s%s",la,mne,opnd);
      }
      fseek(f5,SEEK_SET,0);
      pgmlen=lc-sa;
      fprintf(f6,"H^%s^%d^0%x\n",name,sa,pgmlen);
      fprintf(f6,"T^");
      fprintf(f6,"00%d^0%x",sa,pgmlen);
      fscanf(f5,"%s%s",obj1,obj2);
      while(!feof(f5))
      {
        if(strcmp(obj2,"0000")==0)
          fprintf(f6,"^%s%s",obj1,obj2);
        else if(strcmp(obj2,"-")==0)
          {
          printf("^");
          len1=strlen(obj1);
          for(k=0;k<len1;k++)
          printf("%d",obj1[k]);
          }
          else if(strcmp(obj2,"#")==0)
          {
           printf("^");
           printf("%s",obj1);
           }
        fscanf(f5,"%s%s",obj1,obj2);
      }
      fseek(f5,SEEK_SET,0);
      fscanf(f5,"%s%s",obj1,obj2);
      while(!feof(f5))
      {
       if(strcmp(obj2,"0000")!=0)
       {
         if(strcmp(obj2,"-")!=0)
         {
         if(strcmp(obj2,"#")!=0)
         {
          printf("\n");
          fprintf(f6,"T^%s^02^%s",obj1,obj2);
         }
        }
        }
        fscanf(f5,"%s%s",obj1,obj2);
       }
      fprintf(f6,"\nE^00%d",sa);
     
     }