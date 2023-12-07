bits 32 


global start        

extern exit, scanf, printf
import exit msvcrt.dll   
import scanf msvcrt.dll
import printf msvcrt.dll

;Read numbers (in base 10) in a loop until the digit '0' is read from the keyboard. Determine and display the biggest number from those that have been read.

segment data use32 class=data
    a dd 0
    format dd "%d", 0 
    max dd 0
    printresult db "The biggest number is %d", 0


segment code use32 class=code
    start:
        mov al, 2
        add al, al
        
        push    dword 0   
        call    [exit]   
