from argument_parser import get_config_from_individual_day
import os
import re
from BitVector import BitVector

from day import Day
DAY = 7

class Wire:
    def __init__(self, name: str, value: int = 0) -> None:
        self.name = name
        self.input: Gate = None
        self.output: Gate = None
        self.set_value(value)
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Wire):
            return self.name == __o.name
        if isinstance(__o, str):
            return self.name == __o
    
    def __str__(self) -> str:
        return f"{self.name} ({self.value.int_val()}) from {self.input} to {self.output}"
    
    def set_value(self, value: int|BitVector) -> None:
        if isinstance(value, int):        
            self.value = BitVector(intVal = value, size=16 )
        else:
            self.value = value
        
    def get_value(self) -> int:
        return self.value.int_val()

class WireList:
    def __init__(self, wires: list[Wire]) -> None:
        self.wires = wires
    
    def set_wire_to_value(self, wire_str: str, value: int) -> None:
        self.get_wire(wire_str).set_value(value)
    
    def get_wire(self, wire_str: str) -> Wire:
        if wire_str is None or wire_str == '':
            return None
        
        try:
            value = int(wire_str)
            return Wire(wire_str, value)
        except ValueError:
            pass 
        
        for wire in self.wires:
            if wire == wire_str:
                return wire
        
    def get_list(self) -> list[Wire]:
        return self.wires

class Gate:
    def __init__(self) -> None:
        self.input1 = None
        self.input2 = None
        self.output = None
        
    def set_inputs(self, input1: Wire, input2: Wire = None) -> None:
        self.input1 = input1
        self.input2 = input2
        
        if not input1 is None:
            self.input1.output = self
        if not input2 is None:
            self.input2.output = self
        
    def set_output(self, output: Wire) -> None:
        self.output = output
        self.output.input = self
        
    def get_output_value(self):
        pass
    
    def calculate_output(self):
        self.output.set_value(self.get_output_value())

class NotGate(Gate):        
    def get_output_value(self):
        return ~self.input1.value
    
    def __str__(self) -> str:
        return f"NOT({self.input1.name})"

class AndGate(Gate):        
    def get_output_value(self):
        return self.input1.value & self.input2.value
    
    def __str__(self) -> str:
        return f"AND({self.input1.name}, {self.input2.name})"

class OrGate(Gate):        
    def get_output_value(self):
        return self.input1.value | self.input2.value
    
    def __str__(self) -> str:
        return f"OR({self.input1.name}, {self.input2.name})"

class RshiftGate(Gate):        
    def get_output_value(self):
        output = self.input1.value.deep_copy()
        output >> self.input2.value.int_val()
        return output
    
    def __str__(self) -> str:
        return f"RSHIFT({self.input1.name}, {self.input2.name})"

class LshiftGate(Gate):        
    def get_output_value(self):
        output = self.input1.value.deep_copy()
        output << self.input2.value.int_val()
        return output
    
    def __str__(self) -> str:
        return f"LSHIFT({self.input1.name}, {self.input2.name})"

def get_all_wires(instructions: list[str]) -> list[str]:
    wires = []
    for instruction in instructions:
        wires_list = re.findall(r'[a-z]+', instruction)

        for wire_string in wires_list:
            wire_present = False
            for wire in wires:
                if wire.name == wire_string:
                    wire_present = True
                    break
            
            if not wire_present:
                wires.append(Wire(wire_string))
    
    return wires

def parse_instruction(instruction: str) -> tuple[Gate, str, str, str]: # gate, input1, input2, output
    parsed_elements = re.findall(r'([a-z]+|\d+)*? *(NOT|OR|AND|RSHIFT|LSHIFT)* *([a-z]+|\d+) -> ([a-z]+)', instruction)[0]
        
    if parsed_elements[1] == 'NOT':
        gate = NotGate()
    elif parsed_elements[1] == 'OR':
        gate = OrGate()
    elif parsed_elements[1] == 'AND':
        gate = AndGate()
    elif parsed_elements[1] == 'RSHIFT':
        gate = RshiftGate()
    elif parsed_elements[1] == 'LSHIFT':
        gate = LshiftGate()
    else:
        gate = None
        
    return gate, parsed_elements[0], parsed_elements[2], parsed_elements[3]
        
def handle_gate(gate, wire1, wire2, output_wire):
    if isinstance(gate, NotGate):
        gate.set_inputs(wire2)
        gate.set_output(output_wire)
    elif isinstance(gate, OrGate):
        gate.set_inputs(wire1, wire2)
        gate.set_output(output_wire)
    elif isinstance(gate, AndGate):
        gate.set_inputs(wire1, wire2)
        gate.set_output(output_wire)
    elif isinstance(gate, RshiftGate):
        gate.set_inputs(wire1, wire2)
        gate.set_output(output_wire)
    elif isinstance(gate, LshiftGate):
        gate.set_inputs(wire1, wire2)
        gate.set_output(output_wire)
    

def run_day(day: Day) -> Day:    
    instructions = day.input
    
    # with open(f"{PATH}/../input/day{DAY}_sample.txt", 'r') as f:
    #     instructions = f.readlines()
    
    wires = WireList(get_all_wires(instructions))
    order = sorted(list(range(len(wires.get_list()))), key = lambda i: wires.get_list()[i].name)
    wires = WireList([wires.get_list()[i] for i in order])
    
    gates: list[Gate] = []
    
    for instruction in instructions:
        if instruction == 'lx -> a\n':
            continue        
        
        gate, input1, input2, output = parse_instruction(instruction)
        
        wire1 = wires.get_wire(input1)
        
        wire2 = wires.get_wire(input2)
            
        output_wire = wires.get_wire(output)
        
        if gate == None:
            wires.set_wire_to_value(output, int(input2))
        else:
            handle_gate(gate, wire1, wire2, output_wire)
            gates.append(gate)
        
    turn =0
    while(wires.get_wire("lx").get_value() == 0):
        for gate in gates:
            gate.calculate_output()
        turn += 1
    
    for wire in wires.get_list():
        print(wire)
            
    print(turn)    
    
    
    day.set_description(f"")
    day.set_result(f"{wires.get_wire('lx').get_value()}")
            
    return day




if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config_from_individual_day()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT:
        print(day)