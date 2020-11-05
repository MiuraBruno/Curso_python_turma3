#!/usr/bin/env python
# coding: utf-8

# ## **Faça um programa que recebe um número inteiro como argumento e calcule todas as tabuadas de 1 até n variando de 0 a 10 em cada tabuada

# In[20]:


n = int(input('Informe um número:\n'))


# In[5]:


for i in range(0,n+1):
    for j in range(0,11):
        #print('%d * %d = %d' %(i,j,i * j))
        pass
    print('-' * 30)


# In[21]:


i = 0
while i < n+1:
    j = 0
    while j < 11:
        #print('%d * %d = %d' %(i,j,i * j))
        j = j + 1
    print('-'*30)
    i = i + 1


print('Sucesso')



