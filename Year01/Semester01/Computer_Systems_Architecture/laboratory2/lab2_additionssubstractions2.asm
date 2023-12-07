bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 7
    b dw 9
    c dw 12
    d dw 2

; our code starts here
segment code use32 class=code
    start:
    
    ; first    
        mov ax, [a]
        add ax, [a]
        sbb ax, [c]
        
        mov bx, [b]
        add bx, [b]
        add bx, [d]
    
        sbb ax,bx
    
    ; second
    
        mov cx, [d]
        sbb cx, [a]
        
        mov dx, [b]
        add dx, [b]
        sbb dx, [c]
        sbb dx, [a]
        
        sbb cx, dx
        add cx, [d]
        
        
        ; exit(0)
        push    dword 0      
        ; push the parameter for exit onto the stack
        call    [exit]       
        ; call exit to terminate the program
