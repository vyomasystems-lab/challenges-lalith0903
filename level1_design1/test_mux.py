# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
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

    select = random.randint(0, 29)
    dut.sel.value = select

    if select == 0:
        value = dut.inp0.value
    elif select == 1:
        value = dut.inp1.value
    elif select == 2:
        value = dut.inp2.value
    elif select == 3:
        value = dut.inp3.value
    elif select == 4:
        value = dut.inp4.value
    elif select == 5:
        value = dut.inp5.value
    elif select == 6:
        value = dut.inp6.value
    elif select == 7:
        value = dut.inp7.value
    elif select == 8:
        value = dut.inp8.value
    elif select == 9:
        value = dut.inp9.value
    elif select == 10:
        value = dut.inp10.value
    elif select == 11:
        value = dut.inp11.value
    elif select == 12:
        value = dut.inp12.value
    elif select == 13:
        value = dut.inp13.value
    elif select == 14:
        value = dut.inp14.value
    elif select == 15:
        value = dut.inp15.value
    elif select == 16:
        value = dut.inp16.value
    elif select == 17:
        value = dut.inp17.value
    elif select == 18:
        value = dut.inp18.value
    elif select == 19:
        value = dut.inp19.value
    elif select == 20:
        value = dut.inp20.value
    elif select == 21:
        value = dut.inp21.value
    elif select == 22:
        value = dut.inp22.value
    elif select == 23:
        value = dut.inp23.value
    elif select == 24:
        value = dut.inp24.value
    elif select == 25:
        value = dut.inp25.value
    elif select == 26:
        value = dut.inp26.value
    elif select == 27:
        value = dut.inp27.value
    elif select == 28:
        value = dut.inp28.value
    elif select == 29:
        value = dut.inp30.value
    else:
        value = 0
    
    dut.out.value = value
    #print(value)
    print(dut.out.value)

    cocotb.log.info('for select {select}: the output is {valu}'.format(select=dut.sel.value,valu = dut.out.value))
    #assert dut.out.value == value, 'Test is failed for select {0} in 20_x_1 Mux'.format(select)