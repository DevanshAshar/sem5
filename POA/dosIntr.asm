DATA SEGMENT 
    MSG DB "Enter any Character : $"
    DATA ENDS
CODE SEGMENT
    START:
    MOV AX,DATA
    MOV DS,AX
    LEA DX,MSG
    MOV AH,09H  ;terminal kholega The DOS function 09h display a string that terminated by $
    INT 21H     ;syntax hai dos intr perform karne
    MOV AH,01   ; user ke input ke liye wait karega
    INT 21H      ; al mein hexa value store hoga jo input daala uska => a daala toh ascii 97 and 97 ka hexa 61 , al mein 61 
    MOV DL,AL   ;DL mein daala al ka value
    MOV AH,02   ; 02 se DL wala print karega vaapas
    INT 21H    
    MOV AH,4CH  ;terminate karne 4CH
    INT 21H
    CODE ENDS
END START
