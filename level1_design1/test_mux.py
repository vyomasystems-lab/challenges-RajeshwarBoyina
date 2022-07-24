# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for sel = 12 and inp12 = 1"""
    ip = 1
    sel = 12

    dut.inp12.value = ip
    print("***The mux is being tested***")
    dut.sel.value = sel
    await Timer(2, units='ns')
        
    dut._log.info(f'inp12={dut.inp12.value} sel={dut.sel.value} Expectedout=01 DUT={dut.out.value}')
    assert dut.out.value == ip, "Test failed with: inp = {inp12}, sel = {sel} and out = {out}".format(inp12=dut.inp12.value, sel=dut.sel.value, out=dut.out.value)

@cocotb.test()
async def test_mux_2(dut):
    """Test for sel = 30 and inp30 = 3"""

    dut.inp30.value = 3
    dut.sel.value = 30
    print("***The mux is being tested***")

    await Timer(2, units = 'ns')
    dut._log.info(f'inp30={dut.inp30.value} sel={dut.sel.value} Expectedout=03 DUT={dut.out.value}')
    assert dut.out.value == 3, "Test failed with: inp = {inp30}, sel = {sel} and out = {out}".format(inp30=dut.inp30.value, sel=dut.sel.value, out=dut.out.value)
    