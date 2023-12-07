Compute:

### a - byte, b - word, c - double word, d - qword - Unsigned representation
d-b+a-(b+c)
d-(a+b)+(c+c)

### a - byte, b - word, c - double word, d - qword - Signed representation
(b-a+c-d)-(d+c-a-b)
c+d-a-b+(c-a)


x-(a+b+c*d)/(9-a); a,c,d-byte; b-doubleword; x-qword
x-(a*100+b)/(b+c-1); a-word; b-byte; c-word; x-qword
