; Simple example
; Writes Hello World to the output

	JMP start

start:
	MOV C, 35    ; Point to var 
	ADD C, 21    ; Add both numbers
	MOV D, 232	; Point to output
	CALL print
        HLT             ; Stop execution

print:			; print(C:*from, D:*to)
	PUSH A
	PUSH B
	MOV B, 0
	MOV A, C	; Get char from var
	MOV [D], A	; Write to output

	POP B
	POP A
	RET