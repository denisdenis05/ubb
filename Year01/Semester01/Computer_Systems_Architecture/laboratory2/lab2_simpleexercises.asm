bits 32 ;assembling for the 32 bits architecture
global start
 
 

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
        ; msvcrt.dll contains exit, printf and all the other important C-runtime functions

 

; our variables are declared here (the segment is called data) 
segment data use32 class=data
; ...

a db 2
b db 8
c db 13
d db 5
 
; the program code will be part of a segment called code
segment code use32 class=code
start:
; ... 
;2+8
mov bl,[a]
add bl, [b]

;13/5
mov ax, 0
mov al, [c]
div byte [d]

    ; call exit(0) ), 0 represents status code: SUCCESS
    push dword 0 
    ; saves on stack the parameter of the function exit
    call [exit] 
    ; function exit is called in order to end the     execution of the program