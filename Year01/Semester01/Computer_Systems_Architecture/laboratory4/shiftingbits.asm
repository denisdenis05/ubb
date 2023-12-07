bits 32

global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    a db 0b0110_1101 ;Given 4 bytes, compute in AX the sum of the integers represented by the bits 4-6 of the 4 bytes.
    b db 0b1011_0011
    c db 0b1000_1110
    d db 0b0101_1010
    
segment code use32 class=code
    start:
        ; Given 4 bytes, compute in AX the sum of the integers represented by the bits 4-6 of the 4 bytes.
        
        mov eax, 0
        
        shr byte[a],4
        shr byte[b],4
        shr byte[c],4
        shr byte[d],4
        
        add al, [a]
        adc ah, 0
        add al, [b]
        adc ah, 0
        add al, [c]
        adc ah, 0
        add al, [d]
        adc ah, 0
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
