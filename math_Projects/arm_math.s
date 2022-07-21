

.data
.balign 4
  message: .asciz "Escribe un numero: "
.balign 4
  scan_pattern: .asciz "%d"
.balign 4
  n: .word 0
.global main
main:
  ldr r0, =message
  bl printf
  ldr r1, =scan_pattern
  ldr r0, =n
  bl scanf
parte1:
  @parte 1: 1 +  2**2 + 3**2...n**2
  mov r1, #1 @resultado
  mov r2, #2 @contador
loop:
  cmp r2, r0
  bgt parte2 @branch if r2 > r0
  fmuls r3, r2, r2
  add r1, r1, r3
  add r2, r2, #1
  b loop
parte2:
  @(n(n+1)(2n+1))/6
  add r2, r0, #1
  add r3, r2, r0
  fmuls r2, r3, r2 @fmuld
  fmuls r2, r2, r0
  fdivs r2, r2, 6
end:
  cmp r1, r2
  bne notEqual @branch if r1 != r2
  mov r0, #1
  b end
notEqual:
  mov r0, #0
end:
  bx lr

.global pritf
.global scanf
