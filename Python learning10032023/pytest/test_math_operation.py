#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math_operation


def test_cal_addition():
    
    total = math_operation.cal_addition(4,5)
    assert total == 9
    
def test_cal_multiply():
    
    total = math_operation.cal_multiply(4,5)
    assert total == 20

