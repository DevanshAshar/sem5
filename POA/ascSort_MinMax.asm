DATA SEGMENT
    N1 DB 98h,10h,14h,7h,8h,98h,19h,34h,5h
    SIZE equ $ - N1 
    MIN DB ?
    MAX DB ?
ENDS
CODE SEGMENT
    START:
    MOV AX,DATA
    MOV DS,AX    
    MOV CH,SIZE 

    L1:
    LEA SI,N1 
    MOV CL, SIZE
    DEC CL 
    
    L2:
    MOV AL, [SI] 
    MOV BL, [SI+1]
    CMP AL,BL       ;      Agar Right wala bada hai toh carry aaega
    JC DontSwap     ;      Suppose [SI]=5 [SI+1]=3 
    MOV DL,[SI+1]   ;      DL acts like temp DL mein pehle next element store kiya  DL mein 3 gaya
    XCHG [SI],DL    ;      current pe next element daala and DL mein current SI mein 3 and DL mein 5
    MOV [SI+1],DL   ;      SI+1 mein 5
    
    DontSwap:
    INC SI
    DEC CL
    JNZ L2
    
    DEC CH
    JNZ L1  
    
    LEA SI,N1      ;Min Max ka code
    MOV AL,[SI]    ;AL mein pehla daal diya after asc sort
    MOV MIN,AL     ;MIN mein AL
    ADD SI,SIZE-1  ;SI mein size-1 add kiya toh last element mileg
    MOV AL,[SI]    ;AL mein last element
    MOV MAX,AL     ;MAX mein AL
CODE ENDS    
END START
