bits 32 

global start        

extern exit             
import exit msvcrt.dll    


;A byte string S is given. Obtain the string D1 which contains the elements found on the even positions of S and the string D2 which contains the elements found on the odd positions of S.
;Example:
;S: 1, 5, 3, 8, 2, 9
;D1: 1, 3, 2
;D2: 5, 8, 9

segment data use32 class=data
    s db 1, 5, 3, 8, 2, 9
    slength equ $-s
    
    x dd 2
    
    d1 times slength db 0
    d2 times slength db 0
    
    

segment code use32 class=code
    start:
    
        mov esi, 0
        mov edi, 0
        
        mov ecx, 0
        mov cl, slength ;ecx= lengths1
        
        startofiteration1:
            
            mov ebx, 0
            mov bl, slength
            sub ebx, ecx 
            
            mov edx, 0
            mov eax, 0
            mov eax, ebx
            div dword [x]
            test edx, edx
            jnz oddposition 
            
                
            
            mov al, [s+ebx]
            mov [d2+esi], al
            add esi, 1
            jmp endofadding
            
            
            oddposition:
                mov al, [s+ebx]
                mov [d1+edi], al
                add edi, 1
                
                endofadding:
                    sub ecx, 1
                    test ecx, ecx
                    jnz startofiteration1
    
        push    dword 0    
        call    [exit]       