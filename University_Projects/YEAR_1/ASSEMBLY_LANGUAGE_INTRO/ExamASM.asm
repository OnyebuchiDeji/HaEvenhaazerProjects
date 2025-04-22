
CALL xb 
MOV C, xf
MOV A, xf
ADD A, [xg]
DEC A
MOV D, A
CALL xc
CMP A, 1
JNE xj
MOV [232],80
HLT

xj: 
	MOV [232],62
	MOV [233],80
	HLT
xc: 
	MOV A,0
	MOV B, D
	SUB B, C
	CMP B,0
	JE xh
	MOV B, [C]
	CMP B, [D]
	JNE xi
	INC C
	CMP C, D
	JE xh
	DEC D
	CALL xc
	RET
xh:
	MOV A, 1
	RET
xi:
	MOV A, 0
	RET

xf: 	DB "111 some characters 111"
	DB 0

xg: 	DB 0xff

xb: 	PUSH A
	PUSH B
	PUSH C
	MOV A, 0
	MOV B, 0
	MOV C, xf

xe: 
	CMP B, [C]
	JE xd
	INC A
	INC C
	JMP xe

xd: 
	MOV [xg], A
	POP C
	POP B
	POP A
	RET