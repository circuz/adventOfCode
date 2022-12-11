INPUT = "./day11_input"

class Monkey():
    def __init__(self,name = "Nameless monkey",items = []):
        self.name = name 
        self.items = items
        self.operation = ["*","1"] # default is do nothing
        self.test = 2
        self.doTrue = 0
        self.doFalse = 1
        self.inspects = 0

    def add_item(self,item):
        self.items.append(int(item))
        return

    def set_operation(self,operation_text):
        new_operation = operation_text.split(" ")[3:]
        self.operation = new_operation
        return

    def set_test(self, test_text):
        self.test = int(test_text[:-1].split(" ")[-1])
        return

    def set_dotrue(self, dotrue_text):
        self.doTrue = int(dotrue_text[:-1].split(" ")[-1])
        return

    def set_dofalse(self, dofalse_text):
        self.doFalse = int(dofalse_text[:-1].split(" ")[-1])
        return

    def inspect_items(self, scd):
        new_items = []
        for item in self.items:
            self.inspects += 1
            if self.operation[0] == "*":
                if self.operation[1] == "old":
                    new_items.append(item * item)
                    continue
                new_items.append(item*int(self.operation[1]))
                continue
            if self.operation[1] == "old":
                new_items.append(item + item)
                continue
            new_items.append(item + int(self.operation[1]))
            continue
        self.items = [item % scd for item in new_items ]
        return

    def gets_bored(self):
        self.items = [item // 3 for item in self.items ]
        return

    def test_item(self, item):
        if item != self.items[0]:
            print("uh oh...")
        self.items = self.items[1:]
        if item % self.test == 0:
            give_to = self.doTrue
        else:
            give_to = self.doFalse
        return give_to
                
                
def create_monkeys(lines): 
    monkeys = []
    scd = 1
    for line in lines:
        if "Monkey" in line:
            name = line[7]
        elif "Starting" in line:
            items = eval("[" + line[18:-1] + "]")
        elif "Operation" in line:
            current_monkey = Monkey(name, items)
            current_monkey.set_operation(line[13:-1])
            monkeys.append(current_monkey)
        elif "Test:" in line:
            current_monkey.set_test(line)
            scd *= int(line[:-1].split(" ")[-1])
        elif "true:" in line:
            current_monkey.set_dotrue(line)
        elif "false:" in line:
            current_monkey.set_dofalse(line)
            
    return monkeys, scd

def show_monkey(monkey):
    print(f"""Monkey {monkey.name}:
        items: {monkey.items}
        operation: {monkey.operation}
        test: divisible by {monkey.test}
            if true: toss to monkey {monkey.doTrue}
            if false: toss to monkey {monkey.doFalse}
        and has inspected {monkey.inspects} items.""")

def take_turn(monkey, monkey_list, scd):
    monkey.inspect_items(scd)
    for item in monkey.items:
        monkey_list[monkey.test_item(item)].add_item(item)

    return
        

if __name__ == "__main__":
    with open(INPUT,'r') as lines:
        monkey_list, scd = create_monkeys(lines)
        print(scd)
        #print(monkey_list)
        #for monkey in monkey_list:
        #    show_monkey(monkey)
        for i in range(10000):
            for monkey in monkey_list:
                take_turn(monkey, monkey_list, scd)
                #print("New monkey!")
                #for monkey in monkey_list:
                    #print(monkey.items)
                #show_monkey(monkey)
        top_two = [0,0]
        for monkey in monkey_list:
            if monkey.inspects > min(top_two):
                top_two = [monkey.inspects, max(top_two)]
            show_monkey(monkey)
        print(top_two, top_two[0] * top_two[1])
