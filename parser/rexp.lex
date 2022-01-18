%{
int linecounter = 1;
%}
%option nounput
%%
[0-9]+                                          { return(INTEGER); }
[0-9]*"."[0-9]+                                 { return(REAL); }
"~"                                             { return(TILDE); }
"|"                                             { return(VERTICAL); }
"+"                                             { return(ADD); }
"-"                                             { return(SUBTRACT); }
"*"                                             { return(MULTIPLY); }
"/"                                             { return(DIVIDE); }
"("                                             { return(LPAR); }
")"                                             { return(RPAR); }
"\n"                                            { linecounter++; return(NEWLINE); }
"\r\n"                                          { linecounter++; return(NEWLINE); }
"\r"                                            { linecounter++; return(NEWLINE); }
" "|"\t"                                        { }
"/*"                                            { comment(); }
[^\t \n\r~|\(\)\+\-]+                           { return(ID); }
<<EOF>> {
	// 最後の行が改行ではなかった時のために、改行を加える
	static int once = 0; return (once = !once) ? NEWLINE : 0;
	}
%%
int yywrap(void) {
	return(1);
}
void comment(void) {
	int boolean, first, second;

	boolean = TRUE;
	first = input();
	while (first != EOF && boolean) {
		second = input();
		if (first == '*' && second == '/') {
			boolean = FALSE;
		} else if (first == '\r' && second == '\n') {
			linecounter++;
			first = input();
		} else {
			if (first == '\r' || first == '\n') {
				linecounter++;
			}
			first = second;
		}
	}
	if (first == EOF) {
		fprintf(stderr, "eof in comment\n");
	}
}
