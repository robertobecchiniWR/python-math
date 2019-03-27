#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:48:03 2019

@author: telu
"""


# %% 1)
def rotation(abc, p):
    n = len(abc)
    return abc[p:n]+abc[0:p]


print('Question 1)')
abc = 'abcde'
print(rotation(abc, 1), rotation(abc, 2), rotation(abc, -1))


# %% 2)
def generer_dico(abc, p):
    abc_code = rotation(abc, p)
    dico = {}
    for i in range(len(abc)):
        dico[abc[i]] = abc_code[i]
    return dico


print('Question 2)')
abc = 'abcde'
print(generer_dico(abc, 2))


# %% 3)
def coder_message(msg, p):
    dico = generer_dico('abcdefghijklmnopqrstuvwxyz', p)
    msg_code = ''
    for c in msg:
        if c in dico:
            msg_code += dico[c]
        else:
            msg_code += c
    return msg_code


print('Question 3)')
print(coder_message("c'bon le fromage suisse", 2))

# %% 4)
print('Question 4)')
print(coder_message("gh nf yr qebvg q'nyyre qbezve znvagranag", -13))
