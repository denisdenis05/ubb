bits 32

global start

extern exit
import exit msvcrt.dll

section data use32 class=data:
    s db 'Probrema nr 28'
    slength equ $-s 
    substring db 'r'
    s2 times slength db 0

;Being given a string of bytes and a substring of this string, eliminate all occurrences of this substring from the initial string.

section code use32 class=code:
    start:
        mov ecx, slength
        sub ecx, 1
        mov esi, s
        mov edi, 0
        mov edx, 0
        startoftheloop:
            ;
            mov eax, 0
            lodsb
            cmp al, [substring]
            je end_of_adding_to_s2
            
            mov [s2+edx], al
            add edx, 1
            
            end_of_adding_to_s2:
            
                add edi, 1
                cmp edi, ecx
                jbe startoftheloop
            
    push dword 0
    call [exit]