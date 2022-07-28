from fileinput import filename
from os import remove
from unicodedata import decimal


Instructioncode = {
    'opcode'    : {
        'add'   : '000000',
        'addi'  : '001000',
        'addiu' : '001001',
        'addu'  : '000000',
        'and'   : '000000',
        'andi'  : '001100',
        'beq'   : '000100',
        'bne'   : '000101',
        'j'     : '000010',
        'jal'   : '000011',
        'jr'    : '000000',
        'lbu'   : '100100',
        'lhu'   : '100101',
        'll'    : '110000',
        'lui'   : '001111',
        'lw'    : '100011',
        'nor'   : '000000',
        'or'    : '000000',
        'ori'   : '001101',
        'slt'   : '000000',
        'slti'  : '001010',
        'sltiu' : '001011',
        'sltu'  : '000000',
        'sll'   : '000000',
        'srl'   : '000000',
        'sb'    : '101000',
        'sc'    : '111000',
        'sh'    : '101001',
        'sw'    : '101011',
        'sub'   : '000000',
        'subu'  : '000000',
        'div'   : '000000',
        'divu'  : '000000',
        'lwc1'  : '110001',
        'ldc1'  : '110101',
        'mfhi'  : '000000',
        'mflo'  : '000000',
        'mfc0'  : '010000',
        'mult'  : '000000',
        'multu' : '000000',
        'sra'   : '000000',
        'swc1'  : '111001',
        'sdc1'  : '111101'},
    'function'  : {
        'add'   : '100000',
        'addu'  : '100001',
        'and'   : '100100',
        'jr'    : '001000',
        'nor'   : '100111',
        'or'    : '100101',
        'slt'   : '101010',
        'sltu'  : '101011',
        'sll'   : '000000',
        'srl'   : '000010',
        'sub'   : '100010',
        'subu'  : '100011',
        'div'   : '011010',
        'divu'  : '011011',
        'mfhi'  : '010000',
        'mflo'  : '010010',
        'mfc0'  : '000000',
        'mult'  : '011000',
        'multu' : '011001',
        'sra'   : '000011'},
    'type'  :{
        'add'   : 'R',
        'addu'  : 'R',
        'and'   : 'R',
        'jr'    : 'R',
        'nor'   : 'R',
        'or'    : 'R',
        'slt'   : 'R',
        'sltu'  : 'R',
        'sll'   : 'R',
        'srl'   : 'R',
        'sub'   : 'R',
        'subu'  : 'R',
        'div'   : 'R',
        'divu'  : 'R',
        'mfhi'  : 'R',
        'mflo'  : 'R',
        'mfc0'  : 'R',
        'mult'  : 'R',
        'multu' : 'R',
        'sra'   : 'R',
        'addi'  : 'I',
        'addiu' : 'I',
        'andi'  : 'I',
        'beq'   : 'I',
        'bne'   : 'I',
        'lbu'   : 'I',
        'lhu'   : 'I',
        'll'    : 'I',
        'lui'   : 'I',
        'lw'    : 'I',
        'ori'   : 'I',
        'slti'  : 'I',
        'sltiu' : 'I',
        'sb'    : 'I',
        'sc'    : 'I',
        'sh'    : 'I',
        'sw'    : 'I',
        'lwc1'  : 'I',
        'ldc1'  : 'I',
        'swc1'  : 'I',
        'sdc1'  : 'I',
        'j'     : 'J',
        'jal'   : 'J',},
    '$zero' : '00000',
    '$0'    : '00000',
    '$at'   : '00001',
    '$1'    : '00001',
    '$v0'   : '00010',
    '$2'    : '00010',
    '$v1'   : '00011',
    '$3'    : '00011',
    '$a0'   : '00100',
    '$4'    : '00100',
    '$a1'   : '00101',
    '$5'    : '00101',
    '$a2'   : '00110',
    '$6'    : '00110',
    '$a3'   : '00111',
    '$7'    : '00111',
    '$t0'   : '01000',
    '$8'    : '01000',
    '$t1'   : '01001',
    '$9'    : '01001',
    '$t2'   : '01010',
    '$10'   : '01010',
    '$t3'   : '01011',
    '$11'   : '01011',
    '$t4'   : '01100',
    '$12'   : '01100',
    '$t5'   : '01101',
    '$13'   : '01101',
    '$t6'   : '01110',
    '$14'   : '01110',
    '$t7'   : '01111',
    '$15'   : '01111',
    '$s0'   : '10000',
    '$16'   : '10000',
    '$s1'   : '10001',
    '$17'   : '10001',
    '$s2'   : '10010',
    '$18'   : '10010',
    '$s3'   : '10011',
    '$19'   : '10011',
    '$s4'   : '10100',
    '$20'   : '10100',
    '$s5'   : '10101',
    '$21'   : '10101',
    '$s6'   : '10110',
    '$22'   : '10110',
    '$s7'   : '10111',
    '$23'   : '10111',
    '$t8'   : '11000',
    '$24'   : '11000',
    '$t9'   : '11001',
    '$25'   : '11001',
    '$k0'   : '11010',
    '$26'   : '11010',
    '$k1'   : '11011',
    '$27'   : '11011',
    '$gp'   : '11100',
    '$28'   : '11100',
    '$sp'   : '11101',
    '$29'   : '11101',
    '$fp'   : '11110',
    '$30'   : '11110',
    '$ra'   : '11111',
    '$31'   : '11111',
    'syscall' : '00000000000000000000000000001100'}
label ={}
def readinstruction(filename):
    file1 = open(filename, "r")
    inss = []
    inss = file1.readlines()
    file1.close()
    return inss
def frontProcess(filenamein, filenameout):
    #xoa ", ()"
    instr = readinstruction(filenamein)
    file2 = open("output_after_clear_','.txt", "w")
    elem = []
    for strr in instr:
        elem = strr.translate(strr.maketrans(',', ' '))
        elem = elem.translate(elem.maketrans('(', ' '))
        elem = elem.translate(elem.maketrans(')', ' '))
        file2.write(elem)
        file2.write('\n')
    file2.close()
    
    #xoa #njanjndjf
    instr = readinstruction("output_after_clear_','.txt")
    file2 = open("output_after_clear_comment.txt", "w")
    elem = []
    for strr in instr:
        if strr.find('#') == -1:
            file2.write(strr)
        else:
            elem = strr.split('#')
            if len(elem) > 1:
                file2.write(elem[0])
                file2.write('\n')
    file2.close()

    #xoa space*n va .data .text va cac thu con lai
    instr = readinstruction("output_after_clear_comment.txt")
    file2 = open(filenameout, "w")
    elem = []
    have_data = False
    meet_text = False
    pc = int('0x00400000', 16)/4
    for strr in instr:
        elem = strr.split()
        if elem == []:
            continue
        if elem[0] == '.data':
            have_data = True
            continue
        if elem[0] == '.text':
            meet_text = True
            continue
        if not(have_data == meet_text):
            continue        
        if elem[0] not in list(Instructioncode['opcode'].keys()) and elem[0] != 'syscall':
            label[elem[0][0:-1]] = pc
            elem.remove(elem[0])
            if elem == []:
                continue
        file2.write(" ".join(elem))
        if len(elem) == 1 and elem[0] != 'syscall':
            file2.write(' ')
            continue
        pc += 1
        file2.write('\n')
    file2.close()

def R_Type(words):
    if words[0] == 'jr':
        res = '00000011111000000000000000001000'
    else:
        opcode = Instructioncode['opcode'][words[0]]
        rs = Instructioncode[words[2]]
        rt = Instructioncode[words[3]]
        rd = Instructioncode[words[1]]
        shamt = '00000'
        if words[0] == 'sll' or words[0] == 'srl':
            rs = '00000'
            rt = Instructioncode[words[2]]
            if int(words[3]) > 0:
                shamt = bin(int(words[3]))[2:]
                shamt = shamt.zfill(5)
            else: 
                shamt = bin(2**5 + int(words[3]))[2:]
        funct = Instructioncode['function'][words[0]]
        res = opcode + rs + rt + rd + shamt + funct
    return res

def I_Type(words, pc):
    opcode = Instructioncode['opcode'][words[0]]
    rt = Instructioncode[words[1]]
    if words[0] == 'lui':
        rs = '00000'
        if words[2][0:2] == '0x':
            temp = int(words[2], 16)
            if temp > 0:
                immediate = bin(temp)[2:]
                immediate = immediate.zfill(16)
            else: 
                immediate = bin(2**16 + temp)[2:]
        elif words[2][0:2] == '0b':
            immediate = words[2:].zfill(16)
        else:
            temp = int(words[2])
            if temp > 0:
                immediate = bin(temp)[2:]
                immediate = immediate.zfill(16)
            else: 
                immediate = bin(2**16 + temp)[2:]
    elif words[0] == 'beq' or words[0] == 'bne':
        rs = Instructioncode[words[1]]
        rt = Instructioncode[words[2]]
        temp = int(label[words[3]]) - pc
        if temp > 0:
            immediate = bin(temp)[2:]
            immediate = immediate.zfill(16)
        else: 
            immediate = bin(2**16 + temp)[2:]
    elif words[0] in list(('sb', 'sc', 'sh', 'sw', 'lbu', 'lhu', 'll', 'lw')):
        rs = Instructioncode[words[3]]
        if int(words[2]) >= 0:
            immediate = bin(int(words[2]))[2:]
            immediate = immediate.zfill(16)
        else: 
            immediate = bin(2**16 + int(words[2]))[2:]
    else:
        rs = Instructioncode[words[2]]
        if int(words[3]) > 0:
            immediate = bin(int(words[3]))[2:]
            immediate = immediate.zfill(16)
        else: 
            immediate = bin(2**16 + int(words[3]))[2:]
    res = opcode + rs + rt + immediate
    return res
    
def J_Type(words):
    opcode = Instructioncode['opcode'][words[0]]
    temp = int(label[words[1]])
    if temp > 0:
        address = bin(temp)[2:]
        address = address.zfill(26)
    else: 
        address = bin(2**26 + temp)[2:]
    res = opcode + address
    return res
def backProcess(filenamein, filenameout):
    pc = int("0x00400000", 16)
    pc = int(pc/4)
    ins = readinstruction(filenamein)
    file1 = open(filenameout, "w")
    for strr in ins:
        pc += 1
        words = strr.split()
        if words[0] == 'syscall':
            bincode = Instructioncode['syscall']
        elif Instructioncode['type'][words[0]] == 'R':
            bincode = R_Type(words)
        elif Instructioncode['type'][words[0]] == 'I':
            bincode = I_Type(words, pc)
        else:
            bincode = J_Type(words)
        file1.write(bincode)
        file1.write('\n')
    file1.close()
def BirToHex(filenamein,filenameout):
    fileBir = open(filenamein,"r")
    fileHex = open(filenameout,"w")
    for line in fileBir:
        res = ''
        word = line.split()
        word = word[0]
        for i in range(0,29,4):
            if word[i:i+4]=='0000':
                res +='0'
            if word[i:i+4]=='0001':
                res +='1'
            if word[i:i+4]=='0010':
                res +='2'
            if word[i:i+4]=='0011':
                res +='3'
            if word[i:i+4]=='0100':
                res +='4'
            if word[i:i+4]=='0101':
                res +='5'
            if word[i:i+4]=='0110':
                res +='6'
            if word[i:i+4]=='0111':
                res +='8'
            if word[i:i+4]=='1000':
                res +='8'
            if word[i:i+4]=='1001':
                res +='9'
            if word[i:i+4]=='1010':
                res +='a'
            if word[i:i+4]=='1011':
                res +='b'
            if word[i:i+4]=='1100':
                res +='c'
            if word[i:i+4]=='1101':
                res +='d'
            if word[i:i+4]=='1110':
                res +='e'
            if word[i:i+4]=='1111':
                res +='f'
        fileHex.write(res)
        fileHex.write('\n')
    fileHex.close()
    fileBir.close()



filename1 = "input_for_compiler.asm" 
filename2 = "output_after_front_processing.txt"
filename3 = "bin.txt"
filename4 = "hex.txt"
frontProcess(filename1, filename2)
backProcess(filename2, filename3)
BirToHex(filename3,filename4)
