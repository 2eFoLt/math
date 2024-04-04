import json


class LaplaceTable:
    table = {
    }

    def lookup(self, number):
        if number < 3.0:
            number = round(number, 2)
            if self.table.get(number) is None:
                return self.table.get(round(number - 0.01, 2))
            return number, self.table.get(number)
        elif number < 4.0:  # 3.26
            number = round(number, 1)  # 3.3
            if self.table.get(number) is None:  # None -> True
                return self.table.get(round(number - 0.1, 1))
            return number, self.table.get(number)
        else:  # 4.44
            number = round(number, 1)  # 4.4
            # print(number)
            with open("laplace") as table:
                for line in table:
                    key, value = line.split(' ')
                    key = float(key.replace('\n', '').replace(',', '.'))
                    value = float(value.replace('\n', '').replace(',', '.'))
                    laplace_object.table[key] = value
            tgt_array = [4.0, 4.5, 5.0]
            delta_array = [round(abs(tgt_array[i] - number), 1) for i in range(len(tgt_array))]
            # print(delta_array)
            tgt = tgt_array[delta_array.index(min(delta_array))]
            return tgt, self.table.get(tgt)


laplace_object = LaplaceTable()
with open("laplace") as table:
    laplace_object.table = json.JSONDecoder().decode(table.readline())

print(laplace_object.lookup(3.43732))