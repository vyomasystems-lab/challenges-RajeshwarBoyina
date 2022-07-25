# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    inp_seq = (1,0,1,0,1,1)
    for i in range(len(inp_seq)):
        dut.inp_bit.value = inp_seq[i]
        await FallingEdge(dut.clk)

    dut._log.info(f"The test with Output={bool(dut.seq_seen.value)}, Expected Out=True")
    assert dut.seq_seen.value == True, f"The Test failed at input seq = 101011, the expected op is True and the test output is {bool(dut.seq_seen.value)}" 
    cocotb.log.info('#### CTB: Develop your test here! ######')

@cocotb.test()
async def test_seq_bug2(dut):


    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    print("-->",dut.next_state.value, dut.current_state.value, bool(dut.seq_seen.value))

    inp_seq = (1,1,0,1,1)
    
    for i in range(len(inp_seq)):
        dut.inp_bit.value = inp_seq[i]
        #print("***",dut.next_state.value, dut.current_state.value, bool(dut.seq_seen.value))
        await FallingEdge(dut.clk)
        print(dut.next_state.value, dut.current_state.value, bool(dut.seq_seen.value), dut.inp_bit.value)

    dut._log.info(f"The test with Output={bool(dut.seq_seen.value)}, Expected Out=True")
    assert dut.seq_seen.value == True, f"The Test failed at input seq = 11011, the expected op is True and the test output is {bool(dut.seq_seen.value)}" 