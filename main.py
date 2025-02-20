from fastapi import FastAPI
from gate_model import NotGate, AndGate, OrGate

not_gate = None
and_gate = None
or_gate = None

app = FastAPI()

@app.post("/training/not-gate")
def create_not_gate(learning_rate: float, epochs: int):
    global not_gate
    if not_gate is None:
        not_gate = NotGate()
        not_gate.training(learning_rate=learning_rate, epochs=epochs)
    return {"result": "Sucess"}

@app.post("/training/and-gate")
def create_not_gate(learning_rate: float, epochs: int):
    global and_gate
    if and_gate is None:
        and_gate = AndGate()
        and_gate.training(learning_rate=learning_rate, epochs=epochs)
    return {"result": "Sucess"}

@app.post("/training/or-gate")
def create_not_gate(learning_rate: float, epochs: int):
    global or_gate
    if or_gate is None:
        or_gate = OrGate()
        or_gate.training(learning_rate=learning_rate, epochs=epochs)
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
