class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []


        for ops in operations:
            if ops == "C":
                records.pop()

            elif ops == "D":
                records.append(records[-1] * 2)

            elif ops == "+":
                records.append(records[-1] + records[-2])

            else:
                records.append(int(ops))

        return sum(records)    