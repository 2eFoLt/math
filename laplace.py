class LaplaceTable:
    table = {
    }

    def lookup(self, number):
        precision = 0
        if number < 3.0:
            precision = 2
        elif number < 4.0:
            precision = 1
        tgt = round(number, precision)
        print(f"{number} rounded to {tgt} with {precision} precision")
        found = self.table.get(tgt)
        print(tgt, found)
        if found is None:
            if tgt < 3.0:
                tgt = round(tgt - 0.01, 2)
                print("<3.0 lower, searching", tgt)
                # try searching with lower precision, upwards
                return self.table.get(tgt)
            elif tgt < 4.0:
                tgt = round(tgt - 0.1, 1)
                print(tgt)
                return self.table.get(tgt)
            # else left - right method, abs?
        else:
            return found


laplace_object = LaplaceTable()
with open("laplace") as table:
    for line in table:
        key, value = line.split(' ')
        key = float(key.replace('\n', '').replace(',', '.'))
        value = float(value.replace('\n', '').replace(',', '.'))
        laplace_object.table[key] = value

print(laplace_object.table)
print(laplace_object.lookup(4.44))