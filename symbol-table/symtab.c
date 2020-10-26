#include<stdio.h>
#include<string.h>
#include <stdlib.h>

void main(){
	char opcode[10], operand[10], label[10], mnemonic[10], code[10];
	int locctr, start, length;
	int hash[20], val, temp;

	FILE *input, *optab, *symbol, *output;

	input = fopen("input.txt", "r");
	optab = fopen("optab.txt", "r");
	symbol = fopen("symbol.txt", "w");
	output = fopen("output.txt", "w");

	for(int i=0;i<20;i++){
		hash[i] = 0;
	}

	fscanf(input,"%s\t%s\t%s",label,opcode,operand);

	if(strcmp(opcode,"START")==0){
		start = atoi(operand);
		locctr = start;
		fprintf(output, "\t%s\t%s\t%s\n",label,opcode,operand);
		fscanf(input,"%s\t%s\t%s",label,opcode,operand);
	} else {
		locctr = 0;
	}

	while(strcmp(opcode,"END")!=0){
		fprintf(output, "%d\t",locctr);
		if(strcmp(label,"-")!=0){
			temp = 0;
			val = locctr%5;
			while(temp<20){
				temp ++;
				if(hash[val]==0){
					hash[val]=locctr;
					fprintf(symbol, "%d\t%s\n",locctr,label);
					break;
				}
				else{
					val = (val+1)%5;
				}
			}
		}
		if(temp==20){
			printf("Hash Table is Full!\n");
		}
		fscanf(optab,"%s\t%s",code,mnemonic);
		while(strcmp(code,"END")!=0){
			if(strcmp(opcode,code)==0){
				locctr += 3;
				break;
			}
			fscanf(optab,"%s\t%s",code,mnemonic);
		}
		if(strcmp(opcode,"WORD")==0){
			locctr += 3;
		}
		else if(strcmp(opcode,"RESW")==0){
			locctr += (3*(atoi(operand)));
		}
		else if(strcmp(opcode,"RESB")==0){
			locctr += atoi(operand);
		}
		else if(strcmp(opcode,"BYTE")==0){
			locctr+=strlen(operand)-2;
    
		}
		fprintf(output, "%s\t%s\t%s\t\n",label,opcode,operand);
		fscanf(input,"%s\t%s\t%s",label,opcode,operand);
	}
	fprintf(output, "\t%s\t%s\t%s\n",label,opcode,operand);
	length = locctr-start;
	fclose(input);
	fclose(optab);
	fclose(symbol);
	fclose(output);
	for(int i=0;i<20;i++){
		printf("%i\t",hash[i]);
	}
	printf("\n");
}