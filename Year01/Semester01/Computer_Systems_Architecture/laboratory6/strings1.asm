bits 32

global start

extern exit
import exit msvcrt.dll

section data use32 class=data:
    s dd 12345607h, 1A2B3C15h, 13A33412h
    slength equ ($-s)/4
    d times slength db 0
    seven db 7
    
section code use32 class=code:
    start:
        mov ecx, slength
        sub ecx, 1
        mov esi, s
        
        mov edi, 0
        startoftheloop:
            ;mov edi, slength
            ;sub edi, ecx
            ;sub edi, 1

            mov eax, 0
            mov edx, 0
            lodsb
            add esi, 3
            mov bl, al
            div byte [seven]
            test ah, ah
            jnz end_of_adding_to_d
            
            mov [d+edi], bl
            
            end_of_adding_to_d:
              
                add edi, 1
                cmp edi, ecx
                jbe startoftheloop
        
    push dword 0
    call [exit]