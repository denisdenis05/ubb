bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 3
    b db 9
    c db 2
    d db 9
    e dw 1
    f dw 7
    g dw 5
    h dw 3

; our code starts here
segment code use32 class=code
    start:
    
        ;first (g+5)-a*d
        
        mov al, [a]
        mov ah, 0
        mul byte [d]
        mov bx, ax
        mov ax, [g]
        add ax, 5
        sub ax, bx
    
        ;second (e+g-h)/3+b*c
        mov ah, 0
        mov al, [b]
        mul byte [c]
        mov cx, ax
        mov ax, [e]
        add ax, [g]
        sub ax, [h]
        mov bl, 3
        div bl
        add ax, cx
        mov bx, 5
        mul bx
    
    
    
        ; exit(0)
        push    dword 0      
        ; push the parameter for exit onto the stack
        call    [exit]       
        ; call exit to terminate the program
