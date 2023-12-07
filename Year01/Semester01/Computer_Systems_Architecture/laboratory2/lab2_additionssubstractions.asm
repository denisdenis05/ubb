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
    b db 4
    c db 7
    d db 2 

; our code starts here
segment code use32 class=code
    start:
    
        ; a+b-c+d-(a-d)
    
        mov ax, [a]
        add ax, [b]
        add ax, [c]
        add ax, [d]
        mov bx, [a]
        sub bx, [d]
        sub ax, bx
    
    
        ;second a+b-c+d
        
        mov bx, [a]
        add bx, [b]
        sub bx, [c]
        add bx, [d]
        
        ;third
        
        
    
        ; exit(0)
        push    dword 0      
        ; push the parameter for exit onto the stack
        call    [exit]       
        ; call exit to terminate the program
