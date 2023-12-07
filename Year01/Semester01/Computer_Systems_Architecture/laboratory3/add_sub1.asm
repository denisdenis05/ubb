bits 32

global start        

extern exit             
import exit msvcrt.dll    

segment data use32 class=data
    a db 16
    b dw 21
    c dd 23
    d dq 31

segment code use32 class=code
    start:
        ;d-b+a-(b+c)
        
        mov eax, [d]
        mov edx, [d+4]
        
        mov ebx, 0
        mov bx, [b]
        sub eax, ebx
        sbb edx, 0
        
        mov ebx, 0
        mov bl, [a]
        add eax, ebx
        adc edx, 0
        
        mov ebx, 0
        mov bx, [b]
        mov ecx, [c]
        add ebx, ecx
        sbb edx, 0
        
        sub eax, ebx
        sbb edx, 0
        
        ;d-(a+b)+(c+c)
        mov eax, [d]
        mov edx, [d+4]
        
        mov ebx, 0
        mov bl, [a]
        mov ecx, 0
        mov cx,[b]
        add ebx, ecx
        
        sub eax, ebx
        sbb edx, 0
        
        mov ebx, [c]
        mov ecx, [c]
        add ebx, ecx
        sbb edx, 0
        
        sub eax, ebx
        sbb edx, 0
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
