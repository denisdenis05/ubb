bits 32 


global start        

extern exit, scanf, fopen, fprintf, fclose
import exit msvcrt.dll   
import scanf msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll

;Read two numbers a and b (base 10) from the keyboard and calculate: (a+b)*(a-b). The result of multiplication will be stored in a variable called "result" (defined in the data segment).

segment data use32 class=data
    a dw 0
    b dw 0
    format dd "%d", 0 
    result dd 0
    file db "output.txt", 0
    readtype db "a+", 0
    file_descriptor db 0
    
segment code use32 class=code
    start:
        startoftheloop:
            push a
            push format
            call [scanf]
            add esp, 4*2
        
            mov ecx, 0
            check_lowercase:
                mov al, [a + ecx] 
                cmp al, 0   
                je end_loop

                cmp al, 'a'  
                jg lowercase
                
                cmp al, 'z'  
                jl lowercase

                jmp end_loop
                inc ecx
                jmp check_lowercase
            
            
            lowercase:
            push file
            push readtype
            call [fopen]
            add esp, 4*2
            mov [file_descriptor], eax
            push dword a
            push dword [file_descriptor]
            call [fprintf]
            add esp, 4*2
            push dword [file_descriptor]
            call [fclose]
            add esp, 4

                
            end_loop:
        
        
        
        push    dword 0   
        call    [exit]   
