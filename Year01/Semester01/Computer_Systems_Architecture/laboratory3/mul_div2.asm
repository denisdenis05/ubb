bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 56
    b db 21
    c dw 66
    x dq 98

; our code starts here
segment code use32 class=code
    start:
        ; x-(a*100+b)/(b+c-1); a-word; b-byte; c-word; x-qword
    
        mov dx, 0
        mov ax, 100
        mov bx, [a]
        imul bx
        
        push dx
        push ax
        pop ebx
        
        mov al, [b]
        cbw
        cwde
        add ebx, eax
        
        mov al, [b]
        cbw
        mov cx, ax
        mov ax, [c]
        add ax, cx
        sub ax, 1
        cwde
        
        mov ecx, eax
        mov eax, ebx
        cdq
        
        
        idiv ecx
        
        mov ebx, [x]
        mov ecx, [x+4]
        
        sub ebx, eax
        sbb ecx, 0
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
