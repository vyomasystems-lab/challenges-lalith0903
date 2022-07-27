# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    m1 = 1
    m2 = 2
    m3 = 3
    m4 = 0
    m5 = 1
    m6 = 2
    m7 = 3
    m8 = 0
    m9 = 3
    m10 = 2
    m11 = 0
    m12 = 1
    m13 = 2
    m14 = 3
    m15 = 0
    m16 = 1
    m17 = 2
    m18 = 3
    m19 = 0
    m20 = 1
    m21 = 2
    m22 = 3
    m23 = 0
    m24 = 3
    m25 = 2
    m26 = 0
    m27 = 1
    m28 = 2
    m29 = 3
    m30 = 0
    m31 = 2
    
    #input driving
    dut.inp0.value = m1
    dut.inp1.value = m2
    dut.inp2.value = m3
    dut.inp3.value = m4
    dut.inp4.value = m5
    dut.inp5.value = m6
    dut.inp6.value = m7
    dut.inp7.value = m8
    dut.inp8.value = m9
    dut.inp9.value = m10
    dut.inp10.value = m11
    dut.inp11.value = m12
    dut.inp12.value = m13
    dut.inp13.value = m14
    dut.inp14.value = m15
    dut.inp15.value = m16
    dut.inp16.value = m17
    dut.inp17.value = m18
    dut.inp18.value = m19
    dut.inp19.value = m20
    dut.inp20.value = m21
    dut.inp21.value = m22
    dut.inp22.value = m23
    dut.inp23.value = m24
    dut.inp24.value = m25
    dut.inp25.value = m26
    dut.inp26.value = m27
    dut.inp27.value = m28
    dut.inp28.value = m29
    dut.inp29.value = m30
    dut.inp30.value = m31

    await Timer(10, units='us')

    sel1 = random.randint(0, 29)
    dut.sel.value = random.randint(0, 30)
    if sel1 == 0:
        valu = dut.inp0.value
    elif sel1 == 1:
        valu = dut.inp1.value
    elif sel1 == 2:
        valu = dut.inp2.value
    elif sel1 == 3:
        valu = dut.inp3.value
    elif sel1 == 4:
        valu = dut.inp4.value
    elif sel1 == 5:
        valu = dut.inp5.value
    elif sel1 == 6:
        valu = dut.inp6.value
    elif sel1 == 7:
        valu = dut.inp7.value
    elif sel1 == 8:
        valu = dut.inp8.value
    elif sel1 == 9:
        valu = dut.inp9.value
    elif sel1 == 10:
        valu = dut.inp10.value
    elif sel1 == 11:
        valu = dut.inp11.value
    elif sel1 == 12:
        valu = dut.inp12.value
    elif sel1 == 13:
        valu = dut.inp13.value
    elif sel1 == 14:
        valu = dut.inp14.value
    elif sel1 == 15:
        valu = dut.inp15.value
    elif sel1 == 16:
        valu = dut.inp16.value
    elif sel1 == 17:
        valu = dut.inp17.value
    elif sel1 == 18:
        valu = dut.inp18.value
    elif sel1 == 19:
        valu = dut.inp19.value
    elif sel1 == 20:
        valu = dut.inp20.value
    elif sel1 == 21:
        valu = dut.inp21.value
    elif sel1 == 22:
        valu = dut.inp22.value
    elif sel1 == 23:
        valu = dut.inp23.value
    elif sel1 == 24:
        valu = dut.inp24.value
    elif sel1 == 25:
        valu = dut.inp25.value
    elif sel1 == 26:
        valu = dut.inp26.value
    elif sel1 == 27:
        valu = dut.inp27.value
    elif sel1 == 28:
        valu = dut.inp28.value
    elif sel1 == 29:
        valu = dut.inp30.value
    
    
    dut.out.value = valu
    #print(value)
    print(dut.out.value)

    cocotb.log.info('for select {sel1}: the output is {valu}'.format(sel1=dut.sel.value,valu = dut.out.value))
    #assert dut.out.value == value, 'Test is failed for select {0} in 20_x_1 Mux'.format(select)