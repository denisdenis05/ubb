bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 15
    b dw 19
    c dd 21
    d dq 3
    x dq 0
    ;c+d-a-b+(c-a)

segment code use32 class=code
    start:
        ;(b-a+c-d)-(d+c-a-b)
        
        mov ax, [b]
        cwde
        mov ebx, eax ; b
        mov al, [a]
        cbw
        cwde
        mov ecx, eax ; a
        mov eax, [c]
        cdq
        
        sub eax, ecx
        sbb edx, 0
        add eax, ebx
        adc edx, 0
        
        mov ebx, [d]
        mov ecx, [d+4]
        
        sub eax, ebx
        sbb edx, ecx
        
        mov [x], eax
        mov [x+4], edx
        
        mov eax, [d]
        mov edx, [x+4]
        
        mov ebx, [c]
        add eax, ebx
        adc edx, 0
        
        mov ebx, eax
        mov ecx, edx
        
        mov al, [a]
        cbw
        cwde
        
        sub ebx, eax
        sbb ecx, 0
        
        mov ax, [b]
        cwde
        sub ebx, eax
        sbb ecx, 0
        
        mov eax, [x]
        mov edx, [x+4]
        
        sub eax, ebx
        sbb edx, ecx
        
        
        ;c+d-a-b+(c-a)
        
        mov ebx, [d]
        mov ecx, [d+4]
        
        mov eax, [c]       
        add ebx, eax
        adc ecx, 0
        
        mov al, [a]
        cbw
        cwde
        sub ebx, eax
        sbb ecx, 0
        
        mov ax, [b]
        cwde
        sub ebx, eax
        sbb ecx, 0
        
        mov al, [a]
        cbw
        cwde
        mov edx, [c]
        sub edx, eax
        sbb ecx, 0
        
        add ebx, edx
        adc ecx, 0
        
        mov eax, ebx
        mov edx, ecx  ;sa fie acolo pe edx:eax in orice caz
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
