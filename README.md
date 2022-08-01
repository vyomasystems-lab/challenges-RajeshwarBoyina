# Level 1 Design 1

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://imgur.com/a/X4sqWdA)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 5-bit input *sel* and 31 2-bit input's and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.inp12.value = 1
dut.sel.value = 12
```

The assert statement is used for comparing the Multiplexer's outut to the expected value.

The following errors are seen:
Bug 1
```
assert dut.out.value == ip, "Test failed with: inp = {inp12}, sel = {sel} and out = {out}".format(inp12=dut.inp12.value, sel=dut.sel.value, out=dut.out.value)
                     AssertionError: Test failed with: inp = 01, sel = 01100 and out = 00
```
Bug 2
```
assert dut.out.value == 3, "Test failed with: inp = {inp30}, sel = {sel} and out = {out}".format(inp30=dut.inp30.value, sel=dut.sel.value, out=dut.out.value)
                     AssertionError: Test failed with: inp = 11, sel = 11110 and out = 00
```

## Test Scenario **(Important)**
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end
```
For the adder design, the logic should be ``a + b`` instead of ``a - b`` as in the design code.


challenges-RajeshwarBoyina created by GitHub Classroom
