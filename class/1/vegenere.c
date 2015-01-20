/*
 * Simple vegenere utility.
 *
 * Usage: vegenere -[options] key file
 * 
 * Options:
 * -d decrypt file 
 * -e encrypt file
 * 
 * key: alphanumeric string eg. asjdh38729875839dehuqirhy (to use whitespace, enclose in quotes)
 *
 * file: filename of text filename
 */
 
#include <stdio.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
int main(int argc, char **argv){
	
	char flag = 0;
	if (argc != 4){
		printf("Wrong number of arguments: %d\n", argc);
		return 1;
	}
	
	char* file_name = argv[3];
	flag = getopt(argc, argv, "e:d:");
	FILE *file = fopen(argv[3], "r");
	printf("\n%s\n", argv[3]);
	if (file == 0){
		printf("cannot open file\n");
		goto END;
	}
	
	char text;
	char new_text;
	char* key = argv[2];
	int  key_length = strlen(argv[2]);
	
	char name_end[] = "_new.txt";
	char* name;
	int k;
	for (k = 0; file_name[k] != '.'; k++);
	name = malloc(k);
	int l;
	for (l = 0; l < k; l++){
	  name[l] = file_name[l];
	}
	
	printf("%s\n", name);
	int name_length = strlen(name);
	char* new_name = malloc(name_length + strlen(name_end));

	for(k = 0; k < name_length + strlen(name_end); k++){
		if (k < name_length ){
			new_name[k] = file_name[k];
		}
		else{
			new_name[k] = name_end[k - name_length ];
		}
	}
	printf("New name: %s\n", new_name);
	FILE* out = fopen(new_name, "w");
	if (file == 0){
		printf("cannot open ouput file\n");
		goto END;
	}
	
	printf("Length: %d\n", key_length);
	printf("Flag: %c\n", flag);
	
	int i = 0;
	while ((text=fgetc(file)) != EOF){
		printf (" %c-%d", text, text);
		if (text != '\n'){
    		text -= 32; // shift to zero space (first printing char)
	    	if (flag == 'e'){
	    		new_text = (text + (key[i%key_length] - 32))%95;
	    	}
	    	else if (flag == 'd'){
	    		new_text = (text - (key[i%key_length] - 32))%95;
	    		if (new_text < 0){
	    		    new_text += 95;
	    		}
	    	}
	    	new_text += 32;
	    }
	    else
	        new_text = text;
		fputc(new_text, out);
		i++;
	}
	
	END:
	fclose(file);
	fclose(out);
	free(new_name);
	free(name);
	return 0;
}
