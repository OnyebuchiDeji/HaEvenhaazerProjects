; Simple example
; Writes Hello World to the output

	JMP start
hello: DB "Hello World!" ; Variable
       DB 0	; String terminator

start:
	MOV C, hello    ; Point to variable at memLocation Hello 
	MOV D, 128	; Point new storage area's start
	CALL copy ; copy letters to new area starting from location 128 (80base16)

	MOV D, 232 ; Make D point at new mwmory location

	MOV C, 128 ; Make C also point at location to read the copied letters from

	CALL print ; Print from the new location
        HLT             ; Stop execution

copy:			; copy from C into memory starting at 128(80base16)
	PUSH A
	PUSH B
	MOV B, 0
.loop:
	MOV A, [C]	; Get char from var
	MOV [D], A	; Write to output
	INC C
	INC D  
	CMP B, [C]	; Check if end
	JNZ .loop	; jump if not

	POP B
	POP A
	RET

print:			; print(C:*from, D:*to)
	PUSH A
	PUSH B
	MOV B, 0
.loop2:
	MOV A, [C]	; Get char from var
	MOV [D], A	; Write to output
	INC C
	INC D  
	CMP B, [C]	; Check if end
	JNZ .loop2	; jump if not

	POP B
	POP A
	RET