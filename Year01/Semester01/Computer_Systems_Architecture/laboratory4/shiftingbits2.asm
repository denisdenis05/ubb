bits 32

global start        

extern exit               
import exit msvcrt.dll    
segment data use32 class=data
    a dq 0b1001_0110_1001_1011_1101_1101_1011_1111_1001_0110_1001_1111_1101_1101_1011_1111
    b dd 0
    c db 0
    N db 0
    ;Given the quadword A, obtain the integer number N represented on the bits 17-19 of A. 
              ;Then obtain the the doubleword B by rotating the high doubleword of A N positions to the left. Obtain the byte C as follows:
                ;the bits 0-2 of C are the same as the bits 9-11 of B
                ;the bits 3-7 of C are the same as the bits 20-24 of B

segment code use32 class=code
    start:
        
        mov eax, [a+4] ;first 0-15 bits gone
        mov ebx, 0b0000_0000_0000_0000_0000_0000_0000_1110
        and eax, ebx
        shr eax, 1
        mov [N], eax
        mov cl, [N]
        
        mov ebx, [a+4]
        rol ebx, cl
        mov [b], ebx
        
        mov ecx, 0b0000_0000_0000_0000_0000_1110_0000_0000
        and ebx, ecx
        shr ebx, 9
        mov [c], ebx
        
        mov ebx, [b]
        mov ecx, 0b00000_0001_1111_0000_0000_0000_0000_0000
        and ebx, ecx
        shr ebx, 17
        or [c], ebx
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
