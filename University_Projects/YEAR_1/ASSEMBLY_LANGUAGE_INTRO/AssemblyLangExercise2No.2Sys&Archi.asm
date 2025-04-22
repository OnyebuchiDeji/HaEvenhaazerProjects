; Simple example
; Writes Hello World to the output

	JMP start
hello: DB "Hello World!" ; Variable
       DB 0	; String terminator

start:
	MOV C, hello    ; Point to var 
	MOV D, 232	; Point to output
	CALL print
	SUB C, 12
	CALL print2
        HLT             ; Stop execution

print:			; print(C:*from, D:*to)
	PUSH A
	PUSH B
	MOV B, 0
.loop:
	MOV A, [C]	; Get char from var
	MOV [D], A	; Write to output
	INC C
	INC D  
	CMP B, [C]	; Check if value of C is equal to that of B
	JNZ .loop	; jump if not

	POP B
	POP A
	RET

print2:
	PUSH A
	PUSH B
	MOV B, 0
.comp:
	CMP B, [C]	; Check if end
	JNZ .loop2	; jump if not
	POP B
	POP A
	RET
.loop2:
	MOV A, [C]	; Get char from var
	MOV [D], A	; Write to output
	INC C
	INC D  
	JMP .comp

	