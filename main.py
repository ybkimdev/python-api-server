from fastapi import FastAPI
from gate_model import NotGate, AndGate, OrGate
from xor_gate_model import XORGate

not_gate = None
and_gate = None
or_gate = None
xor_gate = None

app = FastAPI()

@app.post("/training/not-gate")
def create_not_gate(learning_rate: float, epochs: int):
    global not_gate
    if not_gate is None:
        not_gate = NotGate()
        not_gate.training(learning_rate=learning_rate, epochs=epochs)
    return {"result": "Sucess"}

@app.post("/training/and-gate")
def create_and_gate(learning_rate: float, epochs: int):
    global and_gate
    if and_gate is None:
        and_gate = AndGate()
        and_gate.training(learning_rate=learning_rate, epochs=epochs)
    return {"result": "Sucess"}

@app.post("/training/or-gate")
def create_or_gate(learning_rate: float, epochs: int):
    global or_gate
    if or_gate is None:
        or_gate = OrGate()
        or_gate.training(learning_rate=learning_rate, epochs=epochs)
    return {"result": "Sucess"}

@app.post("/training/xor-gate")
def create_xor_gate(learning_rate: float, epochs: int, is_new_training: bool = False):
    global xor_gate

    if is_new_training:
        xor_gate = XORGate()
        xor_gate.training(learning_rate=learning_rate, epochs=epochs)
        xor_gate.save()
    else:
        if xor_gate is None:
            xor_gate = XORGate()
            if xor_gate.load() == False:
                xor_gate.training(learning_rate=learning_rate, epochs=epochs)
                xor_gate.save()
    return {"result": "Sucess"}

@app.get("/not")
def operate_not(input_a: int):
    global not_gate
    if not_gate is not None:
        return {"result": not_gate.operate([input_a])}
    else:
        return {"result": "NOT gate is not created & trained"}

@app.get("/and")
def operate_and(input_a: int, input_b: int):
    global and_gate
    if and_gate is not None:
        return {"result": and_gate.operate([input_a, input_b])}
    else:
        return {"result": "AND gate is not created & trained"}

@app.get("/or")
def operate_or(input_a: int, input_b: int):
    global or_gate
    if or_gate is not None:
        return {"result": or_gate.operate([input_a, input_b])}
    else:
        return {"result": "OR gate is not created & trained"}

@app.get("/xor")
def operate_xor(input_a: int, input_b: int):
    global xor_gate
    if xor_gate is not None:
        result = xor_gate.operate([[input_a, input_b]])
        print("Result :", result)
        return {"result": result}
    else:
        return {"result": "XOR gate is not created & trained"}

@app.get("/xor/gate-combination")
def operate_xor(input_a: int, input_b: int):
    global and_gate, or_gate, not_gate

    if and_gate is None:
        return {"result": "AND gate is not created & trained"}
    
    if or_gate is None:
        return {"result": "OR gate is not created & trained"}
    
    if not_gate is None:
        return {"result": "NOT gate is not created & trained"}
    
    and_result = and_gate.operate([input_a, input_b])
    or_result = or_gate.operate([input_a, input_b])
    not_result = not_gate.operate([or_result])

    new_input_a = and_result
    new_input_b = not_result
    xor_result = not_gate.operate([or_gate.operate([new_input_a, new_input_b])])

    return {
        "input": [input_a, input_b],
        "xor_input": [new_input_a, new_input_b],
        "result": xor_result
        }
