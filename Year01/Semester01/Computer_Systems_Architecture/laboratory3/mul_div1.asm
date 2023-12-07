bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 3
    b db 2
    c db 8
    d dd 13
    x dq 98
segment code use32 class=code
    start:
        ; x-(a+b+c*d)/(9-a); a,c,d-byte; b-doubleword; x-qword

        mov ebx, 0
        mov bl, [a]
        mov cl, [b]
        add bl, cl
    
        mov edx, 0
        mov eax, [d]
        mov ecx, 0
        mov cl, [c]
        mul ecx
    
        add eax, ebx
        adc edx, 0
    
        mov ebx, 0
        mov ecx, 0
        mov bl, 9
        mov cl, [a]
        sub ebx, ecx
    
        div ebx
    
        mov ebx, [x]
        mov ecx, [x-4]
    
        sub ebx, eax
        sbb ecx, 0
    
    
    
        push dword 0
        call [exit]
        