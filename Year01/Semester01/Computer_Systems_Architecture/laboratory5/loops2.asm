bits 32 

global start        

extern exit              
import exit msvcrt.dll   

segment data use32 class=data
    s1 db '+', '4', '2', 'a', '8', '4', 'X', '5'
    lengths1 equ $-s1 
    s2 db 'a', '4', '5'
    lengths2 equ $-s2
    d db 0
    x dd 3

segment code use32 class=code
    start:
        
        mov esi, -1
        mov ecx, 0
        mov cl, lengths1 ;ecx= lengths1
        
        startofiteration1:
            
            mov ebx, 0
            mov bl, [d+esi] ;display???
            
            mov ebx, 0
            mov bl, lengths1
            sub ebx, ecx 
            
            mov edx, 0
            mov eax, 0
            mov eax, ebx
            div dword [x]
            test edx, edx
            jnz endofadding
            
                
            add esi, 1
            mov al, [s1+ebx]
            mov [d+esi], al
            
            endofadding:
            
                sub ecx, 1
                test ecx, ecx
                jnz startofiteration1
        
        mov ecx, 0
        mov cl, lengths2 
        sub ecx, 1 ;ecx= lengths2-1
        startofiteration2:
            
            mov ebx, 0
            mov bl, [d+esi] ;display???
            
            mov al, [s2+ecx]
            mov [d+esi], al
            add esi, 1
            sub ecx, 1
            jnz startofiteration2
            
        push    dword 0  
        call    [exit]      
